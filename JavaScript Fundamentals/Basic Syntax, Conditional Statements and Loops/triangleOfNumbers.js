function solve(n) {
    let repeat = 1;

    for (let i = 1; i <= n; i++) {
        let result = '';
        for (let j = 1; j <= repeat; j++) {
            result += String(i) + ' ';
        }
        console.log(result);
        repeat++;
    }
}
