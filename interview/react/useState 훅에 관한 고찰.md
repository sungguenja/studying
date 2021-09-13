# useState 훅에 관한 고찰

[참고 자료 1](https://velog.io/@jjunyjjuny/React-useState%EB%8A%94-%EC%96%B4%EB%96%BB%EA%B2%8C-%EB%8F%99%EC%9E%91%ED%95%A0%EA%B9%8C) [참고 자료 2](https://velog.io/@dlwlrma/%EB%AC%B4%EC%A7%80%EC%84%B1-React-%EB%A6%AC%EB%A0%8C%EB%8D%94%EB%A7%81-%EB%A7%89%EA%B3%A0-%EC%8B%B6%EC%96%B4%EC%9A%94....feat-%EC%82%AC%EC%9A%A9%EC%9E%90-%EC%BB%B4%ED%8F%AC%EB%84%8C%ED%8A%B8%EB%8A%94-%EB%AC%B4%EC%A1%B0%EA%B1%B4-%EB%8C%80%EB%AC%B8%EC%9E%90%EB%A1%9C)

- useState를 포함한 hooks는 react 모듈에 선언되어있는 함수이고,
- 실행 될 때 마다 dispatcher를 선언하고 useState 메소드 실행해서 그 값을 반환한다
- 할당부를 거슬러 올라가니 dispatcher는 전역 변수 ReactCurrentDispatcher로부터 가져온다.

즉, react자체의 **클로저**를 이용한다는 뜻이다.

그렇다면 useState로 나오는 setter는 어떻게 작동을 할까?

1. 웹이 로딩되고 최초로 App함수가 호출
   - App은 인수를 useState에게 전달
   - useState는 실행될 때마다 초기값을 전달받지만, 내부적으로 _value값이 undefined인지 확인
     - 최초의 호출에만 초기값을 _value에 할당하고, 이후 초기값은 사용되지 않는다
   - 이후 _value와 그 값을 재할당하는 setState함수를 배열에 담아 반환
2. setState 호출
   - 전달 받은 값을 react모듈 상단의 _value에 할당
   - 컴포넌트 리랜더링을 시작
3. setState로 인한 리렌더링 발생
   - 새로운 jsx 반환
   - App함수 자체가 두번째로 실행된다
     - 그때
     - 다시 인수 0을 useState에 전달하며 호출
     - useState는 내부적으로 _value값을 확인하고 undefined가 아닌 값이 할당이 되어있다는 것을 확인해 할당안함
     - 이후 현재 시점의 useState가 선언된 시점에서 _value와 setState를 반호나
     - 두번째 실행된 App함수 내부에서 useState가 반환한 값을 비구조화 할당으로 추출해 변수에 할당

즉, setState는 자신과 함께 반환된 변수를 변경시키는게 아니라, **변경된 값을 useState가 가져오게 하는 역할을 한다**

