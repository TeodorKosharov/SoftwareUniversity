function solve(arr) {
    let mostSequenceEl = 0;
    let bestOccurrences = 0;
    let uniqueElements = [];

    for (let el of arr) {
        if (!(uniqueElements.includes(el))) {
            uniqueElements.push(el);
        }
    }

    for (let uniqElIndex = 0; uniqElIndex < uniqueElements.length; uniqElIndex++) {
        let currentUniqueEl = uniqueElements[uniqElIndex];
        let occurrences = 0;
        
        for (let index = 0; index < arr.length; index++) {
            arr[index] == currentUniqueEl ? occurrences++ : occurrences = 0;

            if (occurrences > bestOccurrences) {
                bestOccurrences = occurrences;
                mostSequenceEl = currentUniqueEl;
            }
        }
    }

    let result = ''
    for (let i = 1; i <= bestOccurrences; i++) {
        result += String(mostSequenceEl) + ' ';
    }
    
    console.log(result);
}
