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

# DOM API 활용

documet. 으로 사용할 수 있는 APIs : [링크 바로가기](https://www.w3schools.com/jsref/dom_obj_document.asp)

element. 으로 사용할 수 있는 APIs : [링크 바로가기](https://www.w3schools.com/jsref/dom_obj_all.asp)

**DOM 탐색 속성**

- childNodes
  - 엘리먼트의 자식 노드의 노드 리스트 반환(텍스트 노드, 주석 노드 포함)
  - [childNodes 예제](https://jsbin.com/qabuciz/edit?html,js,console,output)
- firstChild
  - 엘리먼트의 첫 번째 자식 노드를 반환
  - [firstChild 예제](https://jsbin.com/fuconuk/1/edit?html,js,console,output)
- firstElementChild
  - 첫 번째 자식 엘리먼트를 반환
  - [firstElementChild 예제](https://jsbin.com/retoses/2/edit?html,js,console,output)
- parentElement
  - 엘리먼트의 부모 엘리먼트 반환 
  - [parentElement 예제](https://jsbin.com/jonumig/2/edit?html,js,console,output)
- nextSibling
  - 동일한 노드 트리 레벨에서 다음 노드를 반환 
  - [nextSibling 예제](https://jsbin.com/jonumig/6/edit?html,js,console,output)
- nextElementSibling
  - 동일한 노드 트리 레벨에서 다음 엘리먼트 반환
  - [nextElementSibling 예제](https://jsbin.com/podawep/2/edit?html,js,console,output)

**DOM 조작 메소드**

- removeChild()
  - 엘리먼트의 자식 노드 제거 
  - [removeChild 예제](https://jsbin.com/lexobe/13/edit?html,js,console,output)
- appendChild()
  - 마지막 자식 노드로 자식 노드를 엘리먼트에 추가
  - [appendChild 예제](https://jsbin.com/wunocen/5/edit?html,js,console,output)
- insertBefore()
  - 기존 자식노드 앞에 새 자식 노드를 추가
  - [insertBefore 예제](https://jsbin.com/xogutix/5/edit?html,js,output)
- cloneNode()
  - 노드를 복제
  - [cloneNode 예제](https://jsbin.com/puyeled/3/edit?html,js,output)
- replaceChild()
  - 엘리먼트의 자식 노드 바꿈
  - [replaceChild 예제](https://jsbin.com/rumadi/8/edit?html,js,output)
- closest()
  - 상위로 올라가면서 가장 가까운 엘리먼트를 반환
  - [closest 예제](https://jsbin.com/rumadi/13/edit?html,js,console,output)

**HTML을 문자열로 처리해주는 DOM 속성 / 메소드**

- innerText
  - 지정된 노드와 모든 자손의 텍스트 내용을 설정하거나 반환
  - [innerText 예제](https://jsbin.com/sukihiw/6/edit?html,js,output)
- innerHTML
  - 지정된 엘리먼트의 내부 html을 설정하거나 반환
  - [innerHTML 예제](https://jsbin.com/sutejo/3/edit?html,js,output)
- insertAdjacentHTML()
  - HTML로 텍스트를 지정된 위치에 삽입
  - [insertAdjacentHTML() 예제](https://jsbin.com/puwoqov/4/edit?html,js,output)

[insertAdjacentHTL 위치별 커멘드](https://developer.mozilla.org/ko/docs/Web/API/Element/insertAdjacentHTML)

> 실습
>
> **실습1**
>
> 지금 나온 DOM API를 사용해서, strawberry 아래에 새로운 과일을 하나 더 추가하시오.
>
> 추가 된 이후에는 다시 삭제하시오.
>
> [링크 바로가기](http://jsbin.com/mebuha/1/edit?html,js,output)
>
> 
>
> **실습2**
>
> insertBefore메서드를 사용해서, orange와 banana 사이에 새로운 과일을 추가하시오.
>
> [링크 바로가기](http://jsbin.com/mebuha/1/edit?html,js,output)
>
> 
>
> **실습3**
>
> 실습2를 insertAdjacentHTML메서드를 사용해서, orange와 banana 사이에 새로운 과일을 추가하시오.
>
> 
>
> **실습4**
>
> apple을 grape 와 strawberry 사이로 옮기시오.
>
> [링크 바로가기](http://jsbin.com/mebuha/1/edit?html,js,output)
>
> 
>
> **실습5**
>
> class 가 'red'인 노드만 삭제하시오.
>
> [링크 바로가기](http://jsbin.com/redetul/1/edit?html,css,js,output)
>
> 
>
> **실습6**
>
> section 태그의 자손 중에 blue라는 클래스를 가지고 있는 노드가 있다면, 그 하위에 있는 h2 노드를 삭제하시오.
>
> [링크 바로가기](http://jsbin.com/ricopa/1/edit?html,css,js,output)
>
> **좀더 알아보기**
>
> **polyfill**은 무엇인지 한번 찾아보세요!
>
> 어떠한 기능을 쓰고 싶은데, 지원하지 않는 브라우저에서도 동작시키게 하고 싶을때가 있죠. 그때 아주 유용합니다.

