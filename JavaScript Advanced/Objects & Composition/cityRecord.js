// function solve(name, population, treasury) {
//     let result = {};
//     result['name'] = name;
//     result['population'] = population;
//     result['treasury'] = treasury;
//     return result;
// }

// Second variant using composition:

function solve(name, population, treasury) {
    return {
        name, population, treasury
    }
}
