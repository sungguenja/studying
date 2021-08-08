# Master the JavaScript Interview: What’s the Difference Between Class & Prototypal Inheritance?

[칼럼 링크](https://medium.com/javascript-scene/master-the-javascript-interview-what-s-the-difference-between-class-prototypal-inheritance-e4cd0a7562e9)

객체는 자바스크립트에서 자주 이용되고 효과적으로 그들이 어떻게 작동되는 지 이해하는 것은 생산성에 큰 이점을 가져다 줄 것이다. 사실은 poor 객체 지향 디자인은 프로젝트를 실패로 이끌기 마련이고 안좋은 케이스는 회사의 망함을 가져온다

다른 랭귀지들과는 다르게 자바스크립트이 객체 시스템은 프로토 타입에 기반한다. 클래스가 아닌다. 운이 안좋게도 대부분 자바스크립트 개발자들은 자바스크립트이 객체 시스템을 이해하지 못한다. 그리고 어떻게 가장 좋게 이용하는지 모른다. 나머지들은 이해하고 있지만 클래스 베이스 시스템처럼 운용을 한다. 그 결과 자바스크립트의 객체 시스템은 개별적으로 분산되어 혼돈을 가왔다. 그것은 자바스크립트 개발자가 프로토타입과 클래스 둘 다 이해해야하는 상황이 되었따

## 그래서 뭔 차이가 있는데요?

이것은 트리키한 질문이다. 당신은 아마 아래의 질문에 의존하여 대답할 것이다. 그러니 집중해서 차이점을 알아보도록 하자 어떻게 지식을 더 좋은 코드에 반영할 수 있을지 알아보자

고전적 상속: 클래스는 청사진과 같다. 클래스 상속은 서브클래스와의 관계를 만든다. 그리고 분류학적으로 생각해야한다

인스턴스들은 `new`키워드와 컨슽트럭터 함수에 의해 인스턴스화된다. 클래스 상속은 es6부터 `class`를 사용할 수도 안할 수도 있다. 클래스들은 자바같은 당신이 알고있는 다른 언어와는 다르게 자바스크립트에 기술적으로 존재하지 않는다. 대신에 컨스트럭터 함수가 사용된다. 

```javascript
class Foo {}
console.log(typeof Foo) // 'function'
```

JavaScript에서 클래스 상속은 프로토타입 상속 위에 구현되지만, 그렇다고 해서 다음과 같은 작업을 수행하는 것은 아닙니다.

자바스크립트의 클래스 상속은 자식 `Constructor.prototype`을 부모의 `Constructor.prototype`을 연결하는 프로토타입 채인을 이용한다. 보통 `super()` 컨스트럭터가 호출된다. 이러한 절차는 단일 조상 부모 자식 상속과 객체디자인에서 타이트한 커플링을 가능하게 만드는 형태를 취한다

prototypal 상속: 프로토타입은 작업 객체 인스턴스이다. 객체는 직접적으로 다른 객체들에게 상속받는다

인스턴스들은 많은 다른 소스 객체들로 구성되어있고 선택적 상속을 할 수 있고. 다른 말로 클래스 분류학은 프로토타입적 객체지향의 자동 사이드 이팩트가 아니다.. 팩토리 함수, 오브젝트 리터럴, `object.create()`를 이용해서 인스턴스화한다

## 왜 이런 문제가?

상속은 기본적으로 코드 재사용 매커니즘이다. 다양한 문제를 만들 수 있다. 특히, 클래스 상속은 부모/자식 객체 분류학같은 것을 사이드 이팩트로 만들어 버린다.

이러한 분류법은 모든 새로운 유스케이스에 대해 정확하게 파악하는 것이 사실상 불가능합니다. 그리고 널리 퍼져있는 이 기본 클레스 사용법은 부셔지기 쉬운 기본 클래스 문제로 이끈다, 그리고 그 문제는 다른 잘못을 고치기 어렵게 만든다. 사실 클래스 상속은 객체 지향 디자인의 문제로 알려져 있다

- 타이트한 커플링 문제
- 깨지기 쉬운 기본 클래스 문제
- 유연하지 못한 상속 문제
- 문제로부터의 분리
- 고릴라 바나나 문제

## 모든 상속이 나쁜가?

물론 그렇지 않다. 재사용은 산업의 기본이지 않은가 아래를 한번 살펴보자

## 세가지 다른 프로토타이적 상속

고전 상속을 한번 살펴보고 가자

```javascript
// Class Inheritance Example
// NOT RECOMMENDED. Use object composition, instead.

// https://gist.github.com/ericelliott/b668ce0ad1ab540df915
// http://codepen.io/ericelliott/pen/pgdPOb?editors=001

class GuitarAmp {
  constructor ({ cabinet = 'spruce', distortion = '1', volume = '0' } = {}) {
    Object.assign(this, {
      cabinet, distortion, volume
    });
  }
}

class BassAmp extends GuitarAmp {
  constructor (options = {}) {
    super(options);
    this.lowCut = options.lowCut;
  }
}

class ChannelStrip extends BassAmp {
  constructor (options = {}) {
    super(options);
    this.inputLevel = options.inputLevel;
  }
}

test('Class Inheritance', nest => {
  nest.test('BassAmp', assert => {
    const msg = `instance should inherit props
    from GuitarAmp and BassAmp`;

    const myAmp = new BassAmp();
    const actual = Object.keys(myAmp);
    const expected = ['cabinet', 'distortion', 'volume', 'lowCut'];

    assert.deepEqual(actual, expected, msg);
    assert.end();
  });

  nest.test('ChannelStrip', assert => {
    const msg = 'instance should inherit from GuitarAmp, BassAmp, and ChannelStrip';
    const myStrip = new ChannelStrip();
    const actual = Object.keys(myStrip);
    const expected = ['cabinet', 'distortion', 'volume', 'lowCut', 'inputLevel'];

    assert.deepEqual(actual, expected, msg);
    assert.end();
  });
});
```

`BassAmp`는 `GuitarAmp`로부터 상속받고 `ChannelStrip`은 `BassAmp`와 `GuitarAmp`로부터 상속을 받는다. 이것이 객체 지향 디자인이 어떻게 조져지는지에 대한 예이다. 채널 스트립은 기타 앰프의 타입도 아니고 캐비넷도 필요로 하지 않는다. 좋은 옵션은 새 베이스 클래스를 만드는 것이다. 좀더 나은 아래 상황을 봐보자.

```javascript
// Composition Example

// http://codepen.io/ericelliott/pen/XXzadQ?editors=001
// https://gist.github.com/ericelliott/fed0fd7a0d3388b06402

const distortion = { distortion: 1 };
const volume = { volume: 1 };
const cabinet = { cabinet: 'maple' };
const lowCut = { lowCut: 1 };
const inputLevel = { inputLevel: 1 };

const GuitarAmp = (options) => {
  return Object.assign({}, distortion, volume, cabinet, options);
};

const BassAmp = (options) => {
  return Object.assign({}, lowCut, volume, cabinet, options);
};

const ChannelStrip = (options) => {
  return Object.assign({}, inputLevel, lowCut, volume, options);
};


test('GuitarAmp', assert => {
  const msg = 'should have distortion, volume, and cabinet';
  const level = 2;
  const cabinet = 'vintage';

  const actual = GuitarAmp({
    distortion: level,
    volume: level,
    cabinet
  });
  const expected = {
    distortion: level,
    volume: level,
    cabinet
  };

  assert.deepEqual(actual, expected, msg);
  assert.end();
});

test('BassAmp', assert => {
  const msg = 'should have volume, lowCut, and cabinet';
  const level = 2;
  const cabinet = 'vintage';

  const actual = BassAmp({
    lowCut: level,
    volume: level,
    cabinet
  });
  const expected = {
    lowCut: level,
    volume: level,
    cabinet
  };

  assert.deepEqual(actual, expected, msg);
  assert.end();
});

test('ChannelStrip', assert => {
  const msg = 'should have inputLevel, lowCut, and volume';
  const level = 2;

  const actual = ChannelStrip({
    inputLevel: level,
    lowCut: level,
    volume: level
  });
  const expected = {
    inputLevel: level,
    lowCut: level,
    volume: level
  };

  assert.deepEqual(actual, expected, msg);
  assert.end();
});
```

주의깊게 보면 당신은 우리가 속성과 객체들을 컴포지션으로 특정화 시켰다는 것을 볼 수 있다. 당신이 클래스로부터 상속할 때 당신은 모든 것을 받을 것이다. 당신이 원하지 않는 것도. 이 관점에서 당신은 아마 생각할 것이다. '괜찮은 거 같아. 근데 저것들의 프로토타입은 어디지?' 이것을 이해하기 위해 당신은 3가지 다른 prototypal 객체 지향을 알아야 한다

- Concatenative 상속

  오브젝트 요소 소스를 복사하는 것으로 또다른 객체와 한 객체에서 직접적으로 상속받는 프로세스이다. 자바스크립트에서 프로토타입의 소스는 일반적으로 믹스인으로 참조된다. `Object.assign()` 으로 불리는 자바스크립트에서 편리한 방식이 있다.

- 프로토타입 delegation

  자바스크립트에서 객체는 delegation를 이용해 프로토타입은 연결되어 있다. 요소가 객체에서 발견되지 않는다면, delegate 프로토타입을 바라본다. 계속해서 연쇄적으로 보며 최종적으로는 `Object.prototype`까지 바라보게 된다. 이것이 루트 delegate이다. `Constructor.prototype`과 `new` 상속을 이용해 훅업을 걸 수 있다. 당신은 또한 `Object.create()`를 이런 목적을 위해 이용할 수도 있고 여러 프로토 타입을 섞고 확장할 수도 있다.

- 함수적 상속

  자바스크립트에서 어떤 함수는 객체를 만든다. 팜수가 `contructor`나 `class`가 아닐 때 우리는 이것을 팩토리 함수라고 부른다. 함수적 상속은 팩토리로부터 객체를 제공하는 것으로 작동하고 생성된 객체를 직접 할당하여 확장합니다 

당신은 깨닫기 시작했을 갓이다, concatenative 상속은 자바스크립트에서 객체 컴포지션의 소스를 가릴 수 있다. 당신은 이제 다른 사람들이 실수하는 것을 볼 수 있따. delegate 프로토타입은 좋은 대체제가 아니다 객체 컴포지션이 좋은 대체제이다

## 구성이 취약한 기지 등급 문제에 면역이 되는 이유

깨지기 쉬운 기반 클래스 문제를 이해하기 위해 컴포지션이 추가하지 않는지 왜 일어나는지 알아보자

1. A is the base class
2. B inherits from A
3. C inherits from B
4. D inherits from B

C 는 B를 상속받기 위해 super을 호출하고 B는 A를 상속받기 위해 super를 호출한다

A와 B는 C와 D가 필요한 것들을 포함시키고 있어야 한다. D는 새로운 유스케이스이고 A의 몇 기능들을 C가 원하는 것보다 더 원한다. 그래서 신입 개발자는 A코드를 수정하기 시작한다. 조짐의 시작이다. C는 이 행동에 의해 부셔질 것이고, D는 일하기 시작할 것이다

### with composition

상상해봐라 클래스 대신에 피쳐들로만 이루어진 것들을

```pseudocode
feat1, feat2, feat3, feat4
```

C가 1과3을 원하고 D가 1,2,3를 원한다고 해보자

```javascript
const C = compose(feat1,feat3);
const D = compose(feat1,feat2,feat4);
```

자 이제 생각해보자. D는 feat1을 약간 수정한 것을 원한다. feat1을 고치면 C가 고장나는 것을 이제는 당연하게 안다. 그렇다 커스터마이즈한 버전을 만들자. 그리고 아래와 같이 진행하면 될 것이다

```javascript
const D = compose(custom1, feat2, feat4);
```

C는 전혀 영향받지 않는다.

클래식한 상속은 이러한 것을 하지 못한다. 전부 분류하려고 노력을 해야한다.

### 당신은 당신이 프로토타입을 안다고 생각하겠지만....

아직 다양하게 더 있다 계쏙해서 공부하고 고민하고 할 수 있도록 하자!

