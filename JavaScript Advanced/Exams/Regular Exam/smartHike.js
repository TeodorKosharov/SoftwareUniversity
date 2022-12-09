class SmartHike {
    constructor(username) {
        this.username = username;
        this.goals = {};
        this.listOfHikes = [];
        this.resources = 100;
    }

    addGoal(peak, altitude) {
        if (this.goals.hasOwnProperty(peak)) return `${peak} has already been added to your goals`;
        this.goals[peak] = altitude;
        return `You have successfully added a new goal - ${peak}`;
    }

    hike(peak, time, difficultyLevel) {
        if (!(this.goals.hasOwnProperty(peak))) throw Error(`${peak} is not in your current goals`); else if (this.goals.hasOwnProperty(peak) && this.resources === 0) throw Error('You don\'t have enough resources to start the hike');
        const difference = this.resources - 10 * time;

        if (difference < 0) return 'You don\'t have enough resources to complete the hike';
        this.resources -= 10 * time;
        this.listOfHikes.push({peak, time, difficultyLevel});
        return `You hiked ${peak} peak for ${time} hours and you have ${this.resources}% resources left`;
    }

    rest(time) {
        this.resources += 10 * time;
        if (this.resources >= 100) {
            this.resources = 100;
            return `Your resources are fully recharged. Time for hiking!`;
        }
        return `You have rested for ${time} hours and gained ${time * 10}% resources`;
    }

    showRecord(criteria) {
        if (this.listOfHikes.length === 0) return `${this.username} has not done any hiking yet`;
        if (criteria === 'hard') {
            const allHardHikes = this.listOfHikes.filter(hike => hike.difficultyLevel === 'hard');
            if (allHardHikes.length === 0) return `${this.username} has not done any ${criteria} hiking yet`;

            let bestHike;
            let shortestTime = 100000;

            for (const hike of allHardHikes) {
                if (hike.time < shortestTime) {
                    shortestTime = hike.time;
                    bestHike = hike;
                }
            }
            return `${this.username}'s best ${criteria} hike is ${bestHike.peak} peak, for ${bestHike.time} hours`;
        }
        else if (criteria === 'easy') {
            const allEasyHikes = this.listOfHikes.filter(hike => hike.difficultyLevel === 'easy');
            if (allEasyHikes.length === 0) return `${this.username} has not done any ${criteria} hiking yet`;

            let bestHike;
            let shortestTime = 100000;

            for (const hike of allEasyHikes) {
                if (hike.time < shortestTime) {
                    shortestTime = hike.time;
                    bestHike = hike;
                }
            }
            return `${this.username}'s best ${criteria} hike is ${bestHike.peak} peak, for ${bestHike.time} hours`;
        }
        else if (criteria === 'all') {
            let result = 'All hiking records:';
            this.listOfHikes.forEach(hike => result += `\n${this.username} hiked ${hike.peak} for ${hike.time} hours`);
            return result;
        }
    }
}
