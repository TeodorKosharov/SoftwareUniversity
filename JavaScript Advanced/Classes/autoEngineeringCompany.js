function solve(arr) {
    let cars = {};

    for (const el of arr) {
        let [brand, model, quantity] = el.split(' | ');
        quantity = Number(quantity);

        if (cars[brand] === undefined) {
            cars[brand] = {};
            cars[brand][model] = quantity;
        } else {
            if (cars[brand][model] === undefined) {
                cars[brand][model] = quantity;
            } else cars[brand][model] += quantity;
        }
    }

    for (const carName in cars) {
        console.log(carName);
        for (const carModel in cars[carName]) console.log(`###${carModel} -> ${cars[carName][carModel]}`);
    }
}
