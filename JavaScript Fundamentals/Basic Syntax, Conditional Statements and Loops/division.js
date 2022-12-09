function division(value) {
    let result = 'Not divisible';
    if (value % 2 == 0) {
        result = 2;
    } 
    if (value % 3 == 0) {
        result = 3;
    }
    if (value % 6 == 0) {
        result = 6;
    }
    if (value % 7 == 0) {
        result = 7;
    }
    if (value % 10 == 0) {
        result = 10;
    } 

    console.log(result == 'Not divisible' ? result : `The number is divisible by ${result}`)
}
