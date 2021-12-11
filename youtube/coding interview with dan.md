# coding interview with dan abramov

[영상 링크](https://youtu.be/XEt09iK8IXs)

## dnagerouslySetInnerHtml

[리액트 링크](https://ko.reactjs.org/docs/dom-elements.html)
<br/>
넥스트 처럼 서버로부터 받을 수 있는듯 하다

## center me

글씨를 화면 정 가운데에 위치시키는 것인데 여기서 `%`, `vh`의 차이를 알 수 있다.

- %: 부모 기준
- vh: 뷰 화면 기준

## 노드 스왑하기

```javascript
function swap(node) {
  left = node.left;
  right = node.right;
  node.left = right;
  node.right = left;
  swap(node.left);
  swap(node.right);
}
```
