# DB 연결 웹 앱

> 1. JavaScript - FE
> 2. WEB UI 개발 - FE
> 3. JSP - BE
> 4. redirect & forward - BE
> 5. scope - BE
> 6. JSTL & EL - BE
> 7. MySQL - BE
> 8. SQL - BE
> 9. Maven - BE
> 10. JDBC - BE
> 11. WEB API - BE

# 자바스크립트

## 변수

변수는 var, let, const로 선언할 수 있다. 어떤 것을 사용하는 가에 의해서  scope라는 변수의 유효 범위가 달라진다.

우선 var를 사용해서 변수를 선언한다. 여러가지 변수 선언 방법을 확인해보자.

```javascript
var a = 'i love boostcourse'
console.log(a) // 'i love boostcourse'
a = 'asdf'
console.log(a) // 'asdf'
const myname = a || 'defaultname' // a가 정해져있지 않는다면 오른쪽을 기본값으로 만들어낼 수 있다 or 연산
const data = 11
const result = (data > 10) ? 'ok' : 'fail' ; // 괄호안이 true면 ok false면 fail
```

타입은 선언할 때가 아니라 **실행타임**에 결정된다. 함수안에서의 파라미터나 변수는 실행될 때 그 타입이 결정된다.

타입을 체크하는 또렷한 방법은 없다. 정확하게는 **toString.call**을 이용해서 그 결과를 매칭하고 낳는데, 문자, 숫자와 같은 기본 타입은 typeof 키워드를 사용해서 체크할 수 있다.

배열의 경우 타입을 체크하는 isArray함수가 표준으로 있다.

## 함수

함수는 여러 개의 인자를 받아서, 그 결과를 출력한다. 그러나 인자를 넣지 않으면 undefined라는 값을 가지게 된다.

```javascript
function printName(firstname) {
    var myname = "jisu";
    return myname + " " +  firstname;
}
console.log(printName()); // jisu undefined
console.log(printName('asdf')) // jisu asdf
console.log(printName('asdf','sd')) // jisu asdf
```

### 함수 - 함수표현식

```javascript
function printName(firstname) {
    console.log(inner); // undefined
    var inner = function() {
        return 'inner value'
    }
    console.log(inner); // 함수를 인쇄
}

//////////////////////////////////////////

function printName(firstname) {
    console.log(inner); // 함수를 인쇄
    function inner () {
        return 'inner value'
    }
    console.log(inner); // 함수를 인쇄
}
```

무슨 차이가 있는가? 호이스팅이 생긴다!

위의 식은 var inner; 이것이 호이스팅이 되고 밑의 식은 function inner자체가 위로 호이스팅이 된다

```javascript
// 호이스팅 후
function printName(firstname) {
    var inner;
    console.log(inner); // undefined
    inner = function() {
        return 'inner value'
    }
    console.log(inner); // 함수를 인쇄
}

//////////////////////////////////////////

function printName(firstname) {
    function inner () {
        return 'inner value'
    }
    console.log(inner); // 함수를 인쇄
    console.log(inner); // 함수를 인쇄
}
```

## 함수 - arguments속성

배열 형식으로 접근(`Object`)은 하지만 배열의 메서드는 사용 불가.

```javascript
function a() {
    console.log(arguments); // {'0':1,'1':2,'2':3} for문 가능
}
a(1,2,3);
```

## arrow function

```javascript
function getName(name) {
    return "Kim " + name;
}
// 위와 아래가 같다
var getName = (name) => "Kim " + name;
```

## 함수호출

```javascript
function printName(firstname) {
    var myname = "jisu";
    return myname + " ," +  firstname;
}

function run(firstname) {
   firstname = firstname || "Youn";
   var result = printName(firstname);
   console.log(result);
}
```

함수의 호출은 call stack에 의해서 불린것이 차곡차곡 쌓이고 하나씩 실행된다

[콜스택 엡트루프 등 다양한 자바스크립트 관련](https://medium.com/@gaurav.pandvia/understanding-javascript-function-executions-tasks-event-loop-call-stack-more-part-1-5683dea1f5ec)