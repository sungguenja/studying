# withCredentials

> 1. 서론
> 2. 개념
> 3. 결론

## 1. 서론

프론트엔드 개발자로 일을 하다보면 자주 만나는 것 중 하나는 당연히 cors일 것이다. 그리고 이것에 대한 해결법으로 `withCredentials` 속성을 true로 바꾸라는 말을 자주 들을 것이다.
<br/>
그렇다면 이것은 도당체 무엇일까? 한번 살펴보도록 하자

## 2. 개념

MDN에 정리되어 있는 것을 살펴보자. (영어밖에 없어서 정리할 겸.....)
<br/>

### MDN

> withCredentials는 쿠키와 인증 해더 또는 TLS클라이언트 인증서같은 credentials를 이용하여 크로스 사이트 요청을 만드는 것을 나타내는 `boolean` 값이다.
> 추가로, 이 플래그는 쿠키가 응답에서 무시될 수 있도록 나타내는 데에 이용되기도 한다. 기본값은 `false`이다.

### 간단한 정리

- 요청을 하기 전에 withCredentials가 true로 설정되어 있지 않으면 다른 도메인의 XMLHttpRequest가 자신의 도메인에 대한 쿠키 값을 설정할 수 없음
- withCredentials를 true로 설정하여 얻은 타사 쿠키는 여전히 동일한 출처 정책을 준수하므로 document.cookie 또는 응답 헤더를 통해 요청하는 스크립트에서 액세스 할 수 없음

## 3. 결론

이것을 True값으로 만드는게 무조건 해결이 아니다.
<br/>
위에 글에서도 알 수 있지만 결론적으로 이것은 `HTTP Cookies`나 `HTTP Authentication`정보를 가지는 요청을 말하는 것이다. 즉, 특정 api들이 이런걸 오히려 거부한다면 우리는 요청을 할시에 의도적으로 `false`로 나타내주는 것이 오히려 cors를 해결할 수 있을 것이다.
<br/>
즉, cors를 해결하기 위해서는 결론적으로 여러 기법들과 공식 api문서를 비교하면서 어떤 헤더값이 필요한 지 어떤 body가 필요한지 정확히 따져야하는 것이다!

## 참고자료

- [Hello, Freakin world!](https://javachoi.tistory.com/52)
- [수학과의 좌충우돌 프로그래밍](https://ssungkang.tistory.com/entry/React-axios-%EC%9D%98-withCredentials)
- [crontab](https://cron-tab.github.io/2018/05/31/http-cors-credentials/)
- [mdn](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/withCredentials)
