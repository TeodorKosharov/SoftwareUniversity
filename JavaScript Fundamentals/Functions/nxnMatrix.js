function solve(n) {
    let result = [];
    for (let i = 1; i <= n; i++) {
        result.push(n);
    }

    for (let i = 1; i <= n; i++) {
        console.log(result.join(' '));
    }
}
