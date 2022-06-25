function solve(arr) {
    let waitingPeople = Number(arr.shift());
    let wagon = arr.join(' ').split(' ').map(x => Number(x));
    let firstCase = false;
    let secondCase = false;
    let freeSpace = 0;
    
    for (let place of wagon) {
        freeSpace += 4 - place;
    }
    
    for (let index = 0; index < wagon.length; index++) {
        while (wagon[index] < 4 && waitingPeople > 0) {
            waitingPeople--;
            wagon[index]++
            freeSpace--;
        }

        if (waitingPeople == 0 && freeSpace > 0) {
            firstCase  = true;
            break;
        } else if (waitingPeople > 0 && freeSpace == 0) {
            secondCase = true;
            break;
        } else if (waitingPeople == 0 && freeSpace == 0) {
            break;
        }
    }

    if (firstCase) {
        console.log('The lift has empty spots!');
    } else if (secondCase) {
        console.log(`There isn't enough space! ${waitingPeople} people in a queue!`);
    } 
    console.log(wagon.join(' '));
}
