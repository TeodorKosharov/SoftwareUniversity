function solve(arr) {
    let arrNums = arr.map(x => Number(x));
    return arrNums[0] + arrNums[arrNums.length - 1];
}