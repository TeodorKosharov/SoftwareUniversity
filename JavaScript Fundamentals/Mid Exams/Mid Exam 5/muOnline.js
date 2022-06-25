function solve(string) {
    let arr = string.split('|');
    let health = 100;
    let bitcoins = 0;
    let rooms = 0;
    let lose = false;

    for (let element of arr) {
        rooms++;
        let tokens = element.split(' ');
        if (tokens[0] == 'potion') {
            let hp = Number(tokens[1]);
            let healed = 0;
            if ((health + hp) <= 100) healed = hp;
            else healed = 100 - health;
            health += healed;
            console.log(`You healed for ${healed} hp.`);
            console.log(`Current health: ${health} hp.`);
        } else if (tokens[0] == 'chest') {
            console.log(`You found ${tokens[1]} bitcoins.`);
            bitcoins += Number(tokens[1]);
        } else {
            health -= Number(tokens[1]);
            if (health > 0) console.log(`You slayed ${tokens[0]}.`);
            else {
                console.log(`You died! Killed by ${tokens[0]}.`);
                console.log(`Best room: ${rooms}`);
                lose = true;
                break;
            }
        }
    }

    if (!lose) {
        console.log("You've made it!");
        console.log(`Bitcoins: ${bitcoins}`);
        console.log(`Health: ${health}`);
    }
}
