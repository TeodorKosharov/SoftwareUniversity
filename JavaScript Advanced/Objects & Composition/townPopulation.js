function solve(arr) {
    let towns = {};

    for (let el of arr) {
        let [city, population] = el.split(' <-> ');
        if (!(towns.hasOwnProperty(city))) {
            towns[city] = Number(population)
        } else {
            towns[city] += Number(population);
        }
    }

    for (let city in towns) {
        console.log(`${city} : ${towns[city]}`);
    }
}
