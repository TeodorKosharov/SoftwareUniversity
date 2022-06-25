function solve(arr) {
    arr.sort(function(a, b){return a-b}).reverse();
    let lastIndex = arr.length - 1;
    let result = [];

    for (let index = 0; index < arr.length / 2; index++) {
        result.push(arr[index]);
        if (lastIndex == index) break;
        result.push(arr[lastIndex]);
        lastIndex--;
    }
    console.log(result.join(' '));
}
