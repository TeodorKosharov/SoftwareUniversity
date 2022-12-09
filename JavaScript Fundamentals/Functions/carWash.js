function solve(commands) {
    let value = 0;

    for (let command of commands) {
        if (command == 'soap') value += 10;
        else if (command == 'water') value += 0.20 * value;
        else if (command == 'vacuum cleaner') value += 0.25 * value;
        else value -= 0.10 * value;
    }
    console.log(`The car is ${value.toFixed(2)}% clean.`);
}
