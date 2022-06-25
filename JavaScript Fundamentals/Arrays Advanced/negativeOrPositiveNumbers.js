function solve(arr) {
    let newArr = [];
    for (let element of arr) {
        element >= 0 ? newArr.push(element) : newArr.unshift(element);
    }

    console.log(newArr.join('\n'));
}