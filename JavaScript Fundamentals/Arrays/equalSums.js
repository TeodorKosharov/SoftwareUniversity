function solve(arr) {
    let resultIndex = 'no';
    for (let index = 0; index < arr.length; index++) {
        let currentElement = arr[index];
        let leftSum = 0;
        let rightSum = 0;

        for (let leftIndex = index - 1; leftIndex >= 0; leftIndex--) {
            leftSum += arr[leftIndex];
        }

        for (let rightIndex = index + 1; rightIndex < arr.length; rightIndex++) {
            rightSum += arr[rightIndex];
        }

        if (leftSum == rightSum) {
            resultIndex = index;
            break;
        }
    }

    arr.length == 1 ? console.log(0) : console.log(resultIndex);
}
