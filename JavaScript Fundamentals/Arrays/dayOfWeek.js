function solve(day) {
    let days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'];
    days[day - 1] != undefined ? console.log(days[day - 1]) : console.log('Invalid day!');
}