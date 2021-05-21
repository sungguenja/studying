function showMessage(message,from) {
    console.log(message,from);
}
showMessage('hi') // 'hi',unknown

function printAll(...args) {
    for (const arg of args) {
        console.log(arg);
    }
}

let global_message = 'global'
function printMessage() {
    let message = 'hello';
    console.log(message);
    console.log(global_message);
}
// 위는 에러가 안난다!
// global에서는 local을 쓸 수 없지만 local에서는 global을 사용할 수가 있다.
// 함수 내에서 함수를 또다시 정의해도 상황은 같다!