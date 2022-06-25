function solve(arr) {
    let groceries = arr.shift().split('!');
    for (let command of arr) {
        if (command == "Go Shopping!") break;
        let tokens = command.split(' ');
        if (tokens[0] == 'Urgent') {
            if (!(groceries.includes(tokens[1]))) groceries.splice(0, 0, tokens[1]);
        } else if (tokens[0] == 'Unnecessary') {
            if (groceries.includes(tokens[1])) groceries.splice(groceries.indexOf(tokens[1]), 1);
        } else if (tokens[0] == 'Correct') {
            if (groceries.includes(tokens[1])) { 
                groceries[groceries.indexOf(tokens[1])] = tokens[2];
            }
        } else if (tokens[0] == 'Rearrange') {
            if (groceries.includes(tokens[1])) {
                groceries.splice(groceries.indexOf(tokens[1]), 1);
                groceries.push(tokens[1]);
            }
        }
    }
    console.log(groceries.join(', '));
}
