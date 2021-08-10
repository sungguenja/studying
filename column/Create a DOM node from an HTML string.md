# Create a DOM node from an HTML string

[칼럼 링크](https://grrr.tech/posts/create-dom-node-from-html-string/)

- Dom을 삽입하는 여러 방법들

  - `innerHTML`

    ```javascript
    const placeHolder = document.createElement('div');
    placeholder.innerHTML = html;
    const node = placeHolder.firstElementChild;
    ```

    - 안전성: no script execution
    - 가능한 노드만 가능
    - 지원 좋음
    - [Element.innerHTML](https://developer.mozilla.org/en-US/docs/Web/API/Element/innerHTML)

  - `insertAdjacentHTML`

    ```javascript
    const placeHolder = document.createElement('div');
    placeHolder.insertAdjacentHTML('afterbbegin',html);
    const node = placeHolder.firstElementChild;
    ```

    - 안전성: no script execution
    - 가능한 노드만
    - IE10빼고
    - [Element.insertAdjacentHTML()](https://developer.mozilla.org/en-US/docs/Web/API/Element/insertAdjacentHTML)

  - DOMParser

    ```javascript
    const node = new DOMParser().parseFromString(html, 'text/html').body.firstElementChild;
    ```

    - 안전성: no script execution
    - 가능한 노드만 가능
    - ie10+, Safari9.1+ 빼고
    - [DOMParser](https://developer.mozilla.org/en-US/docs/Web/API/DOMParser)

  - Range

    ```javascript
    const node = document.createRange().createContextualFragment(html);
    ```

    - 안전성: executes scripts, sanitize first
    - 컨텍스트를 맞출 수 있음
    - 지원 구림
    - [Range.createContextualFragment()](https://developer.mozilla.org/en-US/docs/Web/API/Range/createContextualFragment)

- 주의사항

  - 테이블관련 노드는 정말 이상하게 작동할 수 있다 주의하자

  - 이상한 상황들 나열하기

    - ```javascript
      const placeholder = document.createElement('div');
      placeholder.innerHTML = `<tr><td>Foo</td></tr>`;
      const node = placeholder.firstElementChild; //=> null
      ```

    - ```javascript
      const table = document.createElement(`table`);
      const tbody = document.createElement(`tbody`);
      table.appendChild(tbody);
      
      const range = document.createRange();
      range.selectNodeContents(tbody);
      const node = range
          .createContextualFragment(`<tr><td>Foo</td></tr>`); //=> tr
      ```

    - ```javascript
      const template = document.createElement('template');
      template.innerHTML = `<tr><td>Foo</td></tr>`;
      const node = template.content.firstElementChild; //=> tr
      ```

    - ```javascript
      const placeholder = document.createElement('div');
      placeholder.innerHTML = `<div><script>alert('Foo');</script></div>`;
      const node = placeholder.firstElementChild;
      
      document.body.appendChild(node); //=> will not show an alert
      ```

    - ```js
      const placeholder = document.createElement('div');
      placeholder.innerHTML = `<img src='x' onerror='alert(1)'>`;
      const node = placeholder.firstElementChild;
      
      document.body.appendChild(node); //=> will show an alert (!)
      ```

- 성능.

  - `Range.createContextualFragment()` — **winner** (fastest in Firefox)
  - `Element.insertAdjacentHTML()` — **winner**
  - `Element.innerHTML` — **winner**
  - `DOMParser.parseFromString()` — **90% slower**

- 좀더 향상된 형태

  - ```js
    const htmlToElement = html => ({ /* ... */ });
    const fragment = document.createDocumentFragment();
    
    items.forEach(item => {
      const node = htmlToElement(`<div>${item.name}</div>`); 
      fragment.appendChild(node); 
    });
    
    document.body.appendChild(fragment);
    ```

  - 예

    - ```javascript
      var element  = document.getElementById('ul'); // assuming ul exists
      var fragment = document.createDocumentFragment();
      var browsers = ['Firefox', 'Chrome', 'Opera',
          'Safari', 'Internet Explorer'];
      
      browsers.forEach(function(browser) {
          var li = document.createElement('li');
          li.textContent = browser;
          fragment.appendChild(li);
      });
      
      element.appendChild(fragment);
      ```

