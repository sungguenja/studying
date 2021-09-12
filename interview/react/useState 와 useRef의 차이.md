# useState 와 useRef의 차이

[참고 링크 1](https://velog.io/@lyj-ooz/useState-useRef%EC%9D%98-%EC%B0%A8%EC%9D%B4) [참고 링크 2](https://velog.io/@pks787/useRef-vs-variable-useState-%EC%B0%A8%EC%9D%B4%EC%A0%90)

- useState
  - set실행 이후 리렌더링이 일어남
  - 즉, 불필요한 렌더링이 일어나기도 하지만 반대로는 바로바로 변경사항이 적용될 수 있다
  - **클로저 내부까지 접근해서 수정하는게 불가**
- useRef
  - 불필요한 렌더링은 일어나지 않는다
  - 화면에 표시되지 않는 값에 대해 이용할 때 아주 좋다
  - **컴포넌트의 전 생명주기를 통해 유지되는 값이라는 의미이며, 순수한 자바스크립트 객체를 생성 및 유지시켜주기 때문에 closure 이슈가 발생하지 않는다는 걸 알 수 있다**

