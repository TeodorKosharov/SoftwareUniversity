function solve(arr) {
    let vegetables = new Map();
    for (let el of arr) {
        let tokens = el.split(' ');
        if (!(vegetables.has(tokens[0]))) vegetables.set(tokens[0], Number(tokens[1]));
        else {
            let existingQuantity = vegetables.get(tokens[0]);
            vegetables.set(tokens[0], existingQuantity + Number(tokens[1]));
        }
    }

    for (let key of vegetables.keys()) console.log(`${key} -> ${vegetables.get(key)}`);
}
