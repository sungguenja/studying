# redux 간단 정리

[글 링크1](https://kyun2da.dev/%EB%9D%BC%EC%9D%B4%EB%B8%8C%EB%9F%AC%EB%A6%AC/Redux-%EC%A0%95%EB%A6%AC/) [글 링크2](https://13akstjq.github.io/redux/2019/12/14/redux-redux%EC%99%84%EB%B2%BD%EC%A0%95%EB%A6%AC.html) [글 링크3 여기는 직접 보는게 제일 좋다](https://ridicorp.com/story/how-to-use-redux-in-ridi)

- 기본 용어

  1. 액션

     상태에 변화가 필요하다면 액션을 일으켜야 한다

     ```javascript
     {
        type: 'ADD_TODO',
        data: {
            id: 1,
            text: '리덕스 배우기'
        }
     }
     ```

  2. 액션 생성함수

     액션 객체를 만들어주는 함수

     ```javascript
     function addTodo(data) {
      return {
        type: 'ADD_TODO',
        data,
      }
     }
     ```

  3. 리듀서

     리듀서는 현재 상태와 액션 객체를 받아, 필요하다면 새로운 상태를 리턴해주는 함수. 이벤트 리스너라고 생각하면 편안

     ```javascript
     const initialState = {
      counter: 1,
     }
     function reducer(state = initialState, action) {
      switch (action.type) {
        case INCREMENT:
          return {
            counter: state.counter + 1,
          }
        default:
          return state
      }
     }
     ```

  4. 스토어

     상태 저장소. 하나만 가질 수 있다

  5. 디스패치

     스토어의 내장 함수 중 하나인 디스패치는 액션 객체를 넘겨주고 이벤트 실행시킴

  6. 구독

     상태가 업데이트될 때마다 호출시키게 해줌

  7. 셀렉터

     상태값을 가져올 때 이용

- 