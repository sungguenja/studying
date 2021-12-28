# Prototype Pattern

> 같은 타입의 많은 객체에서 요소(properties)를 공유해라

머릿속에서 이미지화 시키고 코드를 보는 것이 가장 이해가 쉬운 패턴이다.

```typescript
class Cat {
  constructor(name) {
    this.name = name;
  }

  meow() {
    return "meow meow";
  }
}

const cat1 = new Cat("nabi");
const cat2 = new Cat("gafield");
const cat3 = new Cat("simba");
```

위와 같이 진행할 경우 `cat1`,`cat2`,`cat3` 의 `__proto__`는 같은 클래스로 되어 있을 것이다.

위와 같이 진행할 경우 새로운 메소드를 넣고 싶다면 두가지 방법이 있다. 위 코드 클래스에서 직접 수정을 하거나 아니면 아래와 같은 방식을 이용하면 된다.

```typescript
class Cat {
  constructor(name) {
    this.name = name;
  }

  meow() {
    return "meow meow";
  }
}

const cat1 = new Cat("nabi");
const cat2 = new Cat("gafield");
const cat3 = new Cat("simba");

Cat.prototype.scratch = () => console.log("cat scratch everything....");
cat3.scratch();
```

아니면 상속을 받는 방법도 있다. 그런데 우리는 이게 완벽한 상속이 아님을 알고 가자. [관련 칼럼](https://medium.com/@limsungmook/%EC%9E%90%EB%B0%94%EC%8A%A4%ED%81%AC%EB%A6%BD%ED%8A%B8%EB%8A%94-%EC%99%9C-%ED%94%84%EB%A1%9C%ED%86%A0%ED%83%80%EC%9E%85%EC%9D%84-%EC%84%A0%ED%83%9D%ED%96%88%EC%9D%84%EA%B9%8C-997f985adb42)

```typescript
class SuperCat extends Cat {
  constructor(name) {
    this.name;
  }

  nyanPunch() {
    console.log("nyan nyan punch");
  }
}

const cat1 = new SuperCat("supeeeeer");
cat1.meow();
cat1.nyanPunch();
```

위와 같이 한다면 `cat1`의 `__proto__`는 `SuperCat`을 `SuperCat`의 `__proto__`는 `Cat`을 보게 될 것이다.

위와 같은 상속의 형태 또는 객체 생성은 `Object.create`를 이용해서도 진행할 수 있다
