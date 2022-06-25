function solve(arr) {
    let houses = arr.shift().split('@').map(x => Number(x));
    let currentIndex = 0;

    for (let command of arr) {
        if (command == 'Love!') break;
        let tokens = command.split(' ');
        if (tokens[0] == 'Jump') {
            let length = Number(tokens[1]);
            let jumpIndex = currentIndex + length;
            if (jumpIndex > houses.length - 1) currentIndex = 0;
            else currentIndex = jumpIndex;

            if (houses[currentIndex] == 0) console.log(`Place ${currentIndex} already had Valentine's day.`);
            else {
                houses[currentIndex] -= 2;
                if (houses[currentIndex] == 0) console.log(`Place ${currentIndex} has Valentine's day.`);
            }
        }
    }
    console.log(`Cupid's last position was ${currentIndex}.`);
    let failedPlaces = 0;
    for (let house of houses) {
        if (house != 0) failedPlaces++;
    }
    if (failedPlaces > 0) console.log(`Cupid has failed ${failedPlaces} places.`);
    else console.log("Mission was successful.");
}
