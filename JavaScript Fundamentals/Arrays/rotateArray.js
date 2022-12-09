function solve(arr) {
    let rotations = Number(arr.pop());
    for (let rotation = 1; rotation <= rotations; rotation++) {
        arr.splice(0, 0, arr.pop());
    }
    console.log(arr.join(' '));
}
