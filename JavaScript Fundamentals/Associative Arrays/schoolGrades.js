function solve(arr) {
    let grades = {};

    for (let el of arr) {
        let tokens = el.split(' ');
        if (!(Object.keys(grades).includes(tokens[0]))) grades[tokens[0]] = tokens.slice(1).map(x => Number(x));
        else grades[tokens[0]] = grades[tokens[0]].concat(tokens.slice(1).map(x => Number(x)));
    }

    for (let name in grades) {
        let currentGrades = grades[name];
        let sumOfGrades = 0;
        
        for (let grade of currentGrades) sumOfGrades += grade;
        grades[name] = (sumOfGrades / currentGrades.length).toFixed(2); 
    }

    for (let result of Object.entries(grades).sort((a, b) => a[0].localeCompare(b[0]))) {
        console.log(`${result[0]}: ${result[1]}`);
    }
}
