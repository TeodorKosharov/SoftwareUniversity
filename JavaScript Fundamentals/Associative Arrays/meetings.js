function solve(arr) {
    let days = {};
    for (let el of arr) {
        let tokens = el.split(' ');
        if (!(Object.keys(days).includes(tokens[0]))) {
            days[tokens[0]] = tokens[1]; 
            console.log(`Scheduled for ${tokens[0]}`);
        } else console.log(`Conflict on ${tokens[0]}!`);
    }

    for (let day in days) console.log(`${day} -> ${days[day]}`);
}
