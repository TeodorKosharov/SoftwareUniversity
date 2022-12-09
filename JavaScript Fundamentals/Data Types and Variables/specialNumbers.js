function special(num) {
    for (let i = 1; i <= num; i++) {
        let sum = 0;
        let isSpecial = 'False';
        for (let index = 0; index < String(i).length; index++) {
            sum += Number(String(i)[index]);
        }
        if (sum == 5 || sum == 7 || sum == 11) isSpecial = 'True';
        console.log(`${i} -> ${isSpecial}`);
    }
}
