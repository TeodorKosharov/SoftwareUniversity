function solve(arr) {
    while (arr.length > 1) {
        let condenseArr = [];
        for (let index = 0; index < arr.length - 1; index++) {
            condenseArr.push(arr[index] + arr[index + 1]);
        }
        arr = condenseArr;
    }
    console.log(arr[0]);
}
