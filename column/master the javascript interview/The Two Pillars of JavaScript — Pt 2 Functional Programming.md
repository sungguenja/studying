# The Two Pillars of JavaScript — Pt 2: Functional Programming

[컬럼 링크](https://medium.com/javascript-scene/the-two-pillars-of-javascript-pt-2-functional-programming-a63aa53a41a4)

> 전 컬럼을 대충 요약해보자
>
> - 자바스크립트는 항상 가장 중요한 프로그래밍언어이고 간단하지는 않다. 그리고 유명세로 인해 프로그래밍의 진화에 있어서 극도로 중요한 두가지 피쳐가 나왔다
>   - 프로토타입적 상속
>   - 함수적 프로그래밍
> - 저자는 이 두가지를 자바스크립트의 두 기둥이록 부르고 싶어한다.

## 우리는 오늘 미래를 만들고 있다.

이노베이션의 연속인 문화로 고 테크적 세상이 세워졌다. 우리는 최첨단을 더욱 더 푸시하는 것은 협업을 필요로 해서 협업하며 대단한 것들을 만들어왔다. 몇 년전에는 우리가 할 수 있을 것이라고 상상도 못했던 것들을 새로운 돌파구는 우리가 할 수 있게 해주었다. 기술의 세계에 온 것을 환영한다

빠르게 변화하는 것 뿐만 아니라, 변화하는 것 자체의 비율 자체가 빠르게 바뀌고 있다. 우리는 기하급수적인 기술적 폭발로 몇 십년에서 기술적 진화를 경험하고 있다. 우리가 5년전에 typical 어플리케이션을 만드는 방법은 오늘날과 아주 달랐다. 당신은 아마 2년전에는 존재하지 않던 툴을 이용할 것이다. 

작년 2년동안 앵귤러를 배웠는가? 그렇다면 당신의 고통을 나는 안다. 배운 많은 것들이 앵귤러 2나 리액트에는 적용시킬 수가 없다. 변화의 비율은 지속가능하지 않다.

만약 길게 엔지니어로 살아남고 싶다면 가장 중요한 것은 우리가 어떻게 적응하고 어떻게 우리의 코드를 좀 더 적응시키도록 만들지를 배우는 것이다.

우리는 빠르게 배워야만 한다, 내년에 우리가 쓸 기술은 지금 쓰는 기술보다는 두배로 복잡할 것이기 때문이다. iot, ai 는 계속 폭발해나가고 있으며 우리의 어플리케이션도 기하급수적으로 성장하고 있다. 내일의 앱은 더욱 크고 상호 운영가능하며 다양한 장점이 오늘것보다 좋을 것이다.

복잡성이 기하급수적으로 증가하는 곳에서 우리가 살아남을 수 있는 유일한 방법은 프로그램의 이해가능한 복잡도를 낮추는 것이다. 내일의 골리앗 앱을 유지하기 위해서 우리는 표현력있는 코드를 만드는 것이다. 우리는 다양한 이유에 대해서 이해하기 쉬운 코드를 짜는 것을 배워야만 한다.

몇년이 지나가면서 우리의 코드 짜는 방식은 지난 30년간 지속해온 방향과 근본적으로 다른 방향으로 우리를 밀어버리는 급진적인 방식으로 바뀌었다. 이러한 변화들은 프로그래밍 기술, 프로세스, 어플리케이션 스케일, 제어의 질 같은 것에 중요한 돌파구를 이끌었다.

객체 처럼 클로저는 상태를 가져가는 매커니즘이다. 자바스크립트에서 클로저는 함수 스코프 안에 정의된 변수에 접근하기 위해 만들어졌다. 클로저를 만드는 것은 쉽다. 간단히 함수를 또다른 함수 안에서 정의 하면 된다. 그리고 안의 함수를 expose하면 된다. 간단하게 살펴보자

```javascript
var counter = function counter() {
    var count = 0;
    return {
        getCount: function getCount() {
            return count;
        },
        incrementL function increment() {
            count += 1;
        }
    };
};
```

~중략~

몇몇 좋은 유틸리티들도 살펴보자

- List utilities
  - `head()` - get first element
  - `tail()` - get all but first elements
  - `last()` - get last element
  - `length()` - count of elements
- Predicates / comparators
  - `equal()`
  - `greaterThan()`
  - `lessThan()`
- List transformations
  - `map()` - ([x]) => [y] take list x and apply a transformation to each element in tat list, return new list y
  - `reverse()`
- List Reducers / folds
  - `reduce()` - ([x],function[,accumulator]) => apply function to each element and accumulate the results as a single value
  - `any()` - true if any values match predicate
  - `all()` - true if all values match predicate
  - `sum()` - total of all values
  - `product()` - product of all values
  - `maximum()` - highest value
  - `minimum()` - lowest value
  - `concat()` - take a list of lists and return a single, concatenated list in list order
  - `merge()` 0 take a list of lists and return a single, merged list in element order
- Iterators / generators / collectors
  - `sample()` - return current value of continuous input source (temperature, form input, toggle switch state, etc...)
  - `repeat()` - (1) => [1,1,1,1,1,....]
  - `cycle()` / `loop()` - when the end of the list is reached, wrap around to the beginning again.

```javascript
// Using ES6 syntax. () => means function () {}
var foo = [1, 2, 3, 4, 5];
var bar = foo.map( (n) => n + 1 ); // [2, 3, 4, 5, 6]
var baz = bar.filter( (n) => n >=3 && n <=5); // [3,4,5]
var bif = baz.reduce( (n, el) => n + el); // 12
```

