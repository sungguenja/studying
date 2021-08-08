# Master the JavaScript Interview: What is Functional Programming?

[칼럼 링크](https://medium.com/javascript-scene/master-the-javascript-interview-what-is-functional-programming-7f218c68b3a0)

자바스크립트 세상에서 함수형 프로그래밍은 진짜로 뜨거운 토픽이다. 몇년 전만해도 적은 JS 프로그래머들만 알았지만 큰 어플리케이션 코드베이스들이 다들 함수형 프로그래밍에 근간을 두고 있다

함수형 프로그램밍은 상태, 변경 가능한 데이터, 사이드 이팩트를 피하는 순수 함수 조합으로 소프트웨어를 만드는 과정이다. 함수형 프로그램밍은 명영적보다 더 선언적이고 어플리케이션 상태 플로우는 순수함수를 통해 흐른다. 

## 상태 공유

상태 공유는 공유 스코프에 있거나 스코프 간에 전달되는 객체의 속성으로 존재하는 어떤 변수, 객체 또는 메모리 공간이다. 공유된 스코프는 클로저나 글로벌 스코프를 포함한다. 종종 객체지향 프로그래밍에서 객체는 다른 객체에 속성을 추가하는 식으로 스코프간에 공유된다.

상태 공유의 문제점은 함수의 이팩트를 이해하는 것이다. 당신은 공유되는 변수에 대해서 함수의 사용과 이팩트들 전체 역사를 알아야 한다. 아래 예를 보자

```javascript
// With shared state, the order in which function calls are made
// changes the result of the function calls.
const x = {
  val: 2
};

const x1 = () => x.val += 1;

const x2 = () => x.val *= 2;

x1();
x2();

console.log(x.val); // 6

// This example is exactly equivalent to the above, except...
const y = {
  val: 2
};

const y1 = () => y.val += 1;

const y2 = () => y.val *= 2;

// ...the order of the function calls is reversed...
y2();
y1();

// ... which changes the resulting value:
console.log(y.val); // 5
```

공유되는 상태가 계속해서 변화한다. 이런 경우 우리는 함수에 대한 예상치 못한 사이드 이팩트가 발생하는 순간 프로그램은 망가지기 시작할 것이다. 그렇다면 위 코드를 조금 갈아보자

```javascript
const x = {
  val: 2
};

const x1 = x => Object.assign({}, x, { val: x.val + 1});

const x2 = x => Object.assign({}, x, { val: x.val * 2});

console.log(x1(x2(x)).val); // 5


const y = {
  val: 2
};

// Since there are no dependencies on outside variables,
// we don't need different functions to operate on different
// variables.

// this space intentionally left blank


// Because the functions don't mutate, you can call these
// functions as many times as you want, in any order, 
// without changing the result of other function calls.
x2(y);
x1(y);

console.log(x1(x2(y)).val); // 5
```

우리는 `Object.assign()`을 이용했고 빈 오브잭트를 첫번째 파라미터로 주면서 x의 속성을 변화시키는 대신에 복사했다. 이 경우에 새 객체를 간단하게 만들었고 객체들은 변하지 않았다.

## 불변성

불변하는 객체는 만들어진 이래로 수정된 적없는 객체이다. 변화가능한 객체는 만들어진 이래로 수정이 될 수 있는 객체이다. JS에서 불변하는 객체를 만드는 방법은 아래와 같다.

```javascript
const a = Object.freeze({
  foo: 'Hello',
  bar: 'world',
  baz: '!'
});

a.foo = 'Goodbye';
// Error: Cannot assign to read only property 'foo' of object Object
```

하지만 위 방법도 아래와 같이 객체 안에 객체가 있다면 허점이 존재한다.

```javascript
const a = Object.freeze({
  foo: { greeting: 'Hello' },
  bar: 'world',
  baz: '!'
});

a.foo.greeting = 'Goodbye';

console.log(`${ a.foo.greeting }, ${ a.bar }${a.baz}`);
```

주의해서 정의할 수 있도록 하자! 많은 함수형 프로그래밍 언어에서 특별한 불변 데이터 구조를 만들고 그것을 `trie data structures`라고 부른다. `Trie`는 적은 메모리를 사용하고 성능 향상을 위한 오퍼레이트에 의해 복사되어진 바뀌지 않는 객체의 모든 부분을 메모리 위치에서 참조하는 것을 공유하기 위해 구조적 공유를 이용한다.

## 사이드 이팩트

- 외부 변수 또는 객체 속성 수정
- 콘솔에 로깅
- 화면에 쓰기
- 파일에 쓰기
- 네트워크에 쓰기
- 외부 프로세스 트리거
- 부작용이 있는 다른 기능 호출

위와 같은 것들이 사이드 이팩트다. 함수형 프로그래밍에서 사이드 이팩트는 극도로 피해지는 것이다. 함수형 언어들은 순수함수에서 모나드라는 것을 이용해 사이드 이팩트를 피할려고 한다.

## 고차 함수를 통한 재사용성

- 콜백 기능, promises, 모나드 등을 사용하여 작업, 효과, 비동기 흐름 제어를 추상화하거나 독립화 시킬 수 있다
- 다양한 데이터 유형에 사용할 수 있는 유틸리티들을 만든다
- 함수 컴포지션의 재사용을 위한 목적을 위해 커리된 함수를 만들거나 인수 그자체를 함수에 추가시키기 위해
- 함수 목록을 작성하고 해당 입력 함수의 구성요소를 반환할 때

위와 같은 상황에서 고차 함수를 이용한다

### 컨테이너, 함수, 리스트, 스트림

```javascript
const double = n => n * 2;
const doubleMap = numbers => numbers.map(double);
console.log(doubleMap([2, 3, 4])); // [ 4, 6, 8 ]

///////////////////////////////////////
const double = n => n.points * 2;

const doubleMap = numbers => numbers.map(double);

console.log(doubleMap([
  { name: 'ball', points: 2 },
  { name: 'coin', points: 3 },
  { name: 'candy', points: 4}
])); // [ 4, 6, 8 ]
```

위부터 살펴보자. `map()` 은 당신이 데이터 타입을 추상화 하는 것을 허락한다. 위와같이 리스트 를 두배로 만드는 함수를 만드는 것은 어렵지 않다. 아래의 경우를 보면 객체를 엮는 것도 가능하다. 추상화사용의 컨셉은 고차 함수와 functor와 같다.

## 선언적 vs 명령형

```javascript
const doubleMap = numbers => {
  const doubled = [];
  for (let i = 0; i < numbers.length; i++) {
    doubled.push(numbers[i] * 2);
  }
  return doubled;
};

console.log(doubleMap([2, 3, 4])); // [4, 6, 8]

//////////////////////
const doubleMap = numbers => numbers.map(n => n * 2);

console.log(doubleMap([2, 3, 4])); // [4, 6, 8]
```

위가 명령형 아래가 선언형이다. 명령형은 흐름을 이해하는데에는 문제는 없지만 코드가 길어지긴 한다. 선언형을 이용하여 추상화를 한다면 간결해지고 기능을 잘 이해하고 있다면 명료해지기까지 한다.