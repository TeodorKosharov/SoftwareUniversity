function solve(string) {
    let elements = string.split(' ');
    let elementsOccurrences = {};
    let result = [];

    for (let element of elements) {
        element = element.toLowerCase();
        if (elementsOccurrences.hasOwnProperty(element)) elementsOccurrences[element]++;
        else elementsOccurrences[element] = 1;
    }

    for (let word in elementsOccurrences) {
        if (elementsOccurrences[word] % 2 == 1) result.push(word);
    }

    console.log(result.join(' '));
}
