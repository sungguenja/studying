var _promise = function(param) {
    return new Promise(function(resolve, reject) {
        // 비동기를 표현하기 위한 setTimeout
        window.setTimeout(function() {
            // 파라메터가 참
            if (param) {
                // 해결
                resolve('해결완료')
            }
            // 파라메터가 거짓
            else {
                // 실패
                reject(Error('실패'))
            }
        },3000)
    })
}

_promise(true)
.then(function(text) {
    console.log(text)
}, function(error) {
    console.error(error)
})