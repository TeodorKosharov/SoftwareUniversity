function solve(requirementsObject) {
    let wheelsSize;
    const engines = {
        'Small engine': {power: 90, volume: 1800},
        'Normal engine': {power: 120, volume: 2400},
        'Monster engine': {power: 200, volume: 3500}
    }

    requirementsObject.wheelsize % 2 === 0
        ? wheelsSize = 2 * Math.floor(requirementsObject.wheelsize / 2) - 1
        : wheelsSize = requirementsObject.wheelsize;

    let engine;
    if (requirementsObject.power <= 90) engine = engines['Small engine'];
    else if (requirementsObject.power > 90 && requirementsObject.power <= 120) engine = engines['Normal engine'];
    else engine = engines['Monster engine'];

    return {
        model: requirementsObject.model,
        engine,
        carriage: {
            type: requirementsObject.carriage,
            color: requirementsObject.color
        },
        wheels: [wheelsSize, wheelsSize, wheelsSize, wheelsSize]
    }
}

console.log(solve({
    model: 'VW Golf II',
    power: 90,
    color: 'blue',
    carriage: 'hatchback',
    wheelsize: 14
}))
