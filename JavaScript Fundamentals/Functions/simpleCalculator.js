function solve(a, b, action) {
    if (action == 'add') return a + b;
    else if (action == 'subtract') return a - b;
    else if (action == 'multiply') return a * b;
    else return a / b;
}