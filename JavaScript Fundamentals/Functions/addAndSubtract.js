function solve(a, b, c) {
    function sum(a, b) {
        return a + b;
    }

    let result = sum(a, b);

    function subtract(result, c) {
        return result - c;
    }
    console.log(subtract(result, c));
}
