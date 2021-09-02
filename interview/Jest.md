# Jest

설치: `nom install jest -D` (보통은 개발중에만 사용하니 꼭 디벨롭 모드로 설치하자)

scripts에 test: jest를 추가해주면 쉽게 테스트가 가능해진다.

## 테스트 코드들은 모듈.test.js 또는 __test__ 폴더에 넣어서 작성하자

- text("설명", () => {expect(함수()}.toBe(기대값)) 형태로 작성
  - 아닌것을 원하면 expect.not.toBe형식으로 작성하면 된다.
  - toBe는 기본값 비교시 이용한다
  - toEqual과 무슨 차이인가?
    - 객체 (당연하지만 배열 포함)은 toBe로 체크를 못한다
    - toEqual을 이용해야 비교가 가능해진다.
    - 하지만 깊은 비교를 하고 싶다면 toStrictEqual을 이용해야 한다
      - 또 둘의 차이는?
      - toStrictEqual은 엄격하다. 하지만 toEqual은 덜 엄격한데 이것의 경우 객체로 치면 비교할 객체에 원하는것의 속성만 있으면 통과하지만 strict는 속성이 더 있으면 통과하지 못하게 한다
  - toBeNull, toBeFalsy, toBeTruthly
    - null인가를 보는 매쳐, false인가를 보는 매쳐, true인가를 보는 매쳐
  - toBeGreaterThan, toBeGreaterThanOrEqual, toBeLessThan, toBeLessThanOrEqual
    - 머 읽는것처럼이다
  - toBeCloseTo 
    - 근사값인지 비교
  - toMatch
    - 정규표현식으로 넣어줘서 비교할 스트링에 해당 정규 표현식이 존재하는지 확인하는 것
  - toContain
    - 배열에 해당 값이 있는지 판별
  - toThrow
    - 해당 에러를 반환하는지

## 비동기 코드 테스트는 어떻게 하지?

- done이라는 콜백을 전달해주면 된다
  - test('설명',(done) => {expect.toBe; done(); }) 이런식의 콜백을 전달하면 된다.
- promise의 경우에는 .then안에서 expect를 이용하면 된다. return 만 잘 해주면 된다.
- async/await의 경우에는 await로 받은 값을 그냥 비교하면 된다

## 테스트 전후에 로직이 필요한데?

- jest는 그 지점에서 다양한 것을 제공한다
  - beforeeach
    - 각 테스트가 실행되기 전에 로직을 실행, 내부에서 await이용 가능
  - aftereach
    - 각 테스트가 실행된 후에 해당 로직을 실행, 내부에서 await이용 가능
  - beforeAll, afterAll
    - 각 테스트 전체 실행 전, 실행 후 에 대해 필요한 로직 실행시켜줌
  - describe
    - 비슷한 작업을 한 곳에 묶어서 설명하기 위해 사용
  - test.only
    - 해당 테스트 코드만 실행시키도록 한다.
  - test.skip
    - 해당 테스트를 스킵한다

## 목 함수 ~~(목진화)~~

- jest.fn으로 호출할 수 있다
- 그리고 내부의 calls를 이용하여 해당 함수가 몇번 호출되었고 뭐가 input되었는지 알 수 있다
- result로 결과값을 볼 수도 있다.
- 데이터베이스 변환이나 여러 번거로운 것들을 테스트해야하는 경우, 이것을 잘 이용하여 해결하면 된다.
- 원래 테스트할 함수에 mockReturnValue메서드를 붙이는 경우 함수는 실행되지 않지만 테스트할 객체는 우리가 만들 수 있다

## 리액트 컴포넌트와 함께 테스팅도 가능하다

- 포함되어있는 리액트 테스트 라이브러리를 이용하면 된다.
- render, screen을 보통 이용하는 편이다.

