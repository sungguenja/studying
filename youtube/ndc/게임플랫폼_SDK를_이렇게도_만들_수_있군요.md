# 게임플랫폼 SDK를 이렇게도 만들 수 있군요!?

[영상링크](https://www.youtube.com/watch?v=JWdpNK-nTto)

> 1. 게임 플랫폼이 무엇인지 아시나요?
> 2. 고속 개발과 안정성을 동시에 잡은 내장형 Node.js
> 3. 어떻게 만들어져 있을까?
> 4. 라이브에서 사용 된 후기

## 1. 게임플랫폼이 무엇인지 아시나요?

- 인증 시스템 연동
- 결제 시스템 연동
- 사용자 게임 경험
- 커뮤니티 시스템 연동

게임 플랫폼 SDK는 멀티플랫폼이 쉽지 않음. 유니티나 언리얼 등 다양한 엔진을 넘어서 그것이 다같이 돌아가는 시스템이 되어야해서 쉽지 않음.

그래서 편하게 만들려면 유니티나 언리얼 등 각 엔진에 종속되어있는 sdk가 되어야하지만 좋지는 않음

넥슨에서는 TOY SDK Interface라는 공통 인터페이스로 해결

## 2. 고속 개발과 안정성을 함께 잡은 내장형 Node.js

게임 프로세스 내부에 Node.js를 삽입, 게임에서 JS로 구현된 기능을 사용

![](./%EB%82%B4%EC%9E%A5%20sdk%20%EA%B5%AC%EC%A1%B0.PNG)

게임 프로세스와 js 생명주기를 잘 맞춰주긴 해야함

그런데 왜 하필 Nodejs?

- 폭넓은 지원환경
- 어마어마한 npm 패키지들
- 많은 개발자
- wasm, n-api 라이러리호출
- 가벼움
- 모바일, 데스크탑 높은 이식성
- xp도 구동 가능
- 웹브라우저 기본 지원
- v8제외 모든 것을 변경가능
- 충분한 성능
- 생산성과 안정성 부분
  - 130만에 달하는 어마어마한 양의 오픈소스
  - 1주안에 프로토타입부터 라이브qa까지 가능한 고도의 생산성
  - 개발자도 많고 서버에서도 10년 이상 사용된 검증된 언어
- JS 특유의 낮은 진입장벽

사내 npm으로 빠른 개발 후 공유하는 방식을 진행

## 3. 어떻게 만들어져 있을까?

게임 <- 브릿지 -> Node.js <- N-API, WASM -> C++ 모듈

게임 (C Interface) <- IPC -> Node.js(JS Interface)

IPC 파이프 형태로 서버 클라이언트 형태의 json 패킷으로 통신하도록 수정, IPC로 작업하여 1:1 통신 뿐 만 아니라 사전 승인된 외부 프로세스 모듈도 SDK 생태계에 합류 가능

> RUST를 통해 C++로 놓치기 쉬운 메모리/스레드 접근 안정성을 개발 환경 차원에서 확보
>
> 대충 돌아가게만 만들면 RUST 컴파일러가 그렇게 만들면 안된다고 알려줌
> 이렇게 까지 해야하나 싶을 정도로 성능\_안정성에 최우선으로 두어 다행히도 배포 후 메모리/스레드 문제가 단 한번도 문제를 일으키지 않았습니다.
>
> 넥슨에서는 러스트를 좋게 본다

## 4. 라이브에서 사용된 후기

1. JS/TS 개발자가 바로 투입되어서 개발 가능해요
2. 인증-결제 모듈도 만들어봤는데 정말 잘 구동됩니다
3. 호환성이 엄청 좋습니다
4. 레퍼런스도 엄청 많습니다
5. SDK 개발기간이 매우 단축되었습니다
6. 신규 게임 엔진과 게임에 연동하는 시간이 1주일 안에 완료된 적도 있습니다.

생각보다 문제가 없던 점

1. Node.js가 구동되지 않는 경우가 없었다
2. 예기치 못한 메모리 문제는 없다!
3. C++ SDK를 JS로 재구현할 필요도 없었다! 그냥 호출해라!
4. ios, aos, arm9, x86 mobile 등 노드는 다 구현체가 있다!
