# Vue.js 면접 질문

## 1. What is Vue.js

동적인 사용자 인터페이스(UI)를 만들기 위한 프레임 워크

## 2. 단방향 바인딩과 양방향 바인딩의 차이

- 단방향 바인딩: 데이터 흐름이 한쪽인 경우. `v-on`, `v-bind`, `{{}}` 로 지시어를 사용
  - `v-on(@)`은 UI에서 데이터 모델을 업데이트 하거나 출력할 때 사용한다
  - `v-bind(:)` 는 데이터 모델에서 업데이트 된 상태를 UI에 반영한다
- 양방향 바인딩: 데이터 바인딩이 양쪽인 경우
  - `v-model`: 데이터 모델이 변경되면 자동으로 UI도 변경

## 3. 컴포넌트 props?

props는 상위 컴포넌트에서 하위 컴포넌트에게 데이터를 전달한느 용으로 사용.

하위에서 상위로 이벤트를 전달할 때는 `emit`을 이용한다

## 4. filter?

- 일반적인 text 형식을 가공해주는 역할을 한다.
- 머스태시 태그와 v-bind에서 사용 가능하며, `|` 기호와 함께 사용한다
- 필터 체이닝도 가능하다

```vue
<!-- in mustached -->
{{ message | capitalize }} // capitalize -> filter

<!-- in v-bind -->
<div v-bind:id="rawId | formatId">
</div>
// formatId -> filter
```

## 5. 리다이렉트 하는 방법

`$router.push()`를 이용

## 6. 뷰 앱 구조에 대한 기본 갠념

vue는 루트 컴포넌트를 생성하고 루트 컴포넌트가 최상위를 기준으로 자식컴포넌트들이 tree구조로 구성됩니다

## 7. Vuex?

vue의 상태관리를 위한 라이브러리

## 8. mixins?

- mixin은 여러 컴포넌트간의 공통으로 사용하고 있는 로직, 상태들을 재사용하는 방법
- 2개의 컴포넌트가 동일한 기능을 가지고 있다고 생각해보자. 만약 같은 메서들르 2개 작성한다면 코드 중복 + 해당메서드들이 바뀌면 2번 수정해야함. 이걸 mixin을 통해 우아하게 처리가 가능하다.
- mixins: `[]` 속성으로 지정하면 된다.
- mixin과 컴포넌트의 옵션이 중첩이 된다면 두 옵션은 `Merged`된다.

## 9. 라이프 사이클

1. Creation 라이프 사이클 중 가장 먼저 실행되는 단계
   - 이 단계의 훅에서는 DOM트리에 해당 컴포넌트가 반영이 안된다
     - 즉, id or class로 접근 불가
   - 훅으로는 beforeCreated, created가 있다.
     - beforeCreated는 데이터나 이벤트에 접근조차 못한다
2. Mouniting은 DOM 삽입 단계로 랜더링 되기 직전의 컴포넌트에 접근이 가능하다
   - beforeMounted, mounted가 있다.
     - beforeMounted는 템플릿과 렌더 함수들이 컴파일이 되고 렌더링이 되기 직전이다
     - mounted는 컴포넌트가 렌더링이 된 상태일 때 호출된다. DOM에 접근할 수 있지만 주의해야할 점은 자식 컴포넌트의 마운트 상태를 보장할 수 없다
   - 아직 DOM element에 접근 불가
3. Updating은 웹페이지의 내용이나 무언가 바껴서 재랜더링을 해야하는 상황
   - beforeUpdate와 updated가 있따
     - beforeUpdate는 DOM변경이 완료가 되고 패치가 되기 직전에 호출이된다
     - updated는 재 렌더링이 완료된 이후에 호출이 된다
       - 재 렌더링 이후의 dom에 접근이 가능
4. Destruction은 컴포넌트가 파괴될 때 실행
   - beforeDestroy, destroyed가 있다.
     - beforeDestroy는 해체 직전에 호출되며 모든 DOM과 이벤트가 남아있음
     - destroyed는 해체가 완전히 된 후에 호출이 되는 훅