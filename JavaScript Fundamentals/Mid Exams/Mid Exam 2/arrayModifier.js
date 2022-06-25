function solve(arr) {
    let numbers = arr.shift().split(' ').map(x => Number(x));
    for (let command of arr) {
        if (command == 'end') break;
        else if (command == 'decrease') {
            for (let index = 0; index < numbers.length; index++) {
                numbers[index]--;
            }
        }
        let tokens = command.split(' ');
        if (tokens[0] == 'swap') {
            let a = numbers[Number(tokens[1])];
            let b = numbers[Number(tokens[2])];
            numbers[Number(tokens[1])] = b;
            numbers[Number(tokens[2])] = a;
        } else if (tokens[0] == 'multiply') {
            numbers[Number(tokens[1])] = numbers[Number(tokens[1])] * numbers[Number(tokens[2])];
        }
    }
    console.log(numbers.join(', '));
}
