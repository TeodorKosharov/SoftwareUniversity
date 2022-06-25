function solve(arr) {
    let dictionary = {};
    let dictArr = [];
    for (let el of arr) {
        let element = JSON.parse(el);
        dictionary[Object.keys(element)] = element[Object.keys(element)];
    }
    for (let key of Object.keys(dictionary)) {
        dictArr.push([key, dictionary[key]]);
    }

    dictArr.sort((a, b) => a[0].localeCompare(b[0]));
    for (let item of dictArr) console.log(`Term: ${item[0]} => Definition: ${item[1]}`);
}
