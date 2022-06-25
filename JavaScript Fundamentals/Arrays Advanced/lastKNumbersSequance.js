function solve(x, y) {
    let n = x;
    let k = y;
    let result = [1];
    let index = 1;

    for (let i = 1; i < n; i++) {
        let currentIndex = index - 1;
        let sumPreviousElements = 0;
        for (let j = 1; j <= k; j++) {
            sumPreviousElements += result[currentIndex];
            currentIndex--;
            if (currentIndex == -1) break;
        }
        index++;
        result.push(sumPreviousElements);
    }
    console.log(result.join(' '));
}
