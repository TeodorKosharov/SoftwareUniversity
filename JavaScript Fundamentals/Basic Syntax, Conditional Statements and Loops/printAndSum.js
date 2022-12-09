function solve(start, end) {
    let sum = 0;
    let result = '';

    for (let i = start; i <= end; i++) {
        sum += i;
        result += String(i) + ' ';
    }

    console.log(result);
    console.log(`Sum: ${sum}`);
}
