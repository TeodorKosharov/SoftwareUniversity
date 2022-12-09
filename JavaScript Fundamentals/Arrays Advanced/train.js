function solve(arr) {
    let wagons = arr.shift().split(' ');
    let maxCapacity = Number(arr.shift());
    for (let command of arr) {
        let tokens = command.split(' ');
        if (tokens[0] == 'Add') wagons.push(tokens[1]);
        else {
            for (let index = 0; index < wagons.length; index++) {
                if (Number(wagons[index]) + Number(tokens[0]) <= maxCapacity) {
                    wagons[index] = Number(wagons[index]) + Number(tokens[0]);
                    break;
                }
            }
        }       
    }
    console.log(wagons.join(' '));
}
