function solve(arr) {
    words = {};
    
    for (let el of arr) {
        if (!(Object.keys(words).includes(el))) words[el] = 1;
        else words[el]++;
    }

    for (let occurrencesData of Object.entries(words).sort((a, b) => b[1] - a[1])) {
        console.log(`${occurrencesData[0]} -> ${occurrencesData[1]} times`);
    }

}
