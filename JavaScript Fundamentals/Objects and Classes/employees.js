function solve(arr) {
    let people = {};
    for (let el of arr) {
        people[el] = el.length;
    }

    for (person of Object.keys(people)) {
        console.log(`Name: ${person} -- Personal Number: ${people[person]}`);
    }
}
