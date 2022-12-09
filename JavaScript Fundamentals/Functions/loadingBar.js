function solve(num) {
    if (num == 100) console.log('100% Complete!');
    else {
        let percentCounter = num / 10;
        let dotCounter = 10 - percentCounter;
        let result = '['

        for (let i = 1; i <= percentCounter; i++) result += '%';
        for (let i = 1; i <= dotCounter; i++) result += '.';
        result += ']';
        console.log(`${num}% ${result}`);
        console.log('Still loading...');
    }
}
