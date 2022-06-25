function solve(arr) {
    let smallestNumIndex = 0;
    let smallestTwoNumbers = [];

    for (let i = 1; i <= 2; i++) {
        let smallest = 1000000;

        for (let index = 0; index < arr.length; index++) {
            if (arr[index] < smallest) {
                smallest = arr[index];
                smallestNumIndex = index;
            }
        }
        smallestTwoNumbers.push(smallest);
        arr.splice(smallestNumIndex, 1);
    }
    console.log(smallestTwoNumbers.join(' '));
}
