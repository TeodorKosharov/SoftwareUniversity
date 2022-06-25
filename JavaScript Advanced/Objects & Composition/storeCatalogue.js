function solve(arr) {
    const result = {};
    const dictionary = {};

    for (const el of arr) {
        const [product, price] = el.split(' : ');
        result[product] = price;
    }

    const sortedProducts = Object.entries(result).sort((a, b) => a[0].localeCompare(b[0]));
    for (const [product, price] of sortedProducts) {
        dictionary.hasOwnProperty(product[0]) ? dictionary[product[0]].push(`${product}: ${price}`) : dictionary[product[0]] = [`${product}: ${price}`];
    }

    for (const letter in dictionary) {
        console.log(letter);

        for (const product of dictionary[letter]) console.log(`  ${product}`);
    }
}
