function solve({ name, area, population, country, postCode }) {
    let obj = { 
        name,
        area,
        population,
        country,
        postCode
    }
    for (let key of Object.keys(obj)) {
        console.log(`${key} -> ${obj[key]}`);
    }
}

solve({
    name: "Plovdiv",
    area: 389,
    population: 1162358,
    country: "Bulgaria",
    postCode: "4000"
   });
