# 잃어버린 개발자의 시간을 찾아서: 매일 하루를 아끼는 DevOps 이야기

[영상 링크](https://www.youtube.com/watch?v=2IE68SDTYvI)

## 서버사이드의 문제

- 빌드와 배포 시간 증가
- 모니터링 및 유지 보수 비용증가
- 필요한 컴퓨팅 리소스 증가

## 웹 서비스의 빌드와 배포에 중심적으로 생각해보는 시간을 가져보자

> 1분만에 배포되는 SSR 서비스를 위해서

- 일반적인 배포 스토리
  - git push => 빌드 준비 => 서비스 빌드 => SSR 서버 실행 => 사용자
    - 빌드에 70초 SSR 서버 실행에 60초가 걸리던걸 각각 **6~7초, 20초**로 줄였다

# 빌드 준비 줄여보기

## 레포지토리 복제와 의존성 설치 최적화하기

- 빌드 준비
  - 토스 프론트엔드는 모노레포로 존재한다
  - 서비스가 많다
    - 그로 인해서 많은 의존성 & 많은 소스 코드가 존재
  - npm install의 문제
    - 수백만~수천만 JS 파일
    - 수 GB 용량
    - I/O 성능 저하
    - 캐싱에 불리
  - Yarn Berry
    - 적은 파일 숫자
    - 캐싱 용이
    - 레포지토리 복제만으로 의존성 설치 완료
  - 레포지토리 복제: Git Clone
    - 일반적으로 이렇게 진행한다
    - 모든 파일, 커밋을 다운 받는 과정을 거친다
    - 엄청난 비효율성이 진행된다
  - 원하는 파일만 내려받기
    - Shallow Clone
      - Git Clone의 shallow 옵션으로 편하게 이용가능
      - 하지만 문제 점이 있긴 하다
    - 수정사항은 모두 존재하지만 파일은 최신으로 받는다
      - Git Filter Spec을 이용하자

## Git

- Git = Key-value 스토어
- 모든 커밋, 파일 및 디렉토리는 해시 값 가짐
- 파일 = blob, 디렉토리 = tree

```bash
git clone --filter=<giler-spec>
```

내려 받을 파일(blob)의 조건을 filter-spec으로 지정할 수 있음

```bash
git clone --filter=blob:none
```

처음에 clone을 할 때는 파일 다운 없이 git 객체만 다운로드 받는다. 그 이후 **내려받지 않은 파일은 브랜치 전환 시 필요하면 다운로드 됨**

## Daily Docker Base Image

- 미리 복제된 toss-frontend 레포지토리
- 변경된 일부분 파일만 내려받기

```yml
executors:
  toss_frontend_executor:
    docker:
      - imageL toss-frontend-ci:2022-02-02
```

# SSR 서버 실행 최적화

## SSR 서버 실행 과정

- 스토리
  - CI 빌드 서버 => 도커 이미지 저장소 => Kubernetes 클러스터
    - 이 경우: 도커 이미지를 올리고 내려받는 네트워크 시간이 병목
    - 도커 이미지는 레이어링 된다
    - ![](/docker.PNG)
    - 바뀌는 레이어를 최대한 작게 유지하자
      - 서비스마다 다른 레이어를 최대한 줄여야한다!
      - 토스에서는 최소한의 JS 실행 파일을 올린다
        - 제일 기초 index에서 시작해서 연결되어 쌓이는 파일들이 무엇인지 파악하면 된다.
        - Node File Trace를 이용해보자

### 또다른 키워드들

- Yarn dedupe
- ESBuild
- SWC
- CircleCI
- parallelism
- continuation
- dynamic configuration
