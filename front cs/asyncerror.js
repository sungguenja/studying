function wait(sec) {
    return new Promise((resolve,reject) => {
        setTimeout(() => {
            // reject('wait error');
            // resolve('done!')
        },sec*1000);
    });
}

async function myAsyncFun() {
    console.log(new Date());
    const result = await wait(3).catch(e => {
        console.log(e);
    })
    console.log(result);
    console.log(new Date());
}