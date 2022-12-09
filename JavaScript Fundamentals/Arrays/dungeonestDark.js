function solve(arr) {
    let rooms = arr.join().split('|');
    let hp = 100;
    let coins = 0;
    let roomCounter = 0;


    for (let room of rooms) {
        roomCounter++;
        let currentRoom = room.split(' ');
        currentRoom[1] = Number(currentRoom[1]);

        if (currentRoom[0] == 'potion') {
            let healed = 0;
            if (hp + currentRoom[1] <= 100) healed = currentRoom[1];  
            else {
                healed = 100 - hp;
            }
            hp += healed;
            console.log(`You healed for ${healed} hp.`);
            console.log(`Current health: ${hp} hp.`);
        } else if (currentRoom[0] == 'chest') {
            console.log(`You found ${currentRoom[1]} coins.`);
            coins += currentRoom[1];
        } else {
            hp -= currentRoom[1];
            if (hp > 0) {
                console.log(`You slayed ${currentRoom[0]}.`);
            } else {
                console.log(`You died! Killed by ${currentRoom[0]}.`);
                console.log(`Best room: ${roomCounter}`);
                break;
            }
        }
    }
    if (hp > 0) {
        console.log("You've made it!");
        console.log(`Coins: ${coins}`);
        console.log(`Health: ${hp}`);
    }
}
