function solve(str) {
    let obj = JSON.parse(str);
    for (let el of Object.keys(obj)) {
        console.log(`${el}: ${obj[el]}`);
    }
}
