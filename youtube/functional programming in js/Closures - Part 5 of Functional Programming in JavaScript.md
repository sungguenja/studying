# Closures - Part 5 of Functional Programming in JavaScript

간단한 예제를 한번 보고 가자

```javascript
var me = "Bruce Wayne";
function greetMe() {
    console.log("Hello, " + me + "!");
}
greetMe();
```

일반적인 언어라면 사실 에러가 나야한다. 하지만 자바스크립트는 함수 내에서 아무런 제한 조건 없이 me에 접근할 수가 있다. 그런데 또 특이한 점이 있다. 부르는 시점에서의 변수에 접근이 가능하다는 것이다. 즉, 아래의 경우에는 값이 다르다는 소리이다

```javascript
var me = "Bruce Wayne";
function greetMe() {
    console.log("Hello, " + me + "!");
}
me = "batman";
greetMe();
```

이런 상황을 막기위해 또는 정보의 은닉을 위해 클로저를 이용할 수가 있다

```javascript
function setRequest() {
    var requestId = '1234';
    return function () {
        alert(requestId);
    }
}
```

위의 상황을 정의하고 어떤 변수를 return되는 함수를 할당해주면 쉽게 requestId에 접근은 가능하지만 수정은 못한다!

