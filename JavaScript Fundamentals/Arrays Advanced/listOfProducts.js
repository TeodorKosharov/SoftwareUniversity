function solve(arr) {
    let products = arr.sort();
    let counter = 1;

    for (let product of products) {
        console.log(`${counter}.${product}`);
        counter++;
    }
}
