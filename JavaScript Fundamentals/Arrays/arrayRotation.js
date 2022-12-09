function solve(arr, rotations) {
    for (let rotation = 1; rotation <= rotations; rotation++) {
        arr.push(arr.splice(0, 1));
    }
    console.log(arr.join(' '));
}
