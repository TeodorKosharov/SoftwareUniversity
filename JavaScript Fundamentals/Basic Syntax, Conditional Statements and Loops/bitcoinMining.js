function mining(gold) {
    let balance = 0;
    let dayCounter = 1;
    let firstDay = 0;
    let boughtBitcoins = 0;

    for (let index = 0; index < gold.length; index++) {
        if (dayCounter % 3 == 0) {
            gold[index] -= gold[index] * 0.30;
        }

        balance += gold[index] * 67.51;
        if (balance >= 11949.16) {
            if(firstDay == 0) {
                firstDay = dayCounter;
            }
            boughtBitcoins += Math.floor(balance / 11949.16);
            balance -= Math.floor(balance / 11949.16) * 11949.16;
        }
        dayCounter++;
    }
    console.log(`Bought bitcoins: ${boughtBitcoins}`);
    if (firstDay != 0) {
        console.log(`Day of the first purchased bitcoin: ${firstDay}`);
    }
    console.log(`Left money: ${balance.toFixed(2)} lv.`)
}