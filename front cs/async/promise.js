'use strict';

const promise = new Promise((resolve,reject) => {
    /* 
    doing some heaby work ()
    resolve는 성공했을시 어떤 값을 전달해줄지
    reject는 실패했을시 어떤 값을 전달해줄지이다
    */
    console.log('doing something');
    resolve("ellie");
    reject(new Error('no network'))
});

promise.then((value) => {
    console.log(value);
})
.catch((error) => {
    console.log(error)
})
.finally(() => {
    console.log('finally')
})

const fetch_number = new Promise((resolve,reject) => {
    setTimeout(() => {
        resolve(3)
    },1000);
})

fetch_number
.then((num )=> {
    console.log(num)
    return num*2
})
.then((num) => {
    console.log(num)
    return num*3
})
.then(num => {
    return new Promise((resolve,reject) => {
        console.log(num)
        setTimeout(() => {
            resolve(num-1)
        },1000)
    });
})
.then(num => console.log(num));

console.log(fetch_number.then)