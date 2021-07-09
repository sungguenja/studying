// 세션 스토리지는 세션이 끝나면 파괴되지만 로컬은 파괴되지 않는것을 기억하자. 둘의 사용법은 비슷하다
sessionStorage.setItem("key","value");
console.log(sessionStorage.getItem("key"));
// 하나만 삭제
sessionStorage.removeItem("key");
// 전부 삭제
sessionStorage.clear();
// 스트링형태로만 저장이 가능하다. 즉, 객체를 저장하기는 힘들다. 따라서 아래와 같은 방법이 요구된다
sessionStorage.setItem("object",JSON.stringify({a:1,b:2}));
console.log(JSON.parse(sessionStorage.getItem('object')))