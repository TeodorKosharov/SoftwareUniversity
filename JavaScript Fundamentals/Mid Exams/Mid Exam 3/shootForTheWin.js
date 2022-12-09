function solve(arr) {
    let sequence = arr.shift().split(' ').map(x => Number(x));
    let shotTargets = 0;
    for (let el of arr) {
        if (el == 'End') break;
        let index = Number(el);
        if (index >= 0 && index < sequence.length) {
            let target = sequence[index];
            if (target != -1) {
                sequence[index] = -1;
                shotTargets++;
            }
            for (let i = 0; i < sequence.length; i++) {
                if (sequence[i] > target && sequence[i] != -1) sequence[i] -= target;
                else if (sequence[i] <= target && sequence[i] != -1) sequence[i] += target;
            }
        }
    }
    console.log(`Shot targets: ${shotTargets} -> ${sequence.join(' ')}`);
}
