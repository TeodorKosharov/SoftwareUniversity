function solve(num) {
    num = String(num);
    let digitsSum = 0;
    let result = 'False';

    for (let index = 0; index < num.length; index++) {
        digitsSum += Number(num[index]);
    }

    for (let index = 0; index < String(digitsSum); index++) {
        if (String(digitsSum)[index] == '9') {
            result = 'True';
            break;
        }
    }
    console.log(`${num} Amazing? ${result}`);
}
