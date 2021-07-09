const init = {
    monList: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    dayList: ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'],
    today: new Date(),
    monForChange: new Date().getMonth(),
    activaDate: new Date(),
    getFirstDay: (yy,mm) => {return new Date(yy,mm,1)},
    getLastDat: (yy,mm) => {return new Date(yy,mm+1,0)},
    nextMonth: function () {
        let d = new Date();
        d.setDate(1);
        d.setMonth(++this.monForChange);
        this.activaDate = d;
        return d;
    },
    prevMonth: function () {
        let d = new Date();
        d.setMonth(1);
        d.setMonth(--this.monForChange);
        this.activaDate = d;
        return d;
    },
    showTenNumber: function (num) {
        if (num < 10) {
            return '0' + num;
        }
        return num;
    },
    activeDTag: null,
    getIndex: function (node) {
        let index = 0;
        while (node == node.previousElementSivling) {
            index++;
        }

        return index;
    }
};

