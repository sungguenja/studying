# typescript 기초

[영상 리스트](https://www.youtube.com/playlist?list=PLZKTXPmaJk8KhKQ_BILr1JKCJbR0EGlx0)

> 1. 왜써요?
> 2. 기본 타입
> 3. 인터페이스
> 4. 함수
> 5. 리터럴, 유니온/교차 타입
> 6. 클래스
> 7. 제네릭
> 8. 유틸리티 타입

## 1. 왜써요?

자바스크립트는 아주 자유롭다는 장점이자 단점이 있다. 심지어 경고조차 안날리는 경우도 종종 존재한다.

[여기서 타입스크립트를 연습할 수가 있다](https://typescript-play.js.org/)

## 2. 기본 타입

```typescript
let car:string = 'bmw'; // 타입 추론이 되기에 let car = 'bmw'; 이렇게 해도 string으로 자동으로 할당해줌

// car = 3; 이런식으로 이제 진행하면 에러가 난다

let a:number[] = [1,2,3];
let b:Array<number> = [1,2,3]; // 둘 다 된다

// 튜플
let b:[string,number]; // 0번째는 string 1번째는 number가 들어가야함

// void 아무것도 반환하지 않는 함수 타입
function sayHello():void {
    console.log('hello');
}

// never 에러를 반환하거나 영원히 끝나지 않는 함수의 타입
function showError():never{
    throw new Error();
}

function infLoop():never{
    while (true) {
        // do something
    }
}

// enum 비슷한 값들끼리 묶여있다고 생각하자
enum Os {
    Window,
    Ios,
    Android
}

let myOs:Os; // 이런식으로 가능, 객체랑 약간 다른 점은 지정되어있는것만 변경가능하다
```

## 3. 인터페이스

```typescript
let user:object;

user = {
    name: 'xx',
    age: 30
}
```

위 코드는 에러가 난다. 왜냐하면 object에는 name속성과 age속성이 없기때문이다! 일반적으로 쓰던것처럼 진행하면 안된다. 그래서 interface가 있다

```typescript
type Score = 'A' | 'B' | 'C' | 'F';

interface User {
    name: string;
    age: number;
    gender? : string; // 생성시 말고 추후에 설정해둬도 되는 방식
    readonly birthYear: number; // 생성만 가능하고 추후에 수정 불가능
    [grade:number] : string; // number타입의 키와 string으로 이루어진 속성을 만들겠다. 여러개 생성할때 계속 생성해도 된다
    // 위를 이렇게 코드를 바꿀 수도 있다. [grade:number] : Score; 
}

let user : User {
    name: 'xx',
    age: 30,
    birthYear: 2000,
    1 : 'A',
    2 : 'B'
}

user.age = 10;
user.asdf = 'asdf'; // 에러발생
```

함수 설정도 가능하다

```typescript
interface Add {
    (num1:number, num2:number): number;
}

const add : Add = function (x,y) {
    return x + y;
}
```

implements나 extends도 가능하다

```typescript
interface Car {
    color: string;
    wheels: number;
    start(): void;
}

class Bmw implements Car {
    color;
    wheels = 4;
    constructor(c:string) {
        this.color = c;
    }
    start() {
        console.log('go....');
    }
}
```

## 4. 함수

```typescript
// optional하게 가능, optional이라 해도 타입은 지켜야한다.
function hello(name?:string) {
    return `Hello, ${name || "world"}`;
}

// 다른 예시 이 경우 타입도 같이 정해주게 된다.
function hello(name = 'world') {
    return `Hello, ${name}`;
}
```

this타입을 명시해주는 것도 가능하다. 파라미터 제일 앞에 써주는 방식을 취한다.

```typescript
interface User {
    name: string;
}

const Sam: User = {name:'Sam'}

function showName(this:User, age:number, gender:'m'|'f') {
    console.log(this.name, age, gender);
}

const a = showName.bind(Sam);
a(30,'m');
```

인풋 타입에 따라 반환 타입이 달라진다면 overriding기법을 이용한다

```typescript
interface User {
    name: string;
    age: number;
}

function join(name: string, age: string): string;
function join(name: string, age: number): User;
function join(name: string, age: number | string): User | string {
    if (typeof age === 'number') {
        return {
            name,
            age
        };
    } else {
        return '나이는 숫자로 입력해주세요.';
    }
}

const sam: User = join('Sam', 30);
const jane: string = join('jane', '30');
```

## 5. 리터럴, 유니온/교차 타입

```typescript
// Literal Types
const userName1 = "Bob";
let userName2: string | number = "Tom";
userName2 = 3; // 에러가 일어나지 않는다
```

이런식으로 선택권을 주는 것이 리터럴이다. 아래와 같이 할 수도 있다

```typescript
type Job = "police" | "developer" | "teacher";

interface User {
    name: string;
    job: Job;
}

const user: User = {
    name: "bob",
    job: "police" // 위에 설정해두지 않은 값으로 하면 에러를 반환할 것이다 숫자로 리터럴도 가능하다
}
```

그리고 타입에 대해서 여러가지 경우를 주는 것을 유니온이라고 한다. 즉, 타입 | 타입 의 경우는 유니온 변수 | 변수 의 경우는 리터럴이라고 할 수가 있다.

교차타입은 and의 의미로 섞는다는 느낌을 가지면 된다

```typescript
interface Car {
    name: string;
    start(): void;
}

interface Toy {
    name: string;
    color: string;
    price: number;
}

const toyCar: Toy & Car = {
    name: '타요',
    start() {},
    color: 'blue',
    price: 1000
}
```

## 6. 클래스

```typescript
class Car {
    static wheels = 4; // 접근하고 싶다면 this가 아니라 class.property로 접근해야한다 ex) Car.wheels
    color: string; // 이렇게 미리 선언해줘야 에러가 일어나지 않는다
    // 위를 안적고 에러가 안일어나게 하고 싶다면 color 앞에 public 또는 readonly를 적어준다
    constructor(color:string) {
        this.color = color;
    }
    start() {
        console.log('start');
    }
}

const bmw = new Car('red');
```

접근 제한자 - public, private, protected가 있다. public은 접근이 가능하다. 하지만 private는 자식조차 접근이 불가능하다. 아무것도 적지 않으면 public이 디폴트고 private 또는 변수앞에 바로 `#`을 붙여주면 private로 설정된다. protected는 자식은 접근할 수 있지만 외부에선 접근이 불가능하다.

- public: 아무대서나 접근 가능
- private: 누구도 접근 불가
- protected: 자식만 접근 가능

수정 불가능한 속성을 주고 싶다면 readonly를 넣어주면 된다. abstract 로 추상 클래스를 생성할 수가 있다.

## 7. Generics

```typescript
function getSize(arr: number[]):number {
    return arr.length;
}

const arr1 = [1,2,3];
getSize(arr1); // 3

const arr2 = ['a','b','c'];
getSize(arr2); // 에러가 일어난다 유니온타입을 이용하거나 다양하게 방법이 있지만
// 다들 수정을 조금씩 해줘야하는 문제가 있다 그래서 아래와 같이 가능하다

function getSize<T>(arr: T[]): number {
    return arr.length;
}

const arr1 = [1,2,3];
getSize<number>(arr1); // 3
const arr2 = ['a','b','c'];
getSize<string>(arr2); // 3
```

```typescript
interface Mobile<T> {
    name: string;
    price: number;
    option: T;
}

const m1: Mobile<string> = {
    name: 'S20',
    price: 900,
    option: 'good'
} 

const m2: Mobile<object> = {
    name: 'S21',
    price: 200,
    option: {
        color: 'red',
        coupon: false
    }
} // object를 직접 {color:string} 이런식으로 적어줘도 되긴 한다
```

```typescript
interface User {
    name: string;
    age: number;
}

interface Car {
    name: string;
    color: string;
}

interface Book {
    price: number;
}

function showName<T extends {name:string}>(data: T): string {
    return data.name;
} // 이런식으로 Book같이 없는 속성이 들어오는 경우에 에러를 반환할 수 있도록 만들 수가 있다
```

## 8. 유틸리티 타입

```typescript
// keyof
interface User = {
    id: number;
    name: string;
    age: number;
    gender: 'm' | 'f';
}

type UserKey = keyof User; // 'id' | 'name' | 'age' | 'gender'
```

```typescript
// Partial<T>
interface User = {
    id: number;
    name: string;
    age: number;
    gender: 'm' | 'f';
}

let admin: Partial<User> = {
    id: 1,
    name: 'Bob'
} // 이러면 age, gender을 넣어주지 않아도 에러가 안난다! 부분으로만 받겠다는 소리
// 즉 없는것을 넣으면 에러가 반환됨
```

```typescript
// Required<T>
interface User = {
    id: number;
    name: string;
    age?: number;
    gender?: 'm' | 'f';
}

let admin: Required<User> = {
    
} // 모든 것을 넣어줘야 함 optional도 다 넣어줘야 함
```

```typescript
// Readonly<T>
// 수정을 못하고 읽기만 할 수 있게 만들어버린다
```

```typescript
// Record<K,T>
type Grade = "1" | "2" | "3" | "4";
type Score = "A" | "B" | "C" | "F";

const score: Record<Grade,Score> = {
    1: "A",
    2: "B",
    3: "F",
    4: "A",
}

interface User = {
    id: number;
    name: string;
    age: number;
}

function isValid(user:User) {
    const result: Record<keyof User, boolean> = {
        id: user.id > 0,
        name: user.name !== "",
        age: user.age > 0,
    };
    return result;
}
```

```typescript
// Pick<T,K> 선택
interface User = {
    id: number;
    name: string;
    age: number;
    gender: 'm' | 'f';
}

const admin: Pick<User, "id" | "name"> = {
    id: 0,
    name: "bob",
}

// Omit<T,K> 제외
interface User = {
    id: number;
    name: string;
    age: number;
    gender: 'm' | 'f';
}

const admin: Pick<User, "age" | "gender"> = {
    id: 0,
    name: "bob",
}
```

```typescript
// Exclude<T1,T2>
// T1에서 T2랑 겹치는 속성을 제외하는 것
```

