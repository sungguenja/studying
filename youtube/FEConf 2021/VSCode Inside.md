# VSCode Inside

[영상 원본](https://www.youtube.com/watch?v=epWQkxwvQ_U)

- VSCode팀은 어떤 방식으로 저작 도구를 설계했을까?
- 구조 형태
  - base
    - VSCode의 코드와 관계없이 어느 앱에서든 활용할 수 있는 Context-free한 코드들
    - Array, Color, Hash, JSON 등 유틸리티 코드
    - Checkbox, List, Grid, Tree 등 특정 App의 Context와 상관없이 사용할 수 있도록 만든 UI 코드
  - platform
    - vscode의 프레임워크
    - Dependency injection등 vs code 코어에 해당
  - editor
    - 코드 에디터에 대한 부분
    - monaco라는 웹 코드 에디터로 제공도 하고 있음
  - workbench
    - 파일탐색창, 탭 등 파트들을 모아놓은 어플리케이션
  - code
    - 부트스트래핑을 담당
- 바닐라 JS로만 작업했다
  - 왜그럴까? (발표자의 주관으로 살펴보자)
    - Imperative Style
    - DOM Friendly
    - lifecycle은 없다!
    - open component

