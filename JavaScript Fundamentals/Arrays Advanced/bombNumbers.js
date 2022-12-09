function solve(sequence, bombData) {
    function validateIndex(arr, index) {
        return 0 <= index && index <= arr.length - 1;
    }
    
    let bomb = bombData[0];
    let power = bombData[1];
    let bombIndices = [];
    
    for (let i = 0; i < sequence.length; i++) {
        if (sequence[i] == bomb) {
            sequence[i] = 0;
            bombIndices.push(i);
        }
    }

    for (let bombIndex of bombIndices) {
        for (let detonation = 1; detonation <= power; detonation++) {
            if (validateIndex(sequence, bombIndex + detonation)) sequence[bombIndex + detonation] = 0;
            if (validateIndex(sequence, bombIndex - detonation)) sequence[bombIndex - detonation] = 0;
        }
    }
    
    let sum = 0;
    for (element of sequence) sum += element;
    console.log(sum);
}
