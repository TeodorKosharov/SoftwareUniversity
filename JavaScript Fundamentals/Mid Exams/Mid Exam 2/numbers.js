function solve(string) {
    let numbers = string.split(' ').map(x => Number(x));
    let sum = 0;
    for (let num of numbers) {
        sum += num;
    }
    let average = sum / numbers.length;
    let topNumbers = [];
    for (let num of numbers) {
        if (num > average) topNumbers.push(num);
    }
    topNumbers.sort((a, b) => b-a);
    topNumbers = topNumbers.slice(0, 5);
    topNumbers.length > 0 ? console.log(topNumbers.join(' ')) : console.log('No');
}