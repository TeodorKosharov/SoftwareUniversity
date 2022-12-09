function solve(str, repeat) {
    let result = str;
    for (let i = 1; i < repeat; i++) {
        result += str;
    }
    return result;
}
