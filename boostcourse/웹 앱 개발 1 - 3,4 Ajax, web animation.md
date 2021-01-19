# 웹 앱 개발 1/4

> 1. JavaScript 배열 - FE
> 2. DOM API 활용 - FE
> 3. Ajax - FE
> 4. Web Animation - FE
> 5. WEB UI - FE
> 6. Tab UI - FE
> 7. Spring Core - BE
> 8. Spring JDBC - BE
> 9. Spring MVC - BE
> 10. 레이어드 아키텍처 - BE
> 11. Controller - BE

# Ajax

```javascript
var oReq = new XMLHttpRequest()
oReq.addEventListener('load', function() {
    console.log(this.responseText)
})
oReq.open("GET","json.txt")
oReq.send()

// json 파싱을 원하면
var 원하는변수명 = JSON.parse("서버에서 받은 문자열")
```

[매일봐도 부족함이 없는 영상](https://youtu.be/8aGhZQkoFbQ)

[디버깅은 구글 디벨로퍼를 이용하며 해보자](https://developers.google.com/web/tools/chrome-devtools/?hl=ko#network)



# Web animation

[setinterval](https://javascript.info/settimeout-setinterval)

### setinterval

```javascript
const interval = window.setInterval(()=> {
  console.log('현재시각은', new Date());
},1000/60);

window.clearInterval(interval);
```

주기적으로 함수를 실행하게 하지만 실행을 보장은 못한다. 이벤트 콜백을 생각하면 일어나야할 시간에 어떤 함수가 진행중이라면 이 함수가끝날때까지 기다리게 된다. 즉, 잘못하면 애니메이션이 끊길 수도 있다

![](16.png)

그러면 이런걸 어떻게 해결해야하는가

## setTimeout

애니메이션을 구현하려면 재귀호출을 하면 된다! 아래와 같은 방식을 생각하면 된다!

```javascript
let count = 0;
function animate() {   
  setTimeout(() => {
    if(count >= 20) return;
    console.log('현재시각은', new Date());
    count++;
    animate();
  },500);
}
animate();
```

## requestAnimationFrame

[공식문서](https://developer.mozilla.org/en-US/docs/Web/API/window/requestAnimationFrame)

```html
<html>
    <header>
        <style>
            .outside {
                position: relative;
                background-color: blueviolet;
                width: 100px;
                font-size: 0.8em;
                color: #ffffff;
            }
        </style>
    </header>
    <body>
        <div class="outside">
            제가 좋아하는 과일은요....
        </div>
    </body>
</html>
```

```javascript
// 개발자 도구에서 실행시키든지 임포트하든지
var count = 0
var el = document.querySelector(".outside")
el.style.left = "0px"
function run() {
    if(count > 50) return
    count = count + 5
    el.style.left = parseInt(el.style.left) + count + "px" // el.style.left는 처음 정의처럼 string이다
    requestAnimationFrame(run)
}

requestAnimationFrame(run)
```

> 주의점!
>
> requestAnimationFrame을 여러번 호출하면 등록한 순서대로 번갈아가며 반복하게 됩니다. 
>
> run1, run2, run3 순서로 등록했으면
>
> run1이 return 할때까지 run1만 돌고 run2가 시작되는게 아니라
>
> run1 -> run2 -> run3 -> run1 -> ... 이렇게 한번씩 번갈아가면서 실행됩니다.

## CSS로 애니메이션 구현

[하드웨어 가속?](https://d2.naver.com/helloworld/2061385)

[트랜지션 가이드](https://thoughtbot.com/blog/transitions-and-transforms)

```html
<html>
    <header>
        <style>
            .outside {
                position: relative;
                background-color: blueviolet;
                width: 100px;
                font-size: 0.8em;
                color: #ffffff;
                left:"0px";
                transform: scale(1);
                transition: all 2s;
            }
        </style>
    </header>
    <body>
        <div class="outside">
            제가 좋아하는 과일은요....
        </div>
    </body>
</html>
```

이렇게 transition 속성을 준 상태에서 자바스크립트로 이벤트를 줘서 변화시키거나 하면 속성에 따라 2s동안 그 변화를 진행한다. all을 수정해서 측정변화만 가능

즉, 자바스크립트로는 이벤트로 변화하는 정도를 css로는 그 변화 사이 중간을 제어한다고 생각하면 편할 것 같다. 단 자바스크립트에서 style속성을 가져올려고 하면 태그안에 직접 style을 넣는 경우도 있다 조심할것!

[벤더 프리픽스란? 한글](https://sapjil.net/vender-prefix/)

[벤더 프리픽스 공식문서](https://developer.mozilla.org/en-US/docs/Glossary/Vendor_Prefix)