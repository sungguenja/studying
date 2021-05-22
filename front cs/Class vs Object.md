# Class vs Object

## Class

- 붕어빵의 틀이라고 생각해도 된다

- 다른 언어의 클래스처럼 상속과 오버라이딩이 가능하다

- ```javascript
  class Person {
      constructor(name,age) {
          this.name = name;
          this.age = age;
      }
  }
  ```

- Getter,Setter: 좀 더 에러 상황을 피하기 위해 방어적으로 설정하는 것

- ```javascript
  class User {
      constructor(first_name,last_name,age) {
          this.first_name = first_name;
          this.last_name = last_name;
          this.age = age;
      }
      
      get age() {
          return this._age;
      }
      
      set age(value) {
          if (value > 0) {
              this._age = value    
          }
      }
  }
  ```

- public, private field

- ```javascript
  class Experiment {
      publicField = 2;
      #private = 0;
  }
  const asdf = new Experment();
  console.log(asdf.piblicField); // 2
  console.log(asdf.private); // undefined
  ```

  - 클래스 내부에서는 #private로 해둔 변수를 쓸 수 있지만 외부에서는 접근이 불가능하다

- Static

- ```javascript
  class Article {
      constructor(article_number) {
          this.article_number = article_number;
      }
      static publisher = 'DC';
      static pritPublisher() {
          console.log(Article.publisher);
      }
  }
  
  const article = new Article(1);
  console.log(article.publisher); // undefined
  console.log(Article.publisher); // 'DC'
  Article.pritPublisher(); // 'DC'
  ```

- 클래스 내부에 지정되는 변수 또는 함수로 각 객체에서는 접근이 불가능하고 클래스 생성자에서 접근이 가능하다

- 필요한 변수가 있는 데 모든 객체에서 같다면 위와같이 이용해서 메모리를 아낄 수가 있다

- instanceOf

  - 해당 객체가 해당 클래스로 생성된 것인지 알려주는 함수이다
  - 상속된 클래스라면 부모 클래스도 True를 반환한다
  - 따라서 Object에 대해서 이 함수를 이용하면 True가 나온다

## Object

- 틀로 만들어진 붕어빵이라고 생각해도 된다.
- 임의로 만든 것은 체계적이지 않은 상황이라고 생각하는 것이 편하다.
- 아니면 딕셔너리라고 생각하는 것도 괜찮다

