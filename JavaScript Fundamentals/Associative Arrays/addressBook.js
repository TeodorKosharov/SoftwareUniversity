function solve(arr) {
    let info = {};
    for (let el of arr) {
        let tokens = el.split(':');
        info[tokens[0]] = tokens[1];
    }

    let infoArr = Object.entries(info);
    infoArr.sort((a, b) => a[0].localeCompare(b[0]));
    for (let person of infoArr) console.log(`${person[0]} -> ${person[1]}`);
}
