# Axios Instance

> 1. 서론
> 2. instance 만들기
> 3. 굳이?

## 1. 서론

axios를 쓰다보면 자주 같은 주소로 요청을 보내는데 이것을 좀 줄이고 싶은 경우가 있을 것이다. <br/>
이것을 모듈화 해서 따로 만들어도 괜찮지만 instance를 만드는 방법도 있다. 한번 살펴보자

## 2. instance 만들기

만드는 법 자체는 아래와 같이 간단하게 만들 수가 있다

```javascript
const axios_instance = axios.create({
  baseURL: "baseUrl",
});
```

위와 같이 쉽게 만들 수가 있다. 또한 필요한 성분을 미리 넣어두고 필요할때 꺼내다 쓰면 어렵지 않게 이용이 가능하다. 이용하는 방법은 다양하게 있다. 클로저로 만드는 방법도 있고 export를 이용하는 방법도 있다.
리액트를 쓰는 분들이라면 (나도 포함) export를 이용하는 방법도 편할 수가 있다고 생각한다. 둘다 살펴보자

```javascript
const axiosMethod = () => {
  const axios_instance = axios.create({ baseURL: "baseURL" });

  return {
    get: function (넣을것) {
      return axios_instance.get(넣을것);
    },
    post: function (넣을것) {
      return axios_instance.post(넣을것);
    },
  };
};
```

```javascript
const axios_instance = axios.create({
  baseURL: "baseUrl",
});
export const getRequest = (넣을것) => {
  return axios_instance.get(넣을것);
};
```

위와 같이 간단하게 이용할 수가 있으니 편한 방식을 잘 골라서 사용하도록 하자

## 3. 굳이?

여기까지 보면 누군가 말할 수가 있다

> 굳이 이걸 써야합니까?

하지만 생각보다 많은 이점이 있다. 2번항목에서 보던 것처럼 간단한 방식뿐만 아니라 다양한 것을 설정할 수가 있다.

1. 디폴트값 설정
   <br/>
   간단하게 이용할 수 있다. 만약 타임아웃을 설정을 해야한다면 아래와 같이 지정해주면 된다. 그러면 인스턴스를 이용하는 상황에서는 편안하게 해당 설정이 적용이 된다.
   ```javascript
   axios_instance.defaults.timeout = 2500;
   ```
2. 인터셉터 추가
   <br/>
   요청, 응답 둘 다에 대한 인터셉터를 간단하게 사용할 수가 있다.

   ```javascript
   // 요청에 관한 인터셉터
   axios_instance.interceptors.request.use(
     (config) => {
       // 요청을 보내기 전에 수행할 로직
       return config;
     },
     (error) => {
       // 에러가 발생했을 때 로직
       return error;
     }
   );

   // 응답에 관한 인터셉터
   axios_instance.interceptors.response.use();
   ```

## 4. 결론

간단하게 만들고 이용할 수 있다는 장점이 있다. 또한 해당 방식을 이용한다면 필요한 요청을 보낼 백엔드 서버마다 axios 인스턴스를 따로 지정해서 요청을 보낼 모듈을 만들기도 매우 쉬울 수도 있다. 필요시에 적당히 이용해볼 수 있도록 하자!
