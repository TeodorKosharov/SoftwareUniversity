function solve(fruit, grams, kgPrice) {
    let kg = grams / 1000;
    let price = kgPrice * kg;
    console.log(`I need $${price.toFixed(2)} to buy ${kg.toFixed(2)} kilograms ${fruit}.`);
}
