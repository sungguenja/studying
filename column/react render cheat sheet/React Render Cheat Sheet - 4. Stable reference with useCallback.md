# React Render Cheat Sheet - 4. Stable reference with useCallback

자 `memo`를 이용해서 변수 변화에 대해 rerender를 막는것은 잘 봤다! 하지만 함수의 경우는?

## function in javascript

그냥 함수를 내려준다면 무조건 리랜더링이 되는데 다음과 같은 자바스크립트에서 함수의 케이스를 보면 너무나도 당연하다

```javascript
const a = () => 1;
const b = () => 1;
a === b // false
a === a // true
```

함수는 1급 객체이다. 그러니 이런 경우는 당연하게 나온다. 그렇다면 어떻게 해야하지?

## The `useCallback`

`useCallback`은 `useMemo`의 함수 버전이라고 생각하면 된다. dependency를 걸어준 요소만 변하지 않는다면 함수 자체를 기억해서 props로 내려줄 수가 있다.

단! props로 내릴때 다시 익명함수로 감싸지 말자! 좋은 선택이 아니다. 왜 굳이 그러는거야....

그리고 `useState`에서 전의 값과 관련이 있다면 아래와 같이 해주는 것이 좋다

```react
// State update
setCount(count + 1)

// Functional state update
setCount(prevCount => prevCount + 1)
```

