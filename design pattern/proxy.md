# Proxy Pattern

[참고 링크](https://ui.toast.com/weekly-pick/ko_20210413)

> 어플리케이션을 관통하는 하나의 글로벌 인스턴스를 공유한다

간단히 대변인에게 일을 대신 시키는 방식이다. 프록시를 이용하여 객체를 생성하는 방식이다. 간단히 살펴보면 아래와 같다

```typescript
const person = {
  name: "name",
  age: 20,
  gender: "male",
};

const personProxy = new Proxy(person, {});
```

하지만 이러면 우리는 값을 수정하거나 얻을 때는 요소에 직접 접근해야한다는 문제점이 생긴다. 그래서 여기서 조금 더 나아가서 getter,setter을 만드는 작업을 해보자

```typescript
const person = {
  name: "name",
  age: 20,
  gender: "male",
};

const personProxy = new Proxy(person, {
  get: (obj, prop) => {
    // 키 값의 유무는 이 패턴을 이용할 때 스스로 넣어볼 수 있도록 하자
    console.log(obj[prop]);
    return obj[prop];
  },
  set: (obj, prop, value) => {
    // 마찬가지로 키의 유무와 타입 검증 로직은 추후에 직접 해보자
    obj[prop] = value;
    return obj[prop];
  },
});
```

## reflect

Proxy를 다룰때 우리는 Reflect도 알면 좋다. 아래와 같이 이용이 가능하다

```typescript
// 1. 에러 핸들링
const obj = {};
try {
  Object.defineProperty(obj, "prop", { value: 1 });
  console.log("success");
} catch (e) {
  console.log(e);
}

const obj2 = {};
if (Reflect.defineProperty(obj2, "prop", { value: 1 })) {
  console.log("success");
} else {
  console.log("problem creating prop");
}
// 2. 더 읽기 쉬운 코드
const obj = { prop: 1 };
console.log(Reflect.has(obj, "prop") === "prop" in obj); // true
```

아래로 바뀌면서 깔끔해 보이는데 이래서 뭐? 어찌되었든 proxy를 쓰고 싶으면 getter, setter를 작성하고 귀찮게 해야하는데? 그래서 reflect에는 해당 메서드가 있다!

```typescript
const person = {
  name: "name",
  age: 20,
  gender: "male",
};

const personProxy = new Proxy(person, {
  get: (obj, prop) => {
    return Reflect.get(obj, prop);
  },
  set: (obj, prop, value) => {
    return Reflect.set(obj, prop, value);
  },
});
```

검증은 알아서 진행해준다! 매우 깔끔하게 진행이 가능하다
