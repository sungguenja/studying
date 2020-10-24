// function getClosure() {
//     var text = 'variable 1'
//     return function() {
//         return text
//     }
// }

// var closure = getClosure()
// console.log(closure())

// var base = 'hello'
// function sayHello(name) {
//     var text = base + name
//     return function() {
//         console.log(text)
//     }
// }

// var hello1 = sayHello('asd')
// var hello2 = sayHello('aaa')
// hello1()
// hello2()
// hello1.text = 'ddd'
// hello1()
for (var i=0; i<10; i++) {
    setTimeout(function(){
        console.log(i,'i')
    },100)
}

for (i=0; i<10; i++) {
    (function(j) {
        setTimeout(function() {
            console.log(j,'j')
        },100)
    })(i)
}