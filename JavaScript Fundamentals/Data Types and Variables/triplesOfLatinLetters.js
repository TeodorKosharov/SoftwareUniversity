function triples(num) {
    num = Number(num);
    for (let a = 97; a < 97 + num; a++) {
        for (let b = 97; b < 97 + num; b++) {
            for (let c = 97; c < 97 + num; c++) {
                console.log(String.fromCharCode(a) + String.fromCharCode(b) + String.fromCharCode(c));
            }
        }
    }
}
