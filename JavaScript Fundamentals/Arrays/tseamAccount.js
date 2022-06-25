function solve(arr) {
    let games = arr[0].split(' ');

    for (let index = 1; index < arr.length; index++) {
        let tokens = arr[index].split(' ');
        if (tokens[0] == 'Play!') break;

        if (tokens[0] == 'Install') {
            if (!(games.includes(tokens[1]))) games.push(tokens[1]);
        } else if (tokens[0] == 'Uninstall') {
            if (games.includes(tokens[1])) games.splice(games.indexOf(tokens[1]), 1);
        } else if (tokens[0] == 'Update') {
            if (games.includes(tokens[1])) {
                games.splice(games.indexOf(tokens[1]), 1);
                games.push(tokens[1]);
            }
        } else {
            let gameExpansion = tokens[1].split('-');
            if (games.includes(gameExpansion[0])) {
                let game = `${gameExpansion[0]}:${gameExpansion[1]}`;
                games.splice(games.indexOf(gameExpansion[0]) + 1, 0, game);
            }
        }
    }
    console.log(games.join(' '));
}
