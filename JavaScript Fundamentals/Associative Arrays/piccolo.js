function solve(arr) {
    let cars = [];

    for (let el of arr) {
        let [command, number] = el.split(', ');
        if (command == 'IN' && !(cars.includes(number))) {
            cars.push(number);
        } else if (command == 'OUT' && cars.includes(number)) {
            cars.splice(cars.indexOf(number), 1);
        }
    }

    if (cars.length > 0) {
    for (let carNumber of cars.sort()) {
        console.log(carNumber);
        }
    } else console.log('Parking Lot is Empty');
}
