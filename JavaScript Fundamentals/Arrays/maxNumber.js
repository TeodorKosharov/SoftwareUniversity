function solve(arr) {
    let topIntegers = [];
    for (let index = 0; index < arr.length; index++) {
        let isBigger = false;
        for (let subIndex = index + 1; subIndex < arr.length; subIndex++) {
            if (arr[index] > arr[subIndex]) {
                isBigger = true;
            } else {
                isBigger = false;
                break;
            }
        }
        if (isBigger) {
            topIntegers.push(arr[index]);
        }
    }
    topIntegers.push(arr[arr.length - 1]);
    console.log(topIntegers.join(' '));
}
