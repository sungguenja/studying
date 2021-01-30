# 웹 앱 개발 2

> 1. 객체지향 JavsScript구현 - FE
> 2. 라이브러리 활용과 클린코드 - FE

# 객체 지향 JavaScript구현

```javascript
var data = [{title : "hello",content : "간지철철", price : 12000},
            {title : "crong",content : "괜춘한 상품", price : 5500},
            {title : "codesquad",content : "쩌는상품", price : 1200}];
```

위와 같은 데이터가 있다고 가정하자

for문과 forEach를 사용해보자

```javascript
for(var i=0; i<data.length; i++) {
    console.log(data[i].title,data[i].price)
}

data.forEach(function(v) {
    console.log(v.title,v.price)
})
```

arrow함수로도 가능

## map,filter

```javascript
var newData = data.map(function(v) {
    return v.price*v.price
})
// newData = [12000**2,5500**2,1200**2]

var newData = data.map(function(v) {
    var Obj = {title:v.title,content:v.content,price:v.price*3}
    return Obj
})
// 이러면 객체형태를 받게 된다!

var newData = data.filter(function(v) {
    return v.price>5000
})
// 가격이 5000원 이상인것만 나옴

var filteredData = data.filter(function(v) {
    return v.price > 5000;
}).map(function(v) {
  var obj = {};
  obj.title = v.title;
  obj.content = v.content;
  obj.price = (''+v.price).replace(/^(\d+)(\d{3})$/, "$1,$2원");
  return obj;
});
// 이런식으로 체이닝가능
```

### reduce

reduce는 배열의 모든 요소에 대해 지정된 콜백 함수를 호출하며, 콜백 함수의 반환 값을 누적하여 반환하는 함수입니다.

reduce 함수의 매개변수로 콜백 함수와 누적을 시작하기 위한 초기 값이며 초기 값은 선택사항입니다.

```javascript
var totalPrice = data.reduce(function(prevValue, product) { return prevValue + product.price; }, 0);
console.log(totalPrice);
```



## 객체 리터럴과 this

```javascript
var healthObj = {
  name : "달리기",
  lastTime : "PM10:12",
  showHealth : function() {
    console.log(this.name + "님, 오늘은 " + this.lastTime + "에 운동을 하셨네요");
  }
}

healthObj.showHealth(); //달리기님, 오늘은 PM10:12에 운동을 하셨네요
```

JavaScript에는 전역스크립트나 함수가 실행될 때 실행문맥(Execution context)이 생성됩니다.

(참고로 실제 실행은 브라우저내에 stack 이라는 메모리 공간에 올라가서 실행됩니다)

모든 context에는 참조하고 있는 객체(thisBinding이라 함)가 존재하는데, 현재 context가 참조하고 있는 객체를 알기 위해서는 this를 사용할 수 있습니다.

다시 말해, 함수가 실행될때 함수에서 가리키는 this 키워드를 출력해보면 context가 참조하고 있는 객체를 알 수 있습니다.

```javascript
function get() {
    return this;
}

get(); //window. 함수가 실행될때의 컨텍스트는 window를 참조한다.
new get(); //object. new키워드를 쓰면 새로운 object context가 생성된다.
```



## bind메소드로 this제어하기

### this가 달라지는 경우

showHealth는 어떤 이유인지 바로 출력하지 못하고, 1초 뒤에 결과를 출력하는 함수입니다.

this가 무엇을 가리킬까요? 

```javascript
var healthObj = {
  name : "달리기",
  lastTime : "PM10:12",
  showHealth : function() {
    setTimeout(function() {
        console.log(this.name + "님, 오늘은 " + this.lastTime + "에 운동을 하셨네요");      
    }, 1000)
  }
}
healthObj.showHealth(); //undefined 한 결과가 나온다
```

왜 이런 상황이 나올까? setTimeout으로 this가 window로 바뀌어버렸다!

### 위와 같은 것을 해결하자! bind

bind 새로운 함수를 반환하는 함수입니다. 이부분이 좀 어색하고 혼란스러울 수 있습니다. bind동작은 특이하게도 새로운 **함수를 반환**한다는 점을 잘 기억해야 합니다. 

bind함수의 첫번째 인자로 this를 주어, 그 시점의 this를 기억하고 있는 새로운 (바인드된)함수가 반환되는 것입니다.

```javascript
var healthObj = {
  name : "달리기",
  lastTime : "PM10:12",
  showHealth : function() {
    setTimeout(function() {
        console.log(this.name + "님, 오늘은 " + this.lastTime + "에 운동을 하셨네요");      
    }.bind(this), 1000)
  }
}
healthObj.showHealth();
```

만약 바인드를 쓰기 싫다면 어떻게 해야할까? arrow function도 비슷한 결과를 낸다. 제대로 알고 사용할 수 있도록 하자!