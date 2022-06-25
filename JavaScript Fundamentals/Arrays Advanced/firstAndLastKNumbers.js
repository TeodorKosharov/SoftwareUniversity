function solve(arr) {
    let k = arr.shift();
    let firstElements = [];
    let lastElements = [];
    let lastIndex = arr.length - 1;
    
    for (let index = 0; index < k; index++) {
        firstElements.push(arr[index]);
        lastElements.push(arr[lastIndex - k + 1]);
        lastIndex++;
    }

    console.log(firstElements.join(' '));
    console.log(lastElements.join(' '));
}
