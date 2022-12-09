function solve(arr) {
    arr.sort((a, b) => a.localeCompare(b));
    for (let number = 1; number <= arr.length; number++) {
        console.log(`${number}.${arr[number - 1]}`);
    }
}
