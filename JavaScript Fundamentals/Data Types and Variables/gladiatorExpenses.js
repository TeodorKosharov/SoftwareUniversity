function solve(losts, helmetPrice, swordPrice, shieldPrice, armorPrice) {
    let expenses = 0;
    let brokenShields = 0;

    for (let i = 1; i <= losts; i++) {
        if (i % 2 == 0) expenses += helmetPrice;
        if (i % 3 == 0) expenses += swordPrice;
        if (i % 2 == 0 && i % 3 == 0) {
            expenses += shieldPrice;
            brokenShields++;
        }
        if (brokenShields % 2 == 0 && brokenShields != 0)  {
            expenses += armorPrice;
            brokenShields = 0;   
        }
    }
    console.log(`Gladiator expenses: ${expenses.toFixed(2)} aureus`)
}
