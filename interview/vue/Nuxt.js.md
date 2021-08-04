# Nuxt.js

## Nuxt.js란?

- Vue.js 애플리케이션 개발을 보다 강력하고 사용하기 쉽게 만들어 주는 프레임워크다. 좀 더 빠른 개발 속도를 위해 Vue.js를 빠르게 적용하는 방법을 고안했고, 이를 프레임워크로 만들었다. 목표는 다음과 같다
  - Nuxt.js의 주요 범위는 클라이언트/서버 배포를 추상화 하는 동안의 UI Rendering이다
  - Node.js 기반의 프로젝트 혹은 기본 프로젝트 베이스로 사용할 수 있을 만큼의 유연한 프레임워크를 만드는 것이다.
  - Nuxt.js는 Vue.js 애플리케이션 서버 렌더링을 보다 즐겁게 개발하는데 필요한 구성요소들을 미리 설정한다
  - nuxt generate라고 부르는 배포 옵션을 제공하고 vue.js 애플리케이션을 정적으로 생성 가능
- 특징
  - Vue 파일 사용
  - 코드 분할 자동화
  - 서버 사이드 렌더링
  - 비동기 데이터 기반의 강력한 라우팅 시스템
  - 정적 파일 전송
  - JS & CSS 코드 번들링 및 압축
  - `<head>` 요소 관리
  - 개발 중 Hot module 대체
  - 전 처리기 지원: SASS, LESS, Stylus 등

## Nuxt.js 설치

1. yarn 설치

   ```bash
   npm i -g yarn
   ```

2. 패키지에 Nuxt 스캐폴딩

   ```bash
   yarn create nuxt-app </Directory>
   ```

3. 개발 서버 구동

   ```bash
   yarn dev
   ```

   