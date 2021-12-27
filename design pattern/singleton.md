# Singleton Pattern

> 어플리케이션을 관통하는 단 하나의 공통 글로벌 인스턴스

글로벌에서 접근 가능한 공용 객체는 단 하나뿐인 패턴이다.

```typescript
let hiText = "hi";
class HiTextClass {
  getInstance() {
    return hiText;
  }
  changeText(text: string) {
    hiText = text;
    return text;
  }
}
const firstText = new HiTextClass();
const secondText = new HiTextClass();
firstText.changeText("lol");
console.log(firstText.getInstance()); // lol
console.log(secondText.getInstance()); // lol
```

전체 시스템에서 하나의 인스턴스만 존재하도록 보장하는 패턴으로 모두 같은 인스턴스 하나만을 공유한다

객체를 많이 만드는 것을 방지하는 것은 간단하다.

```typescript
let instance;
let hiText = "hi";
class HiTextClass {
  constructor() {
    if (instance) {
      throw new Error("객체는 하나만!");
    }
    instance = this;
  }
  getInstance() {
    return hiText;
  }
  changeText(text: string) {
    hiText = text;
    return text;
  }
}
const firstText = new HiTextClass(); // 이제 이걸 같이 사용하면 된다
const secondText = new HiTextClass(); // (객체는 하나만) 에러 반환
```

모듈화를 간단하게 진행해볼 수도 있다

```typescript
let instance;
let hiText = "hi";
class HiTextClass {
  constructor() {
    if (instance) {
      throw new Error("객체는 하나만!");
    }
    instance = this;
  }
  getInstance() {
    return hiText;
  }
  changeText(text: string) {
    hiText = text;
    return text;
  }
}
const firstText = new HiTextClass();

Object.freeze(HiTextClass);
export { HiTextClass };
```

테스트 코드는 약간 트리키하게 작업해야 한다. 우리는 글로벌 상태로 하나를 공유하기 때문에 전의 상황을 기억해서 짜야한다

```typescript
import HiTextClass from "../src/HiTextClass";

test('change text to "hey"', () => {
  HiTextClass.changeText("hey");
  expect(HitextClass.getInstance()).toBe("hey");
});

test('before text is "hey"', () => {
  expect(HitextClass.getInstance()).toBe("hey");
});
```

## 특징

- 객체 자체에는 접근이 불가능해야함
- 객체에 대한 접근자를 사용해 실제 객체를 제어
- 객체는 `단 하나`만 만든다

## 단점

- OOP언어에서 보통은 JS처럼 객체를 직접 생성하는 것은 힘들다
- JS가 아닌 곳에서는 구현에 많은 신경을 써야 한다
