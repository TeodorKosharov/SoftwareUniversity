function solve(arr) {
    let loot = arr.shift().split('|');
    for (let el of arr) {
        if (el == 'Yohoho!') break;

        let tokens = el.split(' ');
        if (tokens[0] == 'Loot') {
            for (let index = 1; index < tokens.length; index++) {
                if (!(loot.includes(tokens[index]))) loot.splice(0, 0, tokens[index]);
            }
        } else if (tokens[0] == 'Drop') {
            let index = Number(tokens[1]);
            if (index >= 0 && index < loot.length) {
                let removedItem = loot.splice(index, 1);
                loot.push(removedItem);
            }
        } else if (tokens[0] == 'Steal') {
            let count = Number(tokens[1]);
            let stolenItems = [];
            for (let i = 1; i <= count; i++) {
                if (loot.length > 0) stolenItems.push(loot.pop());
            }
            console.log(stolenItems.reverse().join(', '));
        }
    }
    if (loot.length == 0) console.log('Failed treasure hunt.');
    else {
        let totalLength = 0;
        for (let item of loot) {
            totalLength += item.length;
        }
        console.log(`Average treasure gain: ${(totalLength / loot.length).toFixed(2)} pirate credits.`);
    }
}
