# master the javascript interview: what is a closure?

[컬럼링크](https://medium.com/javascript-scene/master-the-javascript-interview-what-is-a-closure-b2f0d2152b36#.nkow9q73g)

클로저는 중요합니다. 왜냐하면 그들은 특정 함수에 있는 범위와 없는 범위를 제어하며, 같은 포함 범위 내에서 다른 함수와 어떤 변수가 공유되는지 제어하기 때문입니다. 변수들과 함수들이 어떻게 관계를 가지는지 이해를 하는 것은 당신의 함수적, 객체 지향적 프로그래밍 스타일에서 함수에서 무엇이 일어나는지 이해하는데 치명적이다.

이 질문에 대해 미스하는 것은 인터뷰에서 매우 디스어드밴티지한 것이며 이것은 클로저가 일하는 방식에 대한 이해도 떨어짐 어필과 깊이 없는 경험과 이해를 했다는 빨간깃발~~^^7~~의 표시이다. 자바스크립트뿐만이 아니다. 다른 언에서도 클로저는 많은 관련이 있다.

클로저에 대한 이해없이 자바스크립트 코딩은 문법을 모르고 영어를 말하는것과 같다(되던데?) - 너는 좋은 아이디어를 가지고 있어도 그것을 어색하게 표현할 것이다. 그리고 너는 누군가가 쓴 코드를 이해하는 능력에 대해 또한 취약해질 것이다

클로저에 대한 몇 사용 예를 한번 살펴보자. 클로저는 자바스크립트에서 객체 데이타 프라이버시를 위해 이벤트 핸들러와 콜백 함수에서 자주 사용되며, 부분 어플리케이션, 커링, 그리고 다른 함수형 프로그래밍 패턴에서도 이용된다.

자 그렇다면 이 질문에 대해 접근해보자! "클로저의 일반적인 두가지 사용예를 말해주실 수 있나요?"

## 클로저가 먼데 ~~씹덕아~~

클로저는 주위의 스테트들의 레퍼런스와 함께 번들되어진 함수와의 콤비네이션이다. 또다른 말로는 클로저는 당신에게 밖에서 함수 스코프를 접근할 권한을 준다! 자바스크립트에서, 클로저는 항상 만들어진다. 함수가 만들어질때 그때마다

클로저를 사용하기 위해 함수를 정의하고 안에서 또다른 함수를 정의해고 expose한다. 함수를 expose하기위해 리턴해주거나 또다른 함수에게 넘겨준다

안쪽 함수는 접근할 것이다 다른 함수 스코프에, 심지어 함수가 이미 리턴이 되었더라도

## 클로저를 써보아양! (예시들)

다른 이유들 중에서, 클로저는 객체 데이터 프라이버시를 주기 위해 일반적으로 사용된다. 데이터 프라이버시는 implementation이 아닌 인터페이스를 프로그래밍하는데 도와주는 아주 핵심적인 요소이다. 이것은 좀 더 강력한 소프트웨어를 만들도록 돕는 중요한 컨셉이다. 왜냐하면 implementation details은 인터페이스 컨셉보다 급격하게 바뀔 가능성이 있다.

자바스크립트에서, 데이터 프라이버시를 용이하게 하는 아주 원시적인 방법이 클로저다. 데이터 프라이버시를 위해 당신이 클로저를 사용할 때, 동봉된 변수들은 컨테이닝 함수안에서만 스코프된다. 너는 어떤 방법으로도 밖에서 데이터를 얻을 수가 없다. 자바스크립트에서, 어떤 expose된 메소드든 정의한다 클로져 스코프와 함께. 아래 예를 보자

```javascript
const getSecret = (secret) => {
    return {
        get: () => secret
    };
};

test('Closure for object privacy.', assert => {
    const msg = '.get() should have access to the Closure.';
    const expected = 1;
    const obj = getSecret(1);
    
    const actual = obj.get();
    
    try {
        assert.ok(secret, 'This throws an error.');
    } catch (e) {
        assert.ok(true, 'The secret var is only available to privileged methods');
    }
    
    assert.equal(actual,expected,msg);
    assert.end()
})
```

위의 예제에서, `.get()` 메소드는 `getSecret()`의 스코프 안에서 정의 되었다. 객체는 데이터 프라이버시를 제공하는 유일한 방법이 아니다. 클로저 또한 그들의 상태에 영향을 줄 수 있는 변수를 리턴해주는 스테이트풀한 함수를 만드는데 이용될 수 있다. 

```javascript
const secret = (msg) => () => msg;

test('secret', assert => {
  const msg = 'secret() should return a function that returns the passed secret.';

  const theSecret = 'Closures are easy.';
  const mySecret = secret(theSecret);

  const actual = mySecret();
  const expected = theSecret;

  assert.equal(actual, expected, msg);
  assert.end();
});
```

함수적 프로그래밍에 있어서 클로저는 부분적 어플리케이션이나 커링을 위해 자주 이용된다.

어플리케이션: 함수를 인수에 적용하여 반환하는 것을 산출하는 프로세스

부분적 어플리케이션: 함수 일부 argument에 적용하기 위한 프로세스입니다. 부분적으로 적용된 함수는 나중에 사용할 수 있도록 반환. 부분 응용 프로그램은 반환된 함수 내에서 하나 이상의 인수를 수정하고 반환된 함수는 함수 응용 프로그램을 완료하기 위해 나머지 매개 변수를 인수로 사용한다

부분적 어플리케이션은 파라미터를 고치는 대신 클로저의 이점을 가져간다. 너는 타겟함수에 인수를 적용시키기 위해 일반적인 함수를 쓸 수도 있다. 아래와 같은 시그니쳐를 따를 것이다.

`partialApply(targetFunction: Function, ...fixedArgs: Any[]) =>
  functionWithFewerParams(...remainingArgs: Any[])`

어떤 수의 인수든 취하는 것은 함수를 취할 것이며, 우리가 일부분 함수에 적용하길 원하는 인수들에 의해 따라가게 될 것이며, 인수를 의미하는 것들을 보여주는 함수를 리턴해줄 것이다. 아래와 같은 예를 보자

`const add = (a,b) => a+b;`

너는 이제 어떤 숫자에든 10을 더하는 함수를 원한다. 너는 `add10()`함수를 부를 것이다. 그리고 그 결과의 예는 `add10(5)`같은 것일 것이고 저거의 리턴값은 15일 것이다. 우리의 부분적 적용 함수는 아래와 같이 일어날 수 있다

```javascript
const add1- = partialApply(add,10);
add10(5);
```

이 예에서 10은 고정된 파라미터이다. `partialApply`는 아래와 같이 정의될 것이다

```javascript
const partialApply = (fn,...fixedArgs) => {
    return function (...remainingArgs) {
        return fn.apply(this, fixedArgs.concat(remainingArgs));
    };
};
```

