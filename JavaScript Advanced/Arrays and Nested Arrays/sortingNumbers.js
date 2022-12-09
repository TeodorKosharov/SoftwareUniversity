function solve(arr) {
    let sorted = arr.sort((a, b) => a - b);
    let result = [];
    let lastIndex = sorted.length - 1;

    for (let index = 0; index < (sorted.length) / 2; index++) {
        result.push(sorted[index]);
        result.push(sorted[lastIndex]);
        lastIndex--;
    }

    if (sorted.length % 2 == 1) result.pop();
    return result;
}
