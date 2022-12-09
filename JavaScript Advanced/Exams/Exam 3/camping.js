class SummerCamp {
    constructor(organizer, location) {
        this.organizer = organizer;
        this.location = location;
        this.priceForTheCamp = {"child": 150, "student": 300, "collegian": 500};
        this.listOfParticipants = [];
    }

    registerParticipant(name, condition, money) {
        if (this.priceForTheCamp[condition] === undefined) throw Error('Unsuccessful registration at the camp.');
        if (this.listOfParticipants.map(x => x.name).includes(name)) return `The ${name} is already registered at the camp.`;
        if (money < this.priceForTheCamp[condition]) return 'The money is not enough to pay the stay at the camp.';
        this.listOfParticipants.push({name, condition, power: 100, wins: 0});
        return `The ${name} was successfully registered.`;
    }

    unregisterParticipant(name) {
        if (!(this.listOfParticipants.map(x => x.name).includes(name))) throw Error(`The ${name} is not registered in the camp.`);
        const selectedParticipant = this.listOfParticipants.filter(x => x.name === name)[0];
        this.listOfParticipants.splice(this.listOfParticipants.indexOf(selectedParticipant), 1);
        return `The ${name} removed successfully.`;

    }

    timeToPlay(typeOfGame, ...players) {
        for (const player of players) {
            if (!(this.listOfParticipants.map(x => x.name).includes(player))) throw Error('Invalid entered name/s.');
        }

        if (players.length === 2) {
            const firstPlayer = this.listOfParticipants.filter(x => x.name === players[0])[0];
            const secondPlayer = this.listOfParticipants.filter(x => x.name === players[1])[0];
            if (firstPlayer.condition !== secondPlayer.condition) throw Error('Choose players with equal condition.');
        }

        if (typeOfGame === 'Battleship') {
            const player = this.listOfParticipants.filter(x => x.name === players[0])[0];
            player.power += 20;
            return `The ${player.name} successfully completed the game Battleship.`;
        } else if (typeOfGame === 'WaterBalloonFights') {
            const firstPlayer = this.listOfParticipants.filter(x => x.name === players[0])[0];
            const secondPlayer = this.listOfParticipants.filter(x => x.name === players[1])[0];

            if (firstPlayer.power === secondPlayer.power) return 'There is no winner.'; else if (firstPlayer.power > secondPlayer.power) {
                firstPlayer.wins++;
                return `The ${firstPlayer.name} is winner in the game WaterBalloonFights.`;
            } else {
                secondPlayer.wins++;
                return `The ${secondPlayer.name} is winner in the game WaterBalloonFights.`;
            }
        }
    }

    toString() {
        let result = `${this.organizer} will take ${this.listOfParticipants.length} participants on camping to ${this.location}`;
        this.listOfParticipants.sort((a, b) => b.wins - a.wins);
        this.listOfParticipants.forEach(x => result += `\n${x.name} - ${x.condition} - ${x.power} - ${x.wins}`);
        return result;
    }
}
