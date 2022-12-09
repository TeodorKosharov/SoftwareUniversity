function solve(a, b) {
    let start = a.charCodeAt(0);
    let end = b.charCodeAt(0);
    let result = '';

    if (start < end) {
        for (let charCode = start + 1; charCode < end; charCode++) {
            result += String.fromCharCode(charCode) + ' ';
        }
    } else {
        for (let charCode = end + 1; charCode < start; charCode++) {
            result += String.fromCharCode(charCode) + ' ';
        }
    }
    console.log(result);
}
