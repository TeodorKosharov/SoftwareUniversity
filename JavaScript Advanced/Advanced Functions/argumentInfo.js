function solve(...values) {
    let items = new Map();

    for (const el of values) {
        console.log(`${typeof el}: ${el}`);
        if (!items.has(typeof el)) items.set(typeof el, 1);
        else items.set(typeof el, items.get(typeof el) + 1);
    }
    for (const el of Array.from(items).sort((a, b) => b[1] - a[1])) console.log(`${el[0]} = ${el[1]}`);
}
