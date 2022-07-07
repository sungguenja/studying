# webrtc

## webRtc 이론

[참고 mdn 문서](https://developer.mozilla.org/ko/docs/Web/API/WebRTC_API)

> p2p시스템을 웹으로 구축할 수 있도록 도와줌

- 서버가 필요하기는 하다
  - signaling을 하기 위한 서버가 필요
    - 상대방과 나의 연결점을 찾는 것을 도와줌
  - signaling이 끝나면 p2p로 연결이 된다
- 간단하게는 아래와 같은 프로세스인 것이다
  1. 1번 유저가 서버와 signaling으로 연결가능하게 올려둠
  2. 2번 유저가 1번 유저와 연결하고 싶다고 signaling을 요청
  3. 2번 유저는 서버에게 인증을 받고 1번 유저와 연결할 수 있도록 도움
  4. 1,2번 유저는 서로 연결된다
  5. profit

## user video and other actions

[참고 mdn 문서](https://developer.mozilla.org/ko/docs/Web/API/MediaDevices/getUserMedia)

```javascript
const myFace = document.getElementById("myFace");
const muteBtn = document.getElementById("mute");
const cameraBtn = document.getElementById("camera");

let myStream;
let muted = false;
let cameraOff = false;

async function getMedia() {
  try {
    myStream = await navigator.mediaDevices.getUserMedia({
      audio: true,
      video: true,
    });
    myFace.srcObject = myStream;
  } catch (e) {
    console.log(e);
  }
}

function handleMuteClick() {
  myStream
    .getAudioTracks()
    .forEach((track) => (track.enabled = !track.enabled));
  if (!muted) {
    muteBtn.innerText = "Unmute";
  } else {
    muteBtn.innerText = "mute";
  }
  muted = !muted;
}
function handleCameraClick() {
  myStream
    .getVideoTracks()
    .forEach((track) => (track.enabled = !track.enabled));
  if (!cameraOff) {
    cameraBtn.innerText = "camera off";
  } else {
    cameraBtn.innerText = "camera on";
  }
  cameraOff = !cameraOff;
}

muteBtn.addEventListener("click", handleMuteClick);
cameraBtn.addEventListener("click", handleCameraClick);
```

- 미디어 도구 바꾸는 법
  - 유저가 선택
  - 선택한 미디어의 value를 바꿔주면 된다
  - 그다음 미디어 얻는 함수를 재 실행 (위 예시의 경우에는 getMedia)
  - 그래서 위 순서를 한번에 시키는 방법은 getMedia에 deviceId를 인자로 받는 함수로 만들고 정해주면 될 듯 하다
  - 아마 아래와 같은 흐름으로 진행될 듯 하다. (에러나면 알아서 찾아서 해보자)
  - ```javascript
    let myStream;
    async function getMedia(deviceId) {
      const initialConstraints = {
        audio: true,
        video: { facingMode: "user" },
      };
      const cameraConstraints = {
        audio: true,
        video: { deviceId: { exact: deviceId } },
      };
      try {
        myStream = await navigator.mediaDevices.getUserMedia(deviceId ? cameraConstraints : initialConstrains);
        MyFace.srcObjects = myStream;
      }
    }
    ```
