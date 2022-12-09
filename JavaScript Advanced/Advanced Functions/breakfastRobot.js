function solution() {
    let microelements = {
        protein: 0, carbohydrate: 0, fat: 0, flavour: 0
    };

    const products = {
        apple: {carbohydrate: 1, flavour: 2},
        lemonade: {carbohydrate: 10, flavour: 20},
        burger: {carbohydrate: 5, flavour: 3, fat: 7},
        eggs: {protein: 5, fat: 1, flavour: 1},
        turkey: {protein: 10, carbohydrate: 10, fat: 10, flavour: 10}
    };


    return function (command) {
        let tokens = command.split(' ');

        if (tokens[0] === 'restock') {
            if (microelements.hasOwnProperty(tokens[1])) microelements[tokens[1]] += Number(tokens[2]);
            return 'Success';
        } else if (tokens[0] === 'prepare') {
            let recipe = tokens[1];
            let quantity = Number(tokens[2]);

            for (const product in products[recipe]) {
                if (products[recipe][product] * quantity > microelements[product]) return `Error: not enough ${product} in stock`;
            }

            for (const key in products[recipe]) {
                microelements[key] -= quantity * products[recipe][key];
            }
            return 'Success';

        } else if (tokens[0] === 'report') {
            return `protein=${microelements.protein} carbohydrate=${microelements.carbohydrate} fat=${microelements.fat} flavour=${microelements.flavour}`;
        }

    }
}

let manager = solution ();
console.log(manager('restock flavour 50'));
console.log(manager('prepare lemonade 4'));
console.log(manager('restock carbohydrate 10'));
console.log(manager('restock flavour 10'));
console.log(manager('prepare apple 1'));
console.log(manager('restock fat 10'));
console.log(manager('prepare burger 1'));
console.log(manager('report'));
