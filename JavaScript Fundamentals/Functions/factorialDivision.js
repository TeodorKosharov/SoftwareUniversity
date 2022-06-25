function solve(a, b) {
    let firstResult = 1;
    let secondResult = 1;

    for (let i = 1; i <= a; i++) {
        firstResult *= i;
    }
    
    for (let i = 1; i <= b; i++) {
        secondResult *= i;
    }
    let result = firstResult / secondResult;
    console.log(result.toFixed(2));
}
