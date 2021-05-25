# ES6~ES11

- shorthand property names

  [참고 자료](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Operators/Object_initializer)

  ```javascript
  const name = "ellie";
  const age = 18;
  
  const ellie_obj = {
      name: name,
      age: age,
  }
  
  const ellie_obj2 = {
      name,
      age
  }
  ```

  이렇게 줄여서 하는것도 가능하다

- Destructuring assignment

  파이썬처럼 값을 줄 수 있는 방식

  [참고자료](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Operators/Object_initializer)

- Spread Syntax

  [참고 자료](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Operators/Spread_syntax)

  ```javascript
  {
      const obj1 = {key:'key1'};
      const obj2 = {key:'key2'};
      const array = [obj1,obj2];
      
      const array_copy = [...array];
  }
  ```

  위 문제는 두 array가 같은 object를 본다는 것이다. `deepcopy`가 아니니 조심하자!

  이것의 재미있는 점은 object에서도 같은 방식으로 통한다. 같은 key가 존재하면 나중에 들어간 value가 들어가니 이 점 유의

- Ternary Operator

  간단한 if문은 한줄로 쓰자

  ```javascript
  const component = iscat ? 'cat' : 'dog';
  ```

- Template Literals

  object에 해당 key값이 존재하지 않을때 쓰는 방식

  ```javascript
  // 억지로 구현할 시에
  function printManager(person) {
      console.log(person.job && person.job.manager && person.job.manager.name)
  }
  
  // template literals
  function printManager(person) {
      console.log(person.job && .manager && .name)
  }
  ```

  

