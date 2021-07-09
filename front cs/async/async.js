function delay(ms) {
    return new Promise(resolve => {setTimeout(resolve,ms)});
}

async function getApple() {
    await delay(3000);
    return 'apple';
}

async function getBanana() {
    await delay(3000);
    return 'banana';
}

function pickFruits() {
    return getApple()
    .then(apple => {
        return getBanana().then(banana => `${apple} + ${banana}`)
    })
}

async function pickFruits2() {
    const applePromise = getApple();
    const bananaPromise = getBanana();
    const apple = await applePromise;
    const banana = await bananaPromise;
    return `${apple} + ${banana}`
}

function pickAllFruits() {
    return Promise.all([getApple(),getBanana()]).then((fruits) => {
        return fruits.join(' + ')
    })
}

pickFruits().then((result) => {
    console.log(result)
})

getApple()
.then((result) => {console.log(result)})

pickAllFruits().then((result) => {console.log(result)})

async function test() {
    return 'test';
}

test().then((result) => {console.log(result + result)})

const asdf = new Promise((resolve,reject) => {
    resolve("good");
    reject("not good");
})

asdf.then((result) => {console.log(result)})