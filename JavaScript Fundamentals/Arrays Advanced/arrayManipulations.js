function solve(arr) {
    let numbers = arr.shift();
    numbers = numbers.split(' ');
    for (let command of arr) {
        let tokens = command.split(' ');
        
        if (tokens[0] == 'Add') numbers.push(tokens[1]);
        else if (tokens[0] == 'Remove') numbers = numbers.filter(x => x != tokens[1]);
        else if (tokens[0] == 'RemoveAt') numbers.splice(Number(tokens[1]), 1);
        else if (tokens[0] == 'Insert') numbers.splice(Number(tokens[2]), 0, tokens[1]);
    }
    console.log(numbers.join(' '));
}
