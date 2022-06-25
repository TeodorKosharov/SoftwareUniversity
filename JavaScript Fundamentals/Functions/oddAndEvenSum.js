function solve(num) {
    let number = String(num);
    let evenSum = 0;
    let oddSum = 0;

    for (let index = 0; index < number.length; index++) {
        Number(number[index]) % 2 == 0 ? evenSum += Number(number[index]) : oddSum += Number(number[index]);
    }

    console.log(`Odd sum = ${oddSum}, Even sum = ${evenSum}`);
}
