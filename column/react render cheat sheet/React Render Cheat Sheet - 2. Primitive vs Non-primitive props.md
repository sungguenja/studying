# React Render Cheat Sheet - 2. Primitive vs Non-primitive props

차일드 컴포넌트가 `memo`로 감싸져있다. props도 바뀌지 않는다 하지만 rerender가 계속되는 케이스도 있다! 그것은 자바스크립트의 두가지 타입때문이다. 타입의 차이를 생각해라.

## Primitives

이 경우가 우리가 기억하는 케이스이다. memo로 해두면 rerender되는 것을 방지할 수 있고 쉘로우 딥으로 비교 가능하기 때문이다.

## Non-primitives

이 타입의 경우(스타일을 props로 내리는 케이스 같은 경우). 이것은 항상 전의 상황과 비교할 때 false를 나오게 하고 그것은 리렌더를 하게 만든다. [You don't know JS](https://github.com/getify/You-Dont-Know-JS/blob/2nd-ed/get-started/apA.md#values-vs-references)

여기에는 익명함수도 포함이다. 그러니 왠만하면 함수를 네임화 시켜서 이벤트 객체를 받게 하는 것이 좋다

