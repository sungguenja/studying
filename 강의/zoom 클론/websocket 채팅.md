# Websocket

> webrtc와 차이점은 서버에서 데이터를 관리할 수 있다는 것이 있다. 그러니 차이점을 인지하고 어떻게 간단히 할 수 있는지 한번 알아보자

```javascript
const socket = new WebSocket("주소");

socket.addEventListener("open", () => {
  console.log("connected to server");
});

socket.addEventListener("message", (message) => {
  console.log(message);
});
// message 객체에 보통 data라는 속성으로 필요한 값이 올것임. 뭐 근데 결국 상황마다 봐야하니 잘 이야기하자

socket.addEventListener("close", () => {
  console.log("disconnected");
});

socket.send("message");
```

위 코드 상황이 기본적인 상황이라고 생각하면 편하다 응용은 간단하게 아래와 같이 할 수 있을 것이다

```javascript
messageForm.addEventListener("submit", (evnt) => {
  event.preventDefault();
  const input = messageForm.querySelector("input");
  socket.send(input.value);
  input.value = "";
});
```
