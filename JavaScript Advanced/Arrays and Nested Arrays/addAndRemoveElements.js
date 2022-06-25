function solve(arr) {
    let number = 1;
    let result = [];

    for (let command of arr) {
        if (command == 'add') {
            result.push(number);
        } else if (command == 'remove' && result.length >= 1) {
            result.pop();
        }
        number++;
    }
    result.length >= 1 ? console.log(result.join('\n')) : console.log('Empty');
}
