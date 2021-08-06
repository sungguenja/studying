# S.O.L.I.D The first 5 principles of Object Oriented Design with JavaScript

[컬럼 링크](https://medium.com/@cramirez92/s-o-l-i-d-the-first-5-priciples-of-object-oriented-design-with-javascript-790f6ac9b9fa) [코드 깃허브 링크](https://gist.github.com/Crizstian/ba39c6fdbb30a40c738e3c07ea83b5c1)

- 이 글을 요약하게 된 계기
  - solid이해가 좀 낮지 않을까 싶어서 여러 칼럼을 찾다 괜찮은 것이 있어서 가져왔음

> 자바스크립트는 타입에 느슨한 언어이다, 그래서 몇몇은 함수적 언어라 하고 몇몇은 객체지향이라고 하고 몇몇은 둘다라고 하고 몇몇은 클래스가 있는것 자체가 자바스크립트의 문제라고 한다

많은 사람들이 위와 같은 생각을 가지고 있다. 하지만 자바스크립트에도 충분히 SOLID를 도입가능하며 객체지향형 디자인이 가능하다. SOLID에 대한 뜻은 각자 알고 있을테니 다들 살펴볼 수 있도록 하자

## Single responsibility principle

> 클래스는 오직 단하나의 변경 이유를 가져야 한다. 그리고 클래스는 하나의 역할만을 해야한다

```javascript
const circle = (radius) => {
    const proto = {
        type: "Circle",
        // code
    }
    return Object.assign(Object.create(proto),{radius});
}

const square = (length) => {
    const proto = {
        type: "Square",
        // code
    }
    return Object.assign(Object.create(proto),{length});
}
```

### 팩토리 함수란 무엇인가?

> 자바스크립트에서 어떤 함수든 새 오브젝트를 리턴해줄 수가 있다. 그것이 constructor 함수나 class가 아니더라도 팩토리 함수라고 부를 수가 있다. [왜 팩토리 함수라고 부르는지에 대한 컬럼](https://medium.com/javascript-scene/javascript-factory-functions-vs-constructor-functions-vs-classes-2f22ceddf33e#.m5h2jj8a7) [명확한 설명 비디오](https://www.youtube.com/watch?v=ImwrezYhw4w)

```javascript
const areaCalculator = (s) => {
    const proto = {
        sum() {
            // logic to sum
        },
        output() {
            return `
				<h1>
					Sum of the areas of provided shapes:
					${this.sum()}
				</h1>
		   `
        }
    }
    
    return Object.assign(Object.create(proto), {shapes:s})
}
```

위 코드의 `areaCalculator` 팩토리 함수를 사용하면, 우리는 간단하게 함수를 부를수 있고 어떠한 모양이든지 통과시킬수 있고 페이제에 결과를 보여줄 수가 있다.

```javascript
const shapes = [
    circle(2),
    square(5),
    squere(6)
];

const areas = areaCalculator(shapes);
console.log(areas.output());
```

`areaCalculator`의 `output`메소드의 문제점은 `areaCalculator`가 데이터를 출력하는 로직을 관리한다는 것이다. 그러므로, 만약 유저가 json과 같은 데이터를 출력하고 싶다면 어떻게 해야하는가?

모든 로직이 `areaCalculator` 팩토리 함수에 의해 조절되어 야 한다. 이것은 **단일 책임 원칙에 위배된다** `areaCalculator`의 팩토리 함수는 제공하는 함수의 area를 합쳐야만 한다, 그것이 json이든 html이든 가리지 않고

그러니 우리는 `SumCalculatorOutputter` 팩토리 함수를 만들어서 고치고 조절해보자 어떠한 것이 오든 문제가 되지 않도록. 아래와 같이 짜면 될 거 같다

```javascript
const shapes = [
    circle(2),
    square(5),
    square(6)
]

const areas = areaCalculator(shapes);
const output = sumCalculatorOputter(areas);

console.log(output.JSON());
console.log(output.HAML());
console.log(output.HTML());
console.log(output.JASE());
```

이렇게 된다면 유저가 출력하고 싶은 데이터의 형태가 어떻든 간에 그것을 `sumCalculatorOutputter`팩토리 함수가 관리할 수 있다

## Open-closed Principle

> 객체 또는 엔티티들은 확장에는 열려있어야하지만 수정에는 닫혀있어야 한다

확장에 열려있어야 한다의 의미는 우리가 새 기능 또는 컴포넌트를 애플리케이션에 넣는것이 기존의 코드를 어기지 않고 가능해야한다는 소리이다

수정에 닫혀있어야 한다는 의미는 우리는 기존 기능에 변화를 가해서는 안된다는 소리이다. 리팩토링에 엄청난 문제를 겪게 하기 때문이다.

간단히 말해서 변화없이 확장하기 쉬워야 한다는 소리이다. 한번 아래 코드를 살펴보자

```javascript
sum() {
    const area = [];
    
    for (shape of this.shapes) {
        if (shape.type === "Square") {
            area.push(Math.pow(shape.length, 2));
        } else if (shape.type === "Circle") {
            area.push(Math.PI * Math.pow(shape.length,2));
        }
    }
    
    return area.reduce((v,c) => c+= v,0);
}
```

[reduce?](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/Reduce) 만약 우리가 `sum` 메소드를 모든 shape에 대해 area를 합치는 것을 가능하게 하고 싶다면, 우리는 `if/else`를 더 써서 넣어야 할 것이며 이것은 **`개방-폐쇄 원칙`에 위배된다** 

`sum`메소드를 만드는 더 좋은 방법은 `sum`메소드에서 각 shape들의 area를 계산하는 로직을 제거해라 그리고 shape의 팩토리 함수에 접근하게 하라

```javascript
const square = (length) => {
    const proto = {
        type: "Square",
        area () {
            return Math.pow(this.length,2);
        }
    }
    return Object.assign(Object.create(proto), {length});
}
```

이것을 다른 shape들에도 area를 계산하는 로직을 넣어주자 그러면 우리는 `sum`메소드를 아래와 같이 수정할 수 있을 것이다.

```javascript
sum() {
    const area = [];
    for (shape of this.shapes) {
        area.push(shape.area());
    }
    return area.reduce((v,c) => c+= v,0);
}
```

우리는 이제 또다른 shape클래스를 만드는 것이 어렵지 않을 것이다. 그리고 거기에 area를 계산해주는 로직을 넣어주면 된다. 즉, 우리는 shape에 대해서 확장하기 열려있으며 sum을 수정하는데에는 닫혀있는 것을 알 수 있다. 그러나 또다른 문제가 온다. `areaCalculaotr`에 넣어져서 나왔는지 아니면 그냥 내제된 함수를 이용했는지 우리는 어떻게 알 수 있는가?

타입스크립트의 interface를 이용하면 그런 문제는 우리는 이제 해결할 수 있다. 구조를 확인할 수 있기 때문이다.

```typescript
interface ShapeInterface { 
 area(): number 
}  

class Circle implements ShapeInterface {     
 let radius: number = 0     
 constructor (r: number) {        
  this.radius = r     
 }      
 
 public area(): number { 
  return MATH.PI * MATH.pow(this.radius, 2)
 } 
}
```

그런데 이것은 TypeScript이지 JavaScript가 아니다! 다르게 해결하려면 어떻게 해야할까? `함수 컴포지션`이 우리를 구출했다!

첫째로 우리는 `shapeInterface`팩토리 함수를 만들어보자/ 우리의 `shapeInterface`는 인터페이스를 추상화할 것이고 함수 컴포지션을 이용할 것이다. [컴포지션에 대한 더 좋은 비디오](https://www.youtube.com/watch?v=wfMtDGfHWpA)

```javascript
const shapeInterface = (state) => ({
    type: 'shapeInterface',
    area: () => state.area(state)
})
```

그 다은 square 팩토리 함수에 implement를 해보자

```javascript
const square = (length) => {
    const proto = {
        length,
        type: "Square",
        area: (args) => Math.pow(args.length,2)
    }
    const basics = shapeInterface(proto);
    const composite = Object.assign({},basics);
    return Object.assign(Object.create(composite), {length});
}
```

그다음 square 팩토리 펑션의 호출 결과는 다음과 같을 것이다

```javascript
const s = square(5)
console.log('OBJ\n', s)
console.log('PROTO\n', Object.getPrototypeOf(s))
s.area()
/* output
OBJ
 { length: 5 }
PROTO
 { type: 'shapeInterface', area: [Function: area] }
25
*/
```

`areaCaculator sum`메소드에서는 우리는 이 shape가 `shapeInterface`에서 제공하는 타입인지 확인만 하면 된다, 아니라면 예외를 던져주면 되는 것이고

```javascript
sum() {
  const area = []
  for (shape of this.shapes) {
    if (Object.getPrototypeOf(shape).type === 'shapeInterface') {
       area.push(shape.area())
     } else {
       throw new Error('this is not a shapeInterface object')
     }
   }
   return area.reduce((v, c) => c += v, 0)
}
```

자바스크립트는 인터페이스를 지원하지 않습니다. 하지만 시뮬레이팅한 인터페이스를 만들 수 있고 우리는 이것을 위해 클로저나 함수 컴포지션을 이용하면 된다. [클로저를 모른다면](https://medium.com/javascript-scene/master-the-javascript-interview-what-is-a-closure-b2f0d2152b36#.nkow9q73g) [클로저에 관한 비디오](https://www.youtube.com/watch?v=CQqwU2Ixu-U)

## Liskov substitution principle

> q(x)를 T 타입의 객체 x라는 것을 증명이 가능한 요소라고 하자. 그렇다면 q(y)도 T타입의 서브타입인 S 타입의 객체 y도 증명이 가능해야 한다.

쉬운 말로 다시 설명하자면, 서브 클래스는 클라이언트 관점에서 함수적인 것을 부수지 않는 방법으로 부모 클래스의 메소드를 오버라이드 한다는 것이다.

`areaCaclulator`펙토리 함수를 사용하기 위해 만들어보자,우리는 `areaCalculator`를 확장한 `volumeCalculator` 팩토리 함수를 가지고 있다. 그렇다면 아래와 같을 것이다.

```javascript
const volumeCalculator = (s) => {
    const proto = {
        type: 'volumeCalculator'
    }
    const areaCalProto = Object.getPrototypeOf(areaCalculator());
    const inherit = Object.assign({}, areaCalProtom, proto);
    return Object.assign(Object.create(inherit), {shapes:s});
}
```

## interface segregation principle

> 클라이언트는 사용되지 않는 인터페이스를 implement하라고 강요되어서는 안된다 또한 클라이언트는 사용되지 않는 메소드에 의존하도록 강요되서는 안된다

shapes 예제들과 계속해보자. 우리는 우리가 solid shape를 가진다는 것을 알고 우리가 shape의 volume을 계산하는 것을 원하게 될 것을 알고 있다. 우리는 `shapeInterface`를 추가할 수가 있따

```javascript
const shapeInterface = (state) => ({
    type: 'shapeInterface',
    area: () => state.area(state),
    volume: () => state.volume(state)
})
```

우리가 만든 어떠한 shape도 volume 메소드를 임플리먼트해야만 한다. 하지만 우리는 squares는 flat한 shape인 것을 알고 volume을 가지지 않는 다는 것을 안다. 그래서 이 인터페이스는 square 팩토리 함수가 쓰지 않는 것을 implement하는 것을 강요한다

interface segreagation principle은 이딴 짓을 그만하라고 말한다. ~~이런 짓을 한다면 모두 미치고 말것이다~~ 대신에 우리가 `solidShapeInterface`라고 불릴 interface를 만들어보자. 그것은 volume contract를 가지고 큐브와 같을 것이다

```javascript
const shapeInterface = (state) => ({
    type: "shapeInterface",
    area: () => state.area(state)
})

const solidShapeInterface = (state) => ({
    type: "solidShapeInterface",
    colume: () => state.volume(state)
})

const cubo = (length) => {
    const proto = {
        length,
        type: 'Cubo',
        area: (args) => Math.pow(args.length,2),
        volume: (args) => Math.pow(args.length,3)
    }
    
    const basics = shapeInterface(proto);
    const complex = solidShapeInterface(proto);
    const composite = Object.assign({},basics,complex);
    return Object.assign(Object.create(composite),{length})
}
```

조금 더 나은 접근법이다. 하지만 shape를 위한 sum을 계산해야할 때 조심해야할 위험도 있다. 대신에 `shapeInterface`를 사용하거나 `solidShapeInterface`를 사용할 수 있따

우리는 다른 interface를 만들 수 도 있다. (예를 들면 `manageShapeInterface`같은) 그리고 그것을 implement해올 수 있다 flat 또는 solid shape에, 이것운 우리가 쉽게 할수 있는 방안이다. 아래와 같은 예를 한번 살펴보자

```javascript
const manageShapeInterface = (fn) => ({
    type: "manageShapeInterface",
    calculate: () => fn()
})

const circle = (radius) => {
    const proto = {
        radius,
        type: "Circle",
        area: (args) => Math.PI * Math.pow(args.radius,2)
    }
    
    const basics = shapeInterface(proto);
    const abstraccion = manageShapeInterface(() => basics.area());
    const composite = Object.assign({}, basics, abstraccion);
    return Object.assign(Object.create(composite), {radius});
}

const cubo = (length) => {
    const proto = {
        length,
        type: "Cubo",
        area: (args) => Math.pow(args.length,2),
        volume: (args) => Math.pow(args.length,3)
    }
    
    const basics = shapeInterface(proto);
    const complex = solidShapeInterface(proto);
    const abstraccion = manageShapeInterface(() => basics.area() + complex.volume());
    const composite = Object.assign({},basics,abstraccion);
    return Object.assign(Object.create(composite),{length});
}
```

우리가 지금 보는 것처럼 우리는 자바스크립트에서 인터페이스에 해야하는 것은 함수 컴포지션을 위한 팩토리 함수이다.

그리고 여기, `manageShapeInterface`와 함께 우리가 해야할 것은 추상화되었다 `calculate`함수로, 우리가 여기서 하는 것과 다른 interface들, 우리가 `high order functions`를 사용하며 추상화를 이루어냈다. [high order function?](https://www.youtube.com/watch?v=BMUiFMZr7vk&list=PL0zVEGEvSaeEd9hlmCXrk5yUyqUag-n84)

## Dependency inversion principle

> 엔티티는 추상적인 것에 의존해야만 한다. 하이 레벨 모듈은 로우 레벨 모듈에 의존해서는 안되지만 그들은 추상화에 의존해야 한다

동적 언어에 있어서, 자바스크립트는 디커플링을 용이하게 하기 위해 추상화를 사용할 필요는 없다. 그러므로, 추상화가 디테일에 의존해야 한다는 규정은 사실 자바스크립트에서는 크게 중요하지는 않다. 그러나 하이래밸 모듈이 로우래밸 모듈에 의존하면 안된다는 규정은 다르다

> 함수적인 관점에서, 컨테너들과 인젝션 컨셉들은 풀수 있어야 한다 간단한 상위 부르는 함수에서 또는 미들 타입 패턴에서

[의존성 역전 규칙은 어떻게 상위 함수와 연관이 있는가?](https://softwareengineering.stackexchange.com/questions/103508/how-is-dependency-inversion-related-to-higher-order-functions) 

어렵다고 느낄 수 있지만 정말 이해하기 쉽다. 이 원칙은 디커플링을 위해 허락한다. 그리고 우리는 만들 수 있다. `manageShapeInterface`를 다시 살펴보고 `calculate`메소드를 어떻게 마치는지 생각해보자

```javascript
const manageShapeInterface = (fn) => ({
    type: "manageShapeInterface",
    calculate: () => fn()
})
```

`manageShapeInterface`팩토리 함수가 받는 것은 상위 함수이다, 저것은 모든 shape를 위해 펑셔널리티를 디커플하고 마지막 calculation을 얻기 위한 로직을 필요로 하는 것을 함수적으로 이룩해낸다. 아래 구조를 살펴보자

```javascript
const square = (radius) => {
  // code
 
  const abstraccion = manageShapeInterface(() => basics.area())
 
 // more code ...
}
const cubo = (length) => {
  // code 
  const abstraccion = manageShapeInterface(
    () => basics.area() + complex.volume()
  )
  // more code ...
}
```

## 결론

> 만약 당신이 SOLID 원칙을 극단적으로 받아들인다면, 너는 함수적 프로그래밍에 대해 도달할 수도 있다

자바스크립트는 멀티 패러다임 프로그래밍 언어이다. 그리고 우리는 solid 원칙을 도입시킬 수 있으ㅡ고 대단히 좋으며 우리는 함수 프로그래밍 패러다임과 혼합할 수도 있다.

자바스크립트는 또한 동적 프로그래밍 언어이고 다재 다능하다 위 글은 그저 solid원칙을 해결하기 위한 한가지 방법이다. 다양하게 해결해나갈 수 있도록 해보자!