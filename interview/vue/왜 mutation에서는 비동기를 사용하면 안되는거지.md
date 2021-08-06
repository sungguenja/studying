# 왜 mutation에서는 비동기를 사용하면 안되는거지?

[참고 링크](https://happy-coding-day.tistory.com/m/134?category=713313)

우리는 공식 문서나 어디서 vue를 학습하는 경우에 vuex를 보면 항상 듣는 말이 있다. `mutation에서 async처리를 하지 말아라 actions에서 처리해야 한다` ​

## :thinking: 왜?

일단 vuex의 요소들을 한번 살펴보자

- state
  - 여러 컴포넌트 간에 공유할 데이터
  - 즉, 상태이다! 변경되면 DOM을 업데이트할 트리거 역할을 할 수 있음
- getter
  - computed()처럼 미리 연산된 값을 접근하는 속성입니다. 첫번째 인자값으로 state를 받고 두번째 인자로는 getter을 받을 수가 있다
- mutations
  - 오늘의 주인공
  - state의 값을 변경할 수 있는 유일한 방법이자 메서드이다.
  - mutations은 commit()으로 동작시킨다.
  - mutations은 이벤트와 유사하며, 첫번째 인자로 state를 받는다. 두번째 인자로는 이벤트로 넘길 payload로 추가 전달인자를 사용할 수 있습니다
  - 왜 여기서만 수정하죠?
    - 추적의 용이성이 가장 크다
- action
  - 비동기 처리 로직을 선언하는 메서드이다.
  - 데이터 요청, promise, async 같은 것은 여기서 처리하자

호출되는 순서를 살펴보면 아래와 같다

- methods 영역에서 mutations의 이벤트를 commit할 경우
- mutations의 commit이 끝나지 않은 시점!
  - method의 이벤트가 끝남
- 즉, state의 값이 적절하게 변경되지 않은 상태에서 getter에서 state의 값을 읽어들이기 위한 행위를 시도한다!
  - 그로인해 이슈가 발생한다.

즉, 역으로 생각하면 mutations의 commit이 호출되는 시점이 actions의 필요 이유인 것이다.

시간차를 두고 mutations의 같은 함수를 여러 컴포넌트에 commit 하여 state를 변경할 경우 이를 추적하기 어렵기 때문에 actions에 두는 것!