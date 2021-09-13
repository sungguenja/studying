# Pure Functional Component in React

[컬럼 링크](https://blog.logrocket.com/react-pure-components-functional/)

> 서론은 조금 생략하고 바로 본론으로 넘어가겠습니다

## 퓨어 컴포넌트가 뭔데

- 반환된 값은 인풋값에 의해서만 정해진다
- 인풋값이 같다면 항상 아웃풋이 같다

순수함수와 같다고 할 수가 있따

그러면 이제 반대로 순수 함수형 컴포넌트는 의외로 웃긴 말이라는 것을 알 수가 있다. 순수 함수 자체가 이미 위와 같기 때문이다.

## 퓨어 컴포넌트는 어떻게 작동하지?

```react
import React from 'react';

class PercentageStat extends React.PureComponent {

  render() {
    const { label, score = 0, total = Math.max(1, score) } = this.props;

    return (
      <div>
        <h6>{ label }</h6>
        <span>{ Math.round(score / total * 100) }%</span>
      </div>
    )
  }

}

export default PercentageStat;
```

## 함수형 컴포넌트는 그럼 퓨어함?

이론적이라면 퓨어할 것이다.

## `{pure}` HOC를 리컴포즈로부터 이용하자

[요런 패키지가 있다](https://github.com/acdlite/recompose) HOC를 제공하는 라이브러리인데 이것으로 리액트에서 HOC효과를 이용해볼 수도 있다

하지만 난 바닐라 리액트가 좋다 (근데 이것도 표현이 좀 이상하네. 바닐라 자바스크립트가 이미 아닌데?ㅋㅋㅋ)

## React.memo

이제 그런 효과는 해당 메소드를 이용해 활용할 수가 있다. memo를 통해 전에 인풋과 같다면 굳이 렌덜이 하지 않는 방식으로 이용해볼 수가 있다. 아래와 같은 규칙을 가진다.

1. React.memo는 HOC이다. 리액트 구성 요소를 첫 번째 인수로 사용하고 특별한 종류의 react 구성 요소를 반환
2. 특수 react구성 요소 유형을 반환한다. 이를 통해 렌더러를 메모하고 전의 상황과 비교가 가능하다
3. 함수형에서 이용하자

