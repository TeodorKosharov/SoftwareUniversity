function solve(moves) {
    function isWinner(sign, matrixField) {
        // First row
        if (matrixField[0][0] === sign && matrixField[0][1] === sign && matrixField[0][2] === sign) return true;
        // Second row
        else if (matrixField[1][0] === sign && matrixField[1][1] === sign && matrixField[1][2] === sign) return true;
        // Third row
        else if (matrixField[2][0] === sign && matrixField[2][1] === sign && matrixField[2][2] === sign) return true;
        // First column
        else if (matrixField[0][0] === sign && matrixField[1][0] === sign && matrixField[2][0] === sign) return true;
        // Second column
        else if (matrixField[0][1] === sign && matrixField[1][1] === sign && matrixField[2][1] === sign) return true;
        // Third column
        else if (matrixField[0][2] === sign && matrixField[1][2] === sign && matrixField[2][2] === sign) return true;
        // First diagonal
        else if (matrixField[0][0] === sign && matrixField[1][1] === sign && matrixField[2][2] === sign) return true;
        // Second diagonal
        else if (matrixField[0][2] === sign && matrixField[1][1] === sign && matrixField[2][0] === sign) return true; else return false;
    }

    let field = [[false, false, false], [false, false, false], [false, false, false]]

    let playerCounter = 1;
    let freeSpace = 9;
    let playerSign;

    for (let move of moves) {
        let [moveRow, moveCol] = move.split(' ').map(x => Number(x));
        playerCounter % 2 === 1 ? playerSign = 'X' : playerSign = 'O';

        if (field[moveRow][moveCol] !== false) {
            console.log('This place is already taken. Please choose another!');
            continue;
        }

        field[moveRow][moveCol] = playerSign;
        playerCounter++;
        freeSpace--;
        if (isWinner(playerSign, field)) {
            console.log(`Player ${playerSign} wins!`);
            break;
        }

        if (freeSpace === 0) {
            console.log('The game ended! Nobody wins :(');
            break;
        }
    }
    for (let row of field) console.log(row.join('\t'));
}
