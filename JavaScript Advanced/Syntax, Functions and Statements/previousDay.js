function solve(year, month, day) {
    let date = new Date(year, month, day);
    let previous = new Date(date.getTime());
    previous.setDate(date.getDate() - 1);
    console.log(previous.getFullYear() + '-' + previous.getMonth() + '-' + previous.getDate());
}
