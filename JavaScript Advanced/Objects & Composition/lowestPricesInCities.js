function solve(arr) {
    const result = {};

    for (const el of arr) {
        const [town, product, price] = el.split(' | ');
        if (!(result.hasOwnProperty(product))) {
            result[product] = [Number(price), town];
        } else if (result.hasOwnProperty(product) && Number(price) < result[product][0]) {
            result[product] = [Number(price), town];
        }
    }

    for (const key in result) {
        console.log(`${key} -> ${result[key][0]} (${result[key][1]})`);
    }
}
