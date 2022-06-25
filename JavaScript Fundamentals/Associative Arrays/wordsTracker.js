function solve(arr) {
    let searchWords = arr.shift().split(' ');
    let occurrences = {};

    for (let word of searchWords) occurrences[word] = 0;

    for (let el of arr) {
        if (occurrences.hasOwnProperty(el)) occurrences[el]++;
    }

    for (let [word, occurrence] of Object.entries(occurrences).sort((a, b) => b[1] - a[1])) {
        console.log(`${word} - ${occurrence}`);
    }
}
