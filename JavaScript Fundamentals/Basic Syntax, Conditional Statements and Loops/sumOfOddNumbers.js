function numbers(n) {
    let value = 1;
    let totalSum = 0;
    while (n > 0) {
        if (value % 2 != 0) {
            console.log(value);
            totalSum += value;
            n--;
        }
        value++;
    }
    console.log(`Sum: ${totalSum}`)
}
