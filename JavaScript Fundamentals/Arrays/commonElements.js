function solve(arr1, arr2) {
    let occurrences = [];

    for (let index = 0; index < arr1.length; index++) {
        for (let idx = 0; idx < arr2.length; idx++) {
            if (arr1[index] === arr2[idx]) {
                if (!(occurrences.includes(arr1[index]))) {
                    console.log(arr1[index]);
                }
                occurrences.push(arr1[index]);
             }
        }
    }
}
