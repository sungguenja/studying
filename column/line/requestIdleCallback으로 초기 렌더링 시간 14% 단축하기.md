# requestIdleCallback으로 초기 렌더링 시간 14% 단축하기

[해당 칼럼 링크](https://engineering.linecorp.com/ko/blog/line-securities-frontend-4/)

최적화를 위해 어떤 생각을 해야하는지, ~~의심 또 의심 하십시오~~ 많고 다양한 방면을 보고 다른 서비스(구글신)들은 어떠한 방법을 이용했는지 참고해보는 것도 좋다는 것 같다

## 작업 환경

LINE 증권의 프런트 엔드는 TypeScript와 React로 구성되어 있고 JavaScript번들은 webpack으로 생성한다고 한다.

프론트 엔드의 전형적인 지표는 [Core Web Vitals](https://web.dev/vitals/)가 있다. 그리고 측정 수단은 Google Chrome확장 프로그램인 Lighthouse를 사용할 수가 있다

## 성능 개선 실시

LINE증권은 CSR을 이용하고 있다. 그래서 콘텐츠 표시하려면 JavaScript 번들을 읽고 실행해야 한다. 전형적인 방안으로는 **레이지 로딩을 이용한 번들 분할이 있다.** 이정도로는 부족할 수가 있다. 추가적인 방안은 아래쪽 콘텐츠를 표시하는데 필요한 JavaScript를 다른 파일로 분할해서 나중에 로딩한 후 실행하도록 하는 방법이다.

## 수상한 appendChild

appendChild는 당연히 일어나기 마련이다. 그런데 이따금 이유를 알 수 없는 appendChild가 보일 수가 있다. 그것은 webpack의 런타임일 가능성이 있다. 해당 상황을 설명하는 두가지 요인이 있다.

1. import()

   import()에 해당하는 코드를 실행할 때 webpack런타임이 그 자리에서 동기적으로 스크립트 요소를 생성하고 임베딩을 실시한다

2. react의 lazy()

   해당 팀은 성능 개선을 위해 react의 해당 기능도 이용하고 있다. 문제는 lazy로 생성한 컴포넌트가 렌더링한 시점에서 동기적으로 콜백 함수를 호출한다.

이 두가지 처리가 모두 동기적으로 실행된 결과, appendChild가 초기 렌더링 처리에 섞이게 되었다

## requestIdleCallback 함수 도입

[참고자료1](https://developers.google.com/web/updates/2015/08/using-requestidlecallback) [참고자료2](https://www.w3.org/TR/requestidlecallback/)

requestIdleCallback은 브라우저의 메인 스레드가 비어 있으면 지정한 콜백 함수를 실행하도록 지시할 수 있는 함수이다. 

초기 렌더링하는 동안에 메인 스레드를 최대한 활용하여 콘텐츠를 보여주는 방식을 생각하는 것이다. 실제로 구글도 이러한 접근법을 많이 이용한다. 아래와 같이 간단하게 구현이 가능하다

```javascript
import { lazy } from 'react'

export const lazyIdle: typeof lazy = (factory) => {
    return lazy(
    	() => new Promise((resolve) => {
            window.requestIdleCallback(() => resolove(factory()), {
                timeout: 3000
            })
        })
    )
}

// 사용법
const OtherContents = lazyIdle(() => import('./otherContents'));
```



