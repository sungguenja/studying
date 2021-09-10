# ussAsync 커스텀 hook 만들어서 사용하기

[칼럼 링크](https://react.vlpt.us/integrate-api/03-useAsync.html)

## useAsync.js

```javascript
import { useReducer, useEffect } from 'react';

function reducer(state, action) {
    switch (action.type) {
        case 'Loading':
            return {
                loading: true,
                data: null,
                error:null
            };
        case 'Success':
            return {
                loading: false,
                data: action.data,
                error: null
            };
        case 'Error':
            return {
                loading: false,
                data: null,
                error: action.error
            };
        default:
            throw new Error(`Unhandled action type: ${action.type}`);
    }
}

function useAsync(callback, deps = []) {
    const [state, dispatch] = useReducer(reducer, {
        loading: false,
        data: null,
        error: false
    });
    
    const fetchData = async () => {
        dispatch({type:'Loading'});
        try {
            const data = await callback();
            dispatch({type:'Success',data});
        } catch (e) {
            dispatch({type:'Error',data});
        }
    };
    
    useEffect(() => {
        fetchData();
    },deps);
    
    return [ state, fetchData ];
}

export {useAsync};
```

[useReducer 참고](https://react.vlpt.us/basic/20-useReducer.html) `useAsync` callback과 useEffect에 적용할 [deps(두번째 인자)](https://gist.github.com/ninanung/0ea87bc3d14ed8b1f9e7488561a4b910)를 받는다. 비동기 함수를 callback으로 넣고 그 파라미터가 바뀔 때 새로운 데이터를 불러오고 싶은 경우에 활용 가능하다. 사용 예를 한번 보자

## Users.js

```javascript
import React from 'react';
import axios from 'axios';
import { useAsync } from './useAsync';

async function getUsers() {
    const response = await axios.get('url');
    return response.data;
}

function Users() {
    const [state,refetch] = useAsync(getUsers,[]);
    
    const {loading,data:users,error} = state;
    if (loading) return <div>loading....</div>;
    if (error) return <div>error</div>;
    if (!users) return null;
    return dom;
}
```

# 나중에 불러오기

위와 같은 방식으로 하면 deps특성상 처음과 끝에서만 데이터를 불러온다. 하지만 요즘 시대에 그때만 데이터를 불러오는 것은 매우 좋지 않다. 계속해서 요청을 보내는 경우도 많으며 다양한 경우가 많다 그러니 우리는 한번더 구조를 바꿔서 제작해보자

## useAsync.js

```javascript
import { useReducer, useEffect } from 'react';

function reducer(state, action) {
    switch (action.type) {
        case 'Loading':
            return {
                loading: true,
                data: null,
                error:null
            };
        case 'Success':
            return {
                loading: false,
                data: action.data,
                error: null
            };
        case 'Error':
            return {
                loading: false,
                data: null,
                error: action.error
            };
        default:
            throw new Error(`Unhandled action type: ${action.type}`);
    }
}

function useAsync(callback, deps = [], skip = false) {
    const [state, dispatch] = useReducer(reducer, {
        loading: false,
        data: null,
        error: false
    });
    
    const fetchData = async () => {
        dispatch({type:'Loading'});
        try {
            const data = await callback();
            dispatch({ type: 'Success', data });
        } catch (e) {
            dispatch({ type: 'Error', error: e });
        }
    };
    
    useEffect(() => {
        if (skip) return;
        fetchData();
    },deps);
    
    return [state, fetchData];
}

export {useAsync};
```

`skip` 파라미터를 이용해 useEffect를 멈추게 하는 작업이다. 그렇다면 어떻게 사용할지 생각을 해보자

## Users.js

```javascript
import React from 'react';
import axios from 'axios';
import useAsync from './useAsync';

// useAsync 에서는 Promise 의 결과를 바로 data 에 담기 때문에,
// 요청을 한 이후 response 에서 data 추출하여 반환하는 함수를 따로 만들었습니다.
async function getUsers() {
  const response = await axios.get('url');
  return response.data;
}

function Users() {
  const [state, reload] = useAsync(getUsers, [], true);

  const { loading, data: users, error } = state; // state.data 를 users 키워드로 조회

  if (loading) return <div>로딩중..</div>;
  if (error) return <div>에러가 발생했습니다</div>;
  if (!users) return <button onClick={reload}>불러오기</button>;
  return (
    <>
      <ul>
        {users.map(user => (
          <li key={user.id}>
            {user.username} ({user.name})
          </li>
        ))}
      </ul>
      <button onClick={reload}>다시 불러오기</button>
    </>
  );
}

export default Users;
```

이제 마음껏 커스터마이징이 가능하다! 만약 form데이터가 필요하면 useAsync를 조금 바꿔서 파라미터를 받아올 수도 있다.