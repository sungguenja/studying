# Object

- 생성 방법

  ```javascript
  const obj1 = {}; // object literal
  const obj2 = new Object(); // object constructor
  function makeObject(name,age) {
      return {
          name,
          age,
      };
  }
  const obj3 = makeObject();
  ```

- 뒤늦게 추가,삭제하는 것도 쉽게 가능하다

  ```javascript
  const eliie = {name: 'eliie', age:4};
  ellie.hasJob = true; // 에러가 일어나지 않는다!
  delete eliie.hasJob;
  console.log(ellie.hasJob); // undefined
  ```

- `.`을 이용해 접근 하는 것도 가능하고 파이썬 처럼 `[]`으로 접근도 가능하다

  ```javascript
  console.log(eliie.name);
  console.log(eliie['name']);
  ```

- `in` 연산자로 해당 key가 object안에 있는지 확인 할 수가 있다

  ```javascript
  console.log('name' in eliie); // true
  console.log('asdf' in eliie); // false
  ```

- `for`연산으로 key값 순환도 가능

  ```javascript
  for (key in eliie) {
      console.log(key,eliie[key]);
  }
  ```

- 복사는 언제나 그렇듯 조금 귀찮다

  ```javascript
  // old way
  const user3 = {};
  for (key in eliie) {
      user3[key] = eliie[key];
  }
  
  // other way
  const user4 = {};
  Object.assign(user4,eliie);
  
  // other way
  const user5 = Object.assign({},eliie);
  ```

  