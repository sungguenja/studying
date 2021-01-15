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

![](7.png)

[위키피디아 DOM 문서](https://en.wikipedia.org/wiki/Document_Object_Model)

## Browser Event, Event Object, Event handler

이벤트 등록은 하던 것처럼 addEventListener가 있다

이벤트 객체는 언제나 주의하자. event.target으로 객체를 가져오는 것은 이벤트가 발생한 객체를 가져오는 것이다

```javascript
var el = document.getElementById("outside");
el.addEventListener("click", function(evt){
 console.log(evt.target); // 이벤트가 발생한 객체를 보여준다
 console.log(evt.target.nodeName);
}, false);
```

[이벤트 소개](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Events#event_handler_properties)

[이벤트 레퍼런스](https://developer.mozilla.org/en-US/docs/Web/Events)

## Ajax

예제코드

```javascript
function ajax(data) {
    var oReq = new XMLHttpRequest();
    oReq.addEventListener('load', function() {
        console.log(this.responseText);
    });
    oReq.open('GET','http://www.example.org/example.txt');
    oReq.send();
}
```

대충 axios써도 되긴 하지만 순수 JS에서는 `XMLHttpRequest` 를 이용하면 된다 어렵지 않다!

## 디버깅

크롬에서도 디버그 모드가 있어서 한줄씩 차근차근 실행이 가능하다

또한 해당 라인에서의 객체들을 모두 인쇄해서 확인을 해볼 수가 있다.

Scope에서도 확인이 가능하다! 크롬을 적극적으로 이용하자