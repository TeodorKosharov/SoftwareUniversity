function getFibonator() {
    const x = [];

    return function () {
        if (x[x.length - 1] === undefined || x[x.length - 2] === undefined) {
            x.push(1);
            return 1;
        }

        let y = x[x.length - 1] + x[x.length - 2];
        x.push(y);
        return y;
    }
}


let fib = getFibonator();
console.log(fib()); // 1
console.log(fib()); // 1
console.log(fib()); // 2
console.log(fib()); // 3
console.log(fib()); // 5
console.log(fib()); // 8
console.log(fib()); // 13
