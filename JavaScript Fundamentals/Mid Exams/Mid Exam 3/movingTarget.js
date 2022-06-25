function solve(arr) {
    let sequence = arr.shift().split(' ').map(x => Number(x));
    for (let el of arr) {
        if (el == 'End') break;
        let tokens = el.split(' ');
        if (tokens[0] == 'Shoot') {
            let index = Number(tokens[1]);
            let power = Number(tokens[2]);
            if (index >= 0 && index < sequence.length) {
                sequence[index] -= power;
                if (sequence[index] <= 0) sequence.splice(index, 1);
            }
        } else if (tokens[0] == 'Add') {
            let index = Number(tokens[1]);
            let value = Number(tokens[2]);
            if (index >= 0 && index < sequence.length) {
                sequence.splice(index, 0, value);
            } else console.log("Invalid placement!");
        } else {
            let index = Number(tokens[1]);
            let radius = Number(tokens[2]);
            let shotIndex = index - radius;
            let shots = (radius * 2) + 1;

            for (let i = 1; i <= shots; i++) {
                if (shotIndex >= 0 && shotIndex < sequence.length && sequence.length > 0) {
                    sequence.splice(shotIndex, 1);
                } else {
                    console.log("Strike missed!");
                    break;
                }
            }
        }
    }
    console.log(sequence.join('|'));
}
