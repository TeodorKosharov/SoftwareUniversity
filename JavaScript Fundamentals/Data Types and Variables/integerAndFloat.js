function solve(a, b, c) {
    let sum = a + b + c;
    console.log(`${sum} - ${sum % 1 == 0 ? 'Integer' : 'Float'}`);
}
