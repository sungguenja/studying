# presentational & container 디자인 패턴

[해당 칼람 주소](https://kyounghwan01.github.io/blog/React/container-presenter-dessign-pattern/#presentational-container-디자인-패턴이란)

## presentational & container 디자인 패턴이란?

- 로직을 수행하는 컴포넌트와 markup을 통해 ui를 보여주는 컴포넌트를 분리시키는 패턴. 기능과 ui에 대한 구분이 쉬워진다.
- 같은 state를 다른 container에게 props 내림으로 상태 공유가 가능
- 로직 수행, markup이 다른 컴포넌트에게 하기 때문에 유지보수가 쉽고, 재사용성이 뛰어나다는 장점이 있음

## presentational component

- ui와 관련된 컴포넌트
- state를 직접 조작하지 않으며, container component가 내려준 prop의 함수에 의해 state를 변경
- 그러한 이유로 훅 사용이 기피가 된다.
- 상태를 가지지 않는 것이 특징

## container component

- 로직과 관련된 컴포넌트
- Markup하지 않고 스타일을 사용하지 않음
- 데이터와 데이터 조작에 관한 함수만이 존재