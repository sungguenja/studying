class People {
    constructor(name) {
        this.name = name;
    }

    sayName() {
        console.log(this.name);
    }

    get name() {
        return this._name;
    }

    set name(name) {
        if (name.length < 5) {
            console.log('너무짧');
            return ;
        }
        this._name = name;
    }
}

class User extends People {
    constructor(name) {
        super(name);
    }
}

let test = new People('asdfaa')
let user_test = new User('aaa')