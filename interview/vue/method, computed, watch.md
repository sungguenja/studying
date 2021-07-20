# method, computed, watch

## method

vue인스턴스 내의 값에 접근 가능한 함수들의 집합이라고 생각하자. (보통 method에서 dom접근은 잘 안한다.)

## computed

computed도 데이터에 접근할 수가 있다. 그리고 로직 전개도 가능하다. 그렇다면 method와 무슨 차이가 있을까?

1. method는 template에서 호출시 ()를 적어야하지만 computed는 안적는다
2. method는 로직 전개만 하고 return이 없어도 괜찮지만 computed는 return값이 무조건 있어야 한다
3. method는 paramater를 이용할 수 있지만 computed는 받을 수 없다

어찌 보면 둘의 상위호환은 method처럼 보인다. 하지만 둘의 용도는 살짝 다르다. 동작원리가 각각 아래와 같다

- computed - template내부에 선언된 computed중에서 해당함수와 연결된 값이 바뀔 때만 해당 함수만을 실행
- methods - template내부에 선언된 methods중에서 update라이프사이클이 동작한다면 함수가 모두 실행

그러니 둘의 관점은 여기서 생각하는 것이 좋을 것이다

- 파라메터를 받아서 호출해야 하는가?
  - computed는 받을 수가 없다. 그러니 파라메터를 이용하고자 하면 무조건 methods를 쓸 수 밖에 없다
- 함수 안에서 다른 값을 바꿔줘야 하는가?
  - computed도 가능은 한데 **정책위반**이다.
- 비용적인 면
  - computed가 다른 곳의 변경은 일으키지 않기 때문에 비용적으로 이득을 본다

## watch

어찌 보면 computed와 비슷해보인다.

- computed - 특정 값을 계산해서 보여준다
- watch - 특정값이 **변동**해서 다른 작업을 한다, 하위컴포넌트에서 props가 변경되는 것을 감지하는 데에 쓰인다.

watch는 작작 쓰는게 좋은게 스파게티가 일어날 가능성이 높다