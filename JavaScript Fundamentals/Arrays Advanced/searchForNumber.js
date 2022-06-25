function solve(arr, data) {
    let firstElements = data[0];
    let deleteElements = data[1];
    let searchNumber = data[2];
    let occurrences = 0;

    arr = arr.slice(0, firstElements);
    arr = arr.slice(0 + deleteElements);
    for (let element of arr) if (element == searchNumber) occurrences++;
    console.log(`Number ${searchNumber} occurs ${occurrences} times.`);

}
