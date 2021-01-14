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

# WEB UI 개발

## window 객체

window에는 다양한 메서드가 존재하며 이용이 가능하다. window는 default개념에 해당하여 생략가능

```javascript
window.setTimeout()
setTimeout() //window는 전역객체라서 생략 가능하다.
```

## setTimeout 활용

인자로 함수를 받고 있으며, 보통 나중에 실행되는 함수를 **콜백함수**라고도 합니다. 자바스크립트는 함수를 인자로 받을 수 있는 특징이 있다. 반환도 가능!

```javascript
function run() {
    console.log("run start") // 1번째 인쇄
    setTimeout(function() {
        var msg = "hello codesquad";
        console.log(msg);  // 3번째 인쇄 이 메시지는 즉시 실행되지 않습니다.
    }, 1000);
    console.log("run end") // 2번째 인쇄
}

run();
```

```javascript
function run() {
    setTimeout(function() {
        var msg = "hello codesquad";
        console.log(msg);  // 3번째 인쇄 이 메시지는 즉시 실행되지 않습니다.
    }, 1000);
}
console.log("run start") // 1번째 인쇄
run();
console.log("run end") // 2번째 인쇄
```

setTimeout은 이벤트루프에 들어간다 이것을 꼭 이해해야한다 웹에이피아이 관련이라

[이벤트 루프 관련 영상 시청하면 도움이 된다](https://www.youtube.com/watch?v=8aGhZQkoFbQ&feature=emb_title)

## DOM과 쿼리셀렉터

브라우저에서는 HTML코드를 DOM(Document Object Model)이라는 객체 형태의 모델로 저장합니다. 그렇게 저장된 정보를 DOM Tree라고 함. 결국 HTML element는 Tree형태로 저장됩니다.

![]()