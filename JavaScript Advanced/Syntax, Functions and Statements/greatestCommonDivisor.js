function solve(a, b) {
    let gcd = 1;

    for (let i = 2; i <= b; i++) {
        if (a % i == 0 && b % i == 0) gcd = i;
    }
    console.log(gcd);
}
