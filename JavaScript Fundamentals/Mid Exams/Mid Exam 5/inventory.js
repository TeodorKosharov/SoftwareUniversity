function solve(arr) {
    let items = arr.shift().split(', ');
    for (let el of arr) {
        if (el == 'Craft!') break;

        let tokens = el.split(' - ');
        if (tokens[0] == 'Collect') {
            if (!(items.includes(tokens[1]))) items.push(tokens[1]);
        }
        else if (tokens[0] == 'Drop') {
             if (items.includes(tokens[1])) items.splice(items.indexOf(tokens[1]), 1);
        }
        else if (tokens[0] == 'Combine Items') {
            let givenItems = tokens[1].split(':');
            if (items.includes(givenItems[0])) items.splice(items.indexOf(givenItems[0]) + 1, 0, givenItems[1]);
        } else {
            if (items.includes(tokens[1])) {
                let removedItem = items.splice(items.indexOf(tokens[1]), 1);
                items.push(removedItem);
            }
        }
    }
    console.log(items.join(', '));
}
