function solve(arr) {
    let uniqueElements = [];

    for (let element of arr) {
        if (!(uniqueElements.includes(element))) uniqueElements.push(element);
    }
    console.log(uniqueElements.join(' '));
}