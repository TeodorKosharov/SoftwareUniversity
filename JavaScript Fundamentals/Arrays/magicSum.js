function solve(arr, sum) {

    for (let index = 0; index < arr.length; index++) {
        for (let innerIndex = index + 1; innerIndex < arr.length; innerIndex++) {
            
            if ((arr[index] + arr[innerIndex]) == sum) {
                console.log(`${arr[index]} ${arr[innerIndex]}`);
            }
        }
    }
}
