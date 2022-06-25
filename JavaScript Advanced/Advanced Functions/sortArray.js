function solve(arr, command) {
    command === 'asc' ? arr.sort((a, b) => a - b) : arr.sort((a, b) => b - a);
    return arr;
}
