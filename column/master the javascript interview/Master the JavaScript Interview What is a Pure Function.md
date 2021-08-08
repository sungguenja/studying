# Master the JavaScript Interview: What is a Pure Function?

[컬럼 링크](https://medium.com/javascript-scene/master-the-javascript-interview-what-is-a-pure-function-d1c076bec976)

순수 함수들은 다양한 함수형 프로그래밍의 목적의 정수이고 리액트와 리덕스 어플과 연관이 있따. 하지만 순수 함수가 뭘 말하는 걸까?

순수한 함수가 무엇인지 알기 전에 함수와 친해지는게 좋은 아이디어인 듯 하다. 함수형 프로그래밍을 조금 더 쉽게 이해해 볼 수 있도록 하자

## 함수 넌 도당체 누구세요?

함수는 arguments(인수)라고 불리는 것들을 넣고 값을 얻기 위해 진행하는 과정이다. 함수는 아래와 같은 목적을 가진다

- Mapping

  입력으로 주어지는 값을 가진다.

- Procedures

  함수는 몇 스텝을 실행하기 위해 호출된다. procedural 프로그래밍에서 자주 일어난다

- I/O

  몇 함수들은 시스템의 다른 것과 연동할려고 일어난다

## 순수 함수

순수함수는 아래와 같은 함수이다

- 같은 입력이 주어지면 같은 결과를 준다
- 진행중에 사이드이팩트를 만들지 않는다

나는 당신이 순수함수에 동의하길 추천한다. 즉, 순수한 함수를 사용하여 프로그램 요구 사항을 구현하는 것이 실용적이면 다른 옵션보다 프로그램 요구 사항을 사용해야 합니다. 순수 함수는 인풋값에 베이스로 한 결과값을 인풋값에 따라 반환한다. 그들은 프로그램에서 가장 간단한 재사용 가능한 코드 블럭이다. 그리고 이것은 KISS(Keep It Simple, Stupid) 철학에 가장 잘 맞는다. 순수 함수는 심플함의 가장 최적화된 방법이다

순수 함수는 많은 이점을 가지고 함수형 프로그래밍의 근간이 된다. 순수 함수는 밖의 상태에 대해 철저하게 독립적이다. 그들은 버그에 면역이 있으며 그들의 변경 가능한 상태와만 관련이 있다.

~중략~ (대충 요약하자면 순수함수는 인풋값이 유지될 때 계속 결과값이 같아야한다는 것을 예시와 함께 설명중)

## 순수 함수는 사이드 이펙트를 만들지 않는다

### 변화하지 않음

자바스크립트의 객체 인수는 참조이다. 즉, 함수가 객체 또는 배열 파라미터의 속성을 변화시키고 변화된 상태는 밖의 함수로 접근이 가능한 상태로 만들어버린다는 것이다. 순수 함수는 외부 상태를 변경해서는 안된다.

```javascript
// impure addToCart mutates existing cart
const addToCart = (cart, item, quantity) => {
  cart.items.push({
    item,
    quantity
  });
  return cart;
};


test('addToCart()', assert => {
  const msg = 'addToCart() should add a new item to the cart.';
  const originalCart =     {
    items: []
  };
  const cart = addToCart(
    originalCart,
    {
      name: "Digital SLR Camera",
      price: '1495'
    },
    1
  );

  const expected = 1; // num items in cart
  const actual = cart.items.length;

  assert.equal(actual, expected, msg);

  assert.deepEqual(originalCart, cart, 'mutates original cart.');
  assert.end();
});
```

이것은 일단 잘 작동한다. 함수가 같은 카트를 반환한다.

변경가능한 공유하는 상태가 문제이다. 다른 함수들은 함수를 호출하기 전 카트 객체 상태와 연관이 있고 공유된 상태를 우리가 직접 변화를 준다면 우리는 어떤 효과가 일어날지 두려워 해야 한다. 코드를 리팩터링 해야함을 깨달았을 것이다. 고려된 버전을 한번 보자

```javascript
// Pure addToCart() returns a new cart
// It does not mutate the original.
const addToCart = (cart, item, quantity) => {
  const newCart = lodash.cloneDeep(cart);

  newCart.items.push({
    item,
    quantity
  });
  return newCart;

};


test('addToCart()', assert => {
  const msg = 'addToCart() should add a new item to the cart.';
  const originalCart = {
    items: []
  };

  // deep-freeze on npm
  // throws an error if original is mutated
  deepFreeze(originalCart);

  const cart = addToCart(
    originalCart,
    {
      name: "Digital SLR Camera",
      price: '1495'
    },
    1
  );


  const expected = 1; // num items in cart
  const actual = cart.items.length;

  assert.equal(actual, expected, msg);

  assert.notDeepEqual(originalCart, cart,
    'should not mutate original cart.');
  assert.end();
});
```

