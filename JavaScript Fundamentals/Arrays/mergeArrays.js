function solve(arr1, arr2) {
    let arr3 = [];
    for (let index = 0; index < arr1.length; index++) {
        index % 2 == 0 ? arr3.push(Number(arr1[index]) + Number(arr2[index])) : arr3.push(arr1[index] + arr2[index]);
    }
    console.log(arr3.join(' - '));
}
