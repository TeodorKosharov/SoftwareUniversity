function solve(num, a, b, c, d, e) {
    function operation(action, value) {
        if (action == 'chop') return value / 2;
        else if (action == 'dice') return Math.sqrt(value);
        else if (action == 'spice') return value + 1;
        else if (action == 'bake') return value * 3;
        else return value - 0.20 * value;
    }


    let number = Number(num);
    number = operation(a, number);
    console.log(number);
    number = operation(b, number);
    console.log(number);
    number = operation(c, number);
    console.log(number);
    number = operation(d, number);
    console.log(number);
    number = operation(e, number);
    console.log(number);
}
