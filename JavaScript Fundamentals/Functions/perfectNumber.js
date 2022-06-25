function solve(num) {
    let sum = 0;

    for (let i = 1; i < num; i++) {
        if (num % i == 0) sum += i;
    }

    sum == num ? console.log('We have a perfect number!') : console.log("It's not so perfect.");
}