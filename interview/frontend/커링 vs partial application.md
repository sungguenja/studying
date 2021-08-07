# 커링 vs partial application

함수형 기법들이다. 간단히 알아보자

##  Partial application

여러 개의 인자를 받는 함수가 있을 때 일부의 인자를 고정한 함수를 만드는 기법이다.

```javascript
var plus = function(a, b, c) {
  return a + b + c;
};

Function.prototype.partial = function() {
  var args = [].slice.apply(arguments);
  var self = this;
  return function() {
    return self.apply(null, args.concat([].slice.apply(arguments)));
  };
};

var plusa = plus.partial(1);
plusa(2, 3); // 6
var plusb = plusa.partial(2);
plusb(4); // 7
var plusab = plus.partial(1, 3);
plusab(5); // 9
```

이렇게 클로저와 바인딩을 이용해 구현이 가능하다. 더 깔끔하게 하는 방법은 그냥 bind를 쓰자

```javascript
var plusa = plus.bind(null, 1);
plusa(2, 3); // 6
var plusb = plusa.bind(null, 2);
plusb(4); // 7
var plusab = plus.bind(null, 1, 3);
plusab(5); // 9
```

## 커링

커링은 partial application처럼 인자를 미리 고정하는 것이지만 **하나씩**맘ㄴ 고정한다는 특징이 있다.

```javascript
function multiplyThree(x) {
  return function(y) {
    return function(z) {
      return x * y * z;
     }
  };
}
multiplyThree(4)(8)(2); // 64
```

인자가 100개 있다고 해보자. 어질어질하다. 아래와 같이 커리를 구현해 조금 간단히 가보자

```javascript
Function.prototype.curry = function(one) {
  var origFunc = this;
  var target = origFunc.length;
  var args = [];
  function next(nextOne) {
    args = args.concat(nextOne);
    if (args.length === target) {
      return origFunc.apply(null, args);
    } else {
      return function(nextOne) { return next(nextOne) };
    }
  }
  return next(one);
}

function multiplyFour(w, x, y, z) {
  return w * x * y * z;
}
multiplyFour.curry(2)(3)(4)(5); // 120
```

