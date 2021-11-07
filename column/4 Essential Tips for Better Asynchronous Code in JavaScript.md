# 4 Essential Tips for Better Asynchronous Code in JavaScript

[원글 링크](https://www.ditdot.hr/en/4-tips-better-asynchronous-javascript-code)

## 1. Run In Parallel, Await Later to Make Your Code Run Faster

Promises는 열렬하다. GET 요청은 우리가 함수를 호출하는 순간 보내진다. 다른말로 await는 함수의 실행을 promise가 끝날때까지 멈추게 한다. 우리 코드를 효과적으로 만들려면 최대한 뒤로 미루는 것이 좋다는 소리다.

### 어떻게 paraller한 요청을 만들지?

```javascript
// fake fetch function returning a new Promise object
const fetchFile = (file) => new Promise(resolve => fakeFetch(file, resolve))

// request all files at once, in parallel
const promise1 = fetchFile('file1')
const promise2 = fetchFile('file2')
const promise3 = fetchFile('file3')

// await later
const file1 = await promise1
// 또는 아래와 같이
// we can await for the value immediately, the files are still being requested in parallel
const fileArray = await Promise.all([fetchFile('file1'), fetchFile('file2'), fetchFile('file3')])
```

### 그러면 언제 await를 써?

order 받았을때 쓰자! 매요청마다 하면 꽤 느려진다. 

> 주요 팁: 독립적인 비동기 작업에 대한 병렬 요청을 사용하여 대기 및 성능 저하를 방지합니다.

## 2. Create an Array of Promises With map()

이전 상황에서는 매번 요청을 보내는 형식이다. 그렇다면 리스트로 만들어서 한번에 보내는 것은 어떨까? 

```javascript
// fake fetch function returning a new Promise object
const fetchFile = (file) => new Promise(resolve => fakeFetch(file, resolve))

// array populated with an arbitrary number of elements
const fileNames = ['file1', 'file2', 'file3'/* ... */] 

// builds an array of promises with a callback that returns a Promise object
const promises = fileNames.map(fetchFile)

const files = await Promise.all(promises)
```

이러한 케이스는 한번에 보내지는 것이 가능하다!

> 주요 팁: 많은 promise을 처리할 때, 그것들을 배열로 저장하세요.

## 3. Loop Over Promises With for...of

`forEach`를 이용하는것도 좋은 전략이지만 아래와 같은 코드는 작동이 원하는대로 되지 않는다

```javascript
// this will not log in order
promises.forEach(async promise => console.log(await promise))
```

왜? `Async`는 항상 `promise`를 리턴한다. 즉, 위 코드는 꽤나 멍청한 소리인 것과 다름이 없다. synchronous iterators에 열렬해지자. 다양한 메소드들은 어떻게 멈추고 어떻게 value를 위해 기다릴지 promise를 작업하면 어떻게 작동될지 알수없다. 그러므로, 대부분의 케이스들은 우리가 비동기코드로 돌릴 필요가 없다. 특히, 어레이 메소드콜백과 함께.  돌리고 싶다면 아래와 같이 하는것이 정말로 좋다

```javascript
// for...of
for (const promise of promises) {
  console.log(await promise)
}

// for await...of
for await (const result of promises) {
  console.log(result)
}

// Promise.all returns a single promise that resolves with an array of results 
for (const result of await Promise.all(promises)) {
  console.log(result)
}
```

> 주요 팁: promise 배열에 배열 메서드를 사용합니다. 콜백 기능의 promise에 대한 포장을 해제하거나 기다리지 않도록 합니다. 대신 for...을 선택하라.

## 4. Consider Promise.allSettled() Instead Promise.all()

위 두 메소드는 다르다, 그리고 둘다 사용하는 것은 정말 좋다.

```javascript
const promises = fileNames.map(file => fetchFile(file).catch(() => 'rejected'))
const results = await Promise.all(promises)
const resolved = results.filter(result => result !== 'rejected')
```

`promise.all`은 생각보다 조금 복잡하게 작동을 하고 있다. catch의 에러로 다음과같이 얻을 수가 있는데 `allSettled`를 이용한다면 아래와 깉이 이용이 가능하다.

```javascript
const promises = fileNames.map(fetchFile)
const results = await Promise.allSettled(promises)
const resolved = results.filter(result => result.status === 'fulfilled').map(result => result.value)
```

> 주요 팁: reject에 대한 상태를 잘 조절하고 싶다면 `Promise.all()`을 사용하자. 실패한 것을 아예 거르고 싶다면 `Promise.allSettled()`를 이용하자.
>
> 그리고 둘의 가장 극 강대점은 어찌되었든 둘 다 평행하게 이용이 된다는 것이다.

