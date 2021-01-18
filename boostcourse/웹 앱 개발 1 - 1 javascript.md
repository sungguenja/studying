# 웹 앱 개발 1/4

> 1. JavaScript 배열 - FE
> 2. DOM API 활용 - FE
> 3. Ajax - FE
> 4. Web Animation - FE
> 5. WEB UI - FE
> 6. Tab UI - FE
> 7. Spring Core - BE
> 8. Spring JDBC - BE
> 9. Spring MVC - BE
> 10. 레이어드 아키텍처 - BE
> 11. Controller - BE

# JavaScript 

## 배열

배열 밖에 값을 줄려고 하면 값이 들어가고 그 사이는 undefined가 들어간다

```javascript
var a = [4];
a[1000] = 3;
console.log(a.length);  // 1001
console.log(a[500]); // undefined
```

다양한 메소드가 존재한다

```javascript
var origin = [1,2,3,4]
var result = origin.concat(2,3) // [...origin,2,3] 도 가능
console.log(origin,result) // [1,2,3,4] [1,2,3,4,2,3]
result.forEach(function(v,i,o) {
    console.log(v)
}) // 1 2 3 4 2 3이 하나씩 나옴 => 안을 화살표함수로 써도 되고 아예 함수를 밖에서 만들고 넣어도 괜찮다

var mapped = result.map(function(v) {
    return v*2
})
console.log(mapped, result) // [1,4,9,16,4,9] [1,2,3,4,2,3]
```



## 객체

파이썬의 딕셔너리 형태의 자료구조

값을 부를때는 파이썬처럼 `object['key']`도 가능하고 class처럼 `object.key`도 가능하다

```javascript
for(key in object) {
    console.log(object[key])
}

var myfriend = {'key':'value','add':'ddd'}
console.log(Object.keys(myfriend)) // ['key','add']
Object.keys(myfriend).forEach(function(v) {
    console.log(myfriend[v])
}) // 'value' 'ddd' 가 순차적으로 나온다
```

