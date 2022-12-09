function solve(arr) {
    let names = [];
    for (let element of arr) {
        let tokens = element.split(' ');
        let name = tokens[0];

        if (tokens.includes('not')) {
            if (!(names.includes(name))) console.log(`${name} is not in the list!`);
            else names = names.filter(x => x != name);
        } else {
            if (names.includes(name)) console.log(`${name} is already in the list!`);
            else names.push(name);
        } 
    }
    console.log(names.join('\n'));
}
