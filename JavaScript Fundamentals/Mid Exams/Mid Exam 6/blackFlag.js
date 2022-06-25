function solve(arr) {
    let plunderDays = Number(arr[0]);
    let dailyPlunder = Number(arr[1]);
    let expectedPlunder = Number(arr[2]);
    let total = 0;

    for (let day = 1; day <= plunderDays; day++) {
        total += dailyPlunder;
        if (day % 3 == 0) total += 0.50 * dailyPlunder;
        if (day % 5 == 0) total -= 0.30 * total;
    }
    if (total >= expectedPlunder) console.log(`Ahoy! ${total.toFixed(2)} plunder gained.`);
    else console.log(`Collected only ${(total / expectedPlunder * 100).toFixed(2)}% of the plunder.`);
}
