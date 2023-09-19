# 프라미스와 async, await

## 콜백

```javascript
function loadScript(src) {
  // <script> 태그를 만들고 페이지에 태그를 추가합니다.
  // 태그가 페이지에 추가되면 src에 있는 스크립트를 로딩하고 실행합니다.
  let script = document.createElement("script");
  script.src = src;
  document.head.append(script);
}
```

위 함수는 실행시켜도 스크립트의 로딩이 끝나는 것을 기다리지 않는다

```javascript
loadScript("/my/script.js"); // script.js엔 "function newFunction() {…}"이 있습니다.

newFunction(); // 함수가 존재하지 않는다는 에러가 발생합니다!
```

안전하게 실행시키는 방식으로 콜백을 이용하는 방법이 있다.

```javascript
function loadScript(src, callback) {
  let script = document.createElement("script");
  script.src = src;

  script.onload = () => callback(script);

  document.head.append(script);
}

loadScript(
  "https://cdnjs.cloudflare.com/ajax/libs/lodash.js/3.2.0/lodash.js",
  (script) => {
    alert(`${script.src}가 로드되었습니다.`);
    alert(_); // 스크립트에 정의된 함수
  }
);
```

에러 핸들링도 내부에서 정의 가능하다

```javascript
function loadScript(src, callback) {
  let script = document.createElement("script");
  script.src = src;

  script.onload = () => callback(null, script);
  script.onerror = () =>
    callback(new Error(`${src}를 불러오는 도중에 에러가 발생했습니다.`));

  document.head.append(script);
}
```

콜백은 너무 넣으려고 하면 안되고 안에서 처리하는 방식도 복잡하게 하려면 너무 복잡해진다

## 프라미스

프라미스는 콜백보다 괜찮아보입니다

```javascript
/**
 * @param function 콜백입니다. function의 parameter는 아래와 같습니다
 * @param resolve(value) 성공적일 때 해당 함수를 value와 함께 호출합니다
 * @param reject(error) 에러 발생시 에러 객체를 나타내느 error와 함께 호출
 */
let promise = new Promise(function (resolve, reject) {
  // executor (제작 코드, '가수')
});

// 예시
let promise = new Promise(function (resolve, reject) {
  // 프라미스가 만들어지면 executor 함수는 자동으로 실행됩니다.

  // 1초 뒤에 일이 성공적으로 끝났다는 신호가 전달되면서 result는 '완료'가 됩니다.
  setTimeout(() => resolve("완료"), 1000);
  // 1초 뒤에 에러와 함께 실행이 종료되었다는 신호를 보냅니다.
  setTimeout(() => reject(new Error("에러 발생!")), 1000);
});
```

프라미스는 성공하거나 실패하거나 하나의 결과만이 호출됩니다.

프라미스 성공 또는 실패 후를 다루기 위해 then, catch, finally를 알아봅시다

```javascript
let promise = new Promise(function (resolve, reject) {
  setTimeout(() => resolve("완료!"), 1000);
});

// resolve 함수는 .then의 첫 번째 함수(인수)를 실행합니다.
promise.then(
  (result) => alert(result), // 1초 후 "완료!"를 출력
  (error) => alert(error) // 실행되지 않음
);

// then을 성공으로만 다루고 싶다면 catch를 이용해볼 수도 있습니다
promise.then(alert).catch(alert); // 성공할때는 then으로 에러가 나타나면 catch로 이동됩니다
// finally는 try catch때 처럼 결론적으로 실행하게 만들 수 있습니다
```

## 프라미스 체이닝

> 전 챕터에서 설명했듯이 then, catch, finally를 연속으로 쓸 수 있다
>
> 추가로 then 만 또는 각자 다 연속으로 써내려가는 것도 가능하다

```javascript
new Promise(function (resolve, reject) {
  setTimeout(() => resolve(1), 1000); // (*)
})
  .then(function (result) {
    // (**)

    alert(result); // 1
    return result * 2;
  })
  .then(function (result) {
    // (***)

    alert(result); // 2
    return result * 2;
  })
  .then(function (result) {
    alert(result); // 4
    return result * 2;
  });
```
