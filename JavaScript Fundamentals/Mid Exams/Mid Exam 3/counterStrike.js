function solve(arr) {
    let energy = Number(arr.shift());
    let wins = 0;
    let lose = false;

    for (let el of arr) {
        if (el == "End of battle") break;
        if (wins % 3 == 0 && wins != 0) energy += wins;
        if (Number(el) <= energy) {
            energy -= Number(el);
            wins++;
        } else {
            lose = true;
            break;
        }
    }
    if (lose) {
        console.log(`Not enough energy! Game ends with ${wins} won battles and ${energy} energy`);
    } else {
        console.log(`Won battles: ${wins}. Energy left: ${energy}`);
    }
}
