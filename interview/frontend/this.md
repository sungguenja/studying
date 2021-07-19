# this?

this는 정확히 알아두는 것이 좋다. 보통은 window(global)를 보고 있을 수 있다. 변경되는 경우들을 살펴보자

1. 객체의 메소드에 의해 호출

   ```javascript
   var OBj = {
       name: 'this',
       func: function () {
           console.log(this,this.name);
       }
   }
   
   Obj.func();
   // {name:'this',func:[Function:func]},'this'
   ```

   위의 경우가 가장 알기 쉬운 케이스이다. 해당 객체를 바라보고 있다.

2. 함수 호출

   ```javascript
   var name = 'global_this';
   
   var Obj = {
       name: 'this',
       func1: function() {
           console.log("this is "+ this);
   
           var func2 = function() {
               console.log("this is " + this);
           };
   
           func2();
       }
   };
   Obj.func1();
   // this is [object Object]
   // this is [object global]
   ```

   func1으로 지정된 덩어리 함수는 객체를 바라보게 된다. 하지만 그 안에서 지정된  func2의 경우는 global을 보게 된다.

3. new

   객체를 생성하는 방법중 하나이다. class를 이용해서 만들어도 같음

4. bind,call,apply

   this를 지정해서 묶을 수 있는 메서드들이다

5. 화살표 함수

   상위 스코프에서 가져온다

