function solve(arr1, arr2) {
    let products = {};
    for (let index = 0; index < arr1.length - 1; index += 2) {
        products[arr1[index]] = Number(arr1[index + 1]);
    }
    
    for (let index = 0; index < arr2.length - 1; index += 2) {
        if (!(Object.keys(products).includes(arr2[index]))) products[arr2[index]] = Number(arr2[index + 1]);
        else products[arr2[index]] += Number(arr2[index + 1]);
    }

    for (let product of Object.keys(products)) {
        console.log(`${product} -> ${products[product]}`);
    }
}
