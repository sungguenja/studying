# array

1. 반복문

   ```javascript
   const fruits = ['apple','banana'];
   // 1.
   for (let i = 0; i<fruits.length; i++) {
       console.log(fruits[i]);
   }
   // 2.
   for (let fruit of fruits) {
       console.log(fruit);
   }
   // 3.
   fruits.forEach(function (fruit,index,array) {
       console.log(fruit);
   })
   ```

2. concat

   두 array를 합친 것을 반환한다

   ```javascript
   const fruits2 = ['asd','fas'];
   const new_fruits = fruits.concat(fruits2);
   ```

3. indexOf

   해당 원소가 있는 위치를 반환하는 메소드. 없으면 `-1`을 반환

4. join

   파이썬 join과 비슷하지만 사용 방법은 약간 다름

   ```javascript
   console.log(fruits.join(' '))
   ```

5. split

   파이썬과 같고 사용법도 같음

   ```javascript
   const fruits_string = 'apple,banana'
   const result = fruits_string.split(',') // ['apple','banana']
   ```

6. reverse

   리스트를 뒤집어주는데 뒤집어준 것을 반환도 하면서 원본 리스트도 뒤집어버림

