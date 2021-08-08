# Master the JavaScript Interview: What is Function Composition?

[컬럼 링크](https://medium.com/javascript-scene/master-the-javascript-interview-what-is-function-composition-20dfb109a1a0)

함수 컴포지션은 새 함수를 프로듀스 하기 위해 둘 또는 그 이상의 함수를 엮는 과정이다. 함수를 함께 컴포징 하는 것은 데이터가 흐를 수 있도록 일련의 파이프를 스냅핑하는 것과 같다.

수학에서 `f`,`g`함수를 섞는 것은 간단하게 `f(g(x))`이다. 코드적으로 한번 다가가보자. 유저 풀 네임을 url로 컨버팅하고 그걸로 프로필 페이지를 얻는 것을 생각해보자. 아래와 같은 흐름을 가질 것이다

1. split the name into an array on spaces
2. map the name to lower case
3. join with dashes
4. encode the URI component

```javascript
const toSlug = input => encodeURIComponent(
  input.split(' ')
    .map(str => str.toLowerCase())
    .join('-')
);
```

흐음 나쁘진 않은거 같다? 좀 더 가독성을 높이고 싶긴 하다.

```javascript
const toSlug = input => encodeURIComponent(
  join('-')(
    map(toLowerCase)(
      split(' ')(
        input
      )
    )
  )
);

console.log(toSlug('JS Cheerleader')); // 'js-cheerleader'
```

위와 같이 수정을 해보자. 아이디어는 좋았지만 오히려 전보다 더 읽기 힘들어졌다. 엮을 수 있는 형태의 `split()`, `join()`, `map()`을 만들고 엮어보자! 아래와 같이 한번 해보자

```javascript
const curry = fn => (...args) => fn.bind(null, ...args);

const map = curry((fn, arr) => arr.map(fn));

const join = curry((str, arr) => arr.join(str));

const toLowerCase = str => str.toLowerCase();

const split = curry((splitOn, str) => str.split(splitOn));
```

많이 좋아진 거 같다. 이 상태는 심지어 각 함수들을 원하는 방식으로 재사용할 수도 있다. 모듈화도 가능할 것이다! 여기서 커리는 기술적으로 진짜 커리가 아니다. 대신 간단한 부분적 어플리케이션이 되었다. 하지만 설명에 목적이 있다고 생각하면 아직 코드는 조금 더 읽기 좋아져야 할 거 같다.

이 전 코드로 다시 돌아가보자. 여기에는 너무 많이 엮이고 들여쓰기가 들어가며 읽기에 혼돈을 준다. 우리는 괄호안에 쓰는 것을 조금은 그만두어야할 거 같다.

와서 생각좀 해봐라. 우리는 어레이에 대한 몇 특수한 메소드들을 가지고 있다! `reduce()`메소드가 있다. 하지만 `reduce`완전히 적절하지는 않다. 그렇다면 적절한 reduce같은 것을 만들어보자

```javascript
const compose = (...fns) => x => fns.reduceRight((v,f) => f(v),x)
```

reduceRight는 이미 있는 메소드고 그걸 이용해서 괜찮은 함수로 만들었다! 그렇다면 `toSlug`함수는 아래와 같이 수정이 가능할 것이다.

```javascript
const toSlug = compose(
	encodeURIComponent,
    join('-'),
    map(toLowerCase),
    split(' ')
);

console.log(toSlug('JS Cheerleader')); // js-cheerleader
```

이것이 글쓴이 입장에서는 읽기 더 좋다

하드코어 함수형 프로그래밍은 그들의 전체 어플리케이션을 정의한다. 나는 빈번이 일시적인 변수를 요구하는 것을 제거하기 위해 사용한다. points-free 스타일은 매우 중요하게 다가올 것이다