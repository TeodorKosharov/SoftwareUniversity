function solve(arr) {
    let pirateship = arr.shift().split('>').map(x => Number(x));
    let warship = arr.shift().split('>').map(x => Number(x));
    let maxHp = Number(arr.shift());
    let stalemate = true;

    for (let el of arr) {
        if (el == 'Retire') break;
        let tokens = el.split(' ');
        if (tokens[0] == 'Fire') {
            let index = Number(tokens[1]);
            let damage = Number(tokens[2]);
            if (index >= 0 && index < warship.length) {
                warship[index] -= damage;
                if (warship[index] <= 0) {
                    console.log("You won! The enemy ship has sunken.");
                    stalemate = false;
                    break;
                }
            }
        } else if (tokens[0] == 'Defend') {
            let startIndex = Number(tokens[1]);
            let endIndex = Number(tokens[2]);
            let damage = Number(tokens[3]);
            let areIndicesValid = true;
            for (let checkIndex = startIndex; checkIndex <= endIndex; checkIndex++) {
                if (!(checkIndex >= 0 && checkIndex < pirateship.length)) {
                    areIndicesValid = false;
                    break;
                }
            }

            if (areIndicesValid) {
                for (let attackIndex = startIndex; attackIndex <= endIndex; attackIndex++) {
                    if (attackIndex >= 0 && attackIndex < pirateship.length) {
                        pirateship[attackIndex] -= damage;
                        if (pirateship[attackIndex] <= 0) {
                            console.log("You lost! The pirate ship has sunken.");
                            stalemate = false;
                            break;
                        }
                    }
                }
            }

        } else if (tokens[0] == 'Repair') {
            let index = Number(tokens[1]);
            let health = Number(tokens[2]);
            if (index >= 0 && index < pirateship.length) {
                pirateship[index] += health;
                if (pirateship[index] > maxHp) pirateship[index] = maxHp;
            }


        } else if (tokens[0] == 'Status') {
            let count = 0;
            for (let section of pirateship) {
                if (section < 0.20 * maxHp) count++;
            }
            console.log(`${count} sections need repair.`);
        }
    }
    if (stalemate) {
        let pirateSum = 0;
        let warSum = 0;
        for (i of pirateship) pirateSum += i;
        for (j of warship) warSum += j;

        console.log(`Pirate ship status: ${pirateSum}`);
        console.log(`Warship status: ${warSum}`);
    }
}
