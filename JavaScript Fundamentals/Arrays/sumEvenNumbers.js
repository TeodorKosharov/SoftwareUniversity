function solve(arr) {
    let = sum = 0;
    for (let index = 0; index < arr.length; index++) {
        Number(arr[index]) % 2 == 0 ? sum += Number(arr[index]) : sum += 0;
    }
    console.log(sum);
}
