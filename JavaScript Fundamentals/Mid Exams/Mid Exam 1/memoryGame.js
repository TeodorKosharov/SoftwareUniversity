function solve(arr) {
    let sequence = arr.shift().split(' ');
    let moves = 0;
    let win = false;

    for (let el of arr) {
        if (el == 'end') break;
        let tokens = el.split(' ').map(x => Number(x));
        if (sequence.length == 0) {
            console.log(`You have won in ${moves} turns!`);
            win = true;
            break;
        }

        moves++;
        let firstIndex = tokens[0];
        let secondIndex = tokens[1];

        if (firstIndex == secondIndex || firstIndex < 0 || firstIndex >= sequence.length || secondIndex < 0 || secondIndex >= sequence.length) {
            let middle = Math.ceil(sequence.length / 2);
            sequence.splice(middle, 0, `-${moves}a`);
            sequence.splice(middle, 0, `-${moves}a`);
            console.log('Invalid input! Adding additional elements to the board');
        } else if (sequence[firstIndex] == sequence[secondIndex]) {
            console.log(`Congrats! You have found matching elements - ${sequence[firstIndex]}!`);
            sequence = sequence.filter(x => x != sequence[firstIndex]);
        } else if (sequence[firstIndex] != sequence[secondIndex]) {
            console.log("Try again!");
        }
    }
    
    if (sequence.length > 0 && win == false) {
        console.log('Sorry you lose :(');
        console.log(sequence.join(' '));
    }
}
