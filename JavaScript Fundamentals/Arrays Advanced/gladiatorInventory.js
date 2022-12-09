function solve(arr) {
    let items = arr[0].split(' ');

    for(let index = 1; index < arr.length; index++) {
        let command = arr[index];
        let tokens = command.split(' ');
        if (tokens[0] == 'Buy') {
            if (!(items.includes(tokens[1]))) items.push(tokens[1]);
        } else if (tokens[0] == 'Trash') {
            if (items.includes(tokens[1])) {
                let itemIndex = Number(items.indexOf(tokens[1]));
                items.splice(itemIndex, 1);
            }
        } else if (tokens[0] == 'Repair') {
            if (items.includes(tokens[1])) {
                let itemIndex = Number(items.indexOf(tokens[1]));
                let removedItem = items.splice(itemIndex, 1);
                items.push(removedItem);
            }
        } else if (tokens[0] == 'Upgrade') {
            let miniTokens = tokens[1].split('-');
            let equipment = miniTokens[0];
            if (items.includes(equipment)) {
                let itemIndex = Number(items.indexOf(equipment));
                items.splice(itemIndex + 1, 0, `${equipment}:${miniTokens[1]}`);
            }
        }
    }
    console.log(items.join(' '));
}
