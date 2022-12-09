function solve(arr) {
    arr.sort((a, b) => a - b);
    let half = Math.floor(arr.length / 2);
    return arr.slice(half);
}
