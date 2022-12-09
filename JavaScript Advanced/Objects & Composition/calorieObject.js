function solve(arr) {
    const result = {};
    const products = arr.filter(a => arr.indexOf(a) % 2 === 0);
    const quantitites = arr.filter(a => arr.indexOf(a) % 2 === 1);

    for (let index = 0; index < products.length; index++) {
        result[products[index]] = Number(quantitites[index]);
    }
    console.log(result);
}
