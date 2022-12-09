function solve(arr, rotations) {
    for (let rotation = 1; rotation <= rotations; rotation++) {
        arr.unshift(arr.pop());
    }
    console.log(arr.join(' '));
}
