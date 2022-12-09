function solve(arr) {
    let fieldSize = arr[0];
    let ladybugsPositions = arr[1].split(' ');
    let field = [];

    for (let i = 0; i < fieldSize; i++) {
        if (ladybugsPositions.includes(String(i))) {
            field.push('1');
        } else {
        field.push('0');
        }
    }

    for (let index = 2; index < arr.length; index++) {
        let movingData = arr[index].split(' ');
        let ladyBugIndex = Number(movingData[0]);
        let direction = movingData[1];
        let flyLength = Number(movingData[2]);
        
        if (field[ladyBugIndex] == '1') {
            field[ladyBugIndex] = '0';
            if (direction == 'right') {
                let ladybugArriveIndex = ladyBugIndex + flyLength;
                if (ladybugArriveIndex < field.length) {
                    while(true) {
                        if (field[ladybugArriveIndex] == '0') {
                            field[ladybugArriveIndex] = '1';
                            break;
                        }
                        ladybugArriveIndex += flyLength;
                        if (ladybugArriveIndex >= field.length) break;
                    }
                }
            } else {
                field[ladyBugIndex] = '0';
                let ladybugArriveIndex = ladyBugIndex - flyLength;
                if (ladybugArriveIndex < field.length && ladybugArriveIndex >= 0) {
                    while(true) {
                        if (field[ladybugArriveIndex] == '0') {
                            field[ladybugArriveIndex] = '1';
                            break;
                        }
                        ladybugArriveIndex -= flyLength;
                        if (ladybugArriveIndex < 0) break;
                    }
                }
            }
        }
    }
    console.log(field.join(' '));
}
