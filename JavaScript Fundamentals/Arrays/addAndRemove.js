function solve(arr) {
    let num = 1;
    let result = [];

    for(let command of arr) {
        if (command == 'add') {
            result.push(num);
        } else {
            result.pop();
        }
        num++;
    }
    result.length > 0 ? console.log(result.join(' ')) : console.log('Empty');
}