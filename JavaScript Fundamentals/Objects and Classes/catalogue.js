function solve(arr) {
    let products = [];
    let productsObject = {};

    for (let el of arr) {
        let tokens = el.split(' : ');
        products.push([tokens[0], Number(tokens[1])]);
    }
    products.sort((a, b) => a[0].localeCompare(b[0]));
    
    for (let product of products) {
        if (!(Object.keys(productsObject).includes(product[0][0]))) {
            productsObject[product[0][0]] = [`${product[0]}: ${product[1]}`];
        } else productsObject[product[0][0]].push(`${product[0]}: ${product[1]}`);
    }

    for (let element of Object.keys(productsObject)) {
        console.log(element);
        for (let productInfo of productsObject[element]) console.log(`  ${productInfo}`);
    }

}

solve([
    'Appricot : 20.4',
    'Fridge : 1500',
    'TV : 1499',
    'Deodorant : 10',
    'Boiler : 300',
    'Apple : 1.25',
    'Anti-Bug Spray : 15',
    'T-Shirt : 10'
    ]);