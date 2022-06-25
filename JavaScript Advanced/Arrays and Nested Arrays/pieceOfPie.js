function solve(arr, start, end) {
    let result = [];
    let fill = false;

    for (let el of arr) {
        if (el == start) fill = true;
        if (fill == true) result.push(el);
        if (el == end) fill = false; 
    }
    return result;
}
