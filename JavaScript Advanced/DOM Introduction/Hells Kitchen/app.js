function solve() {
    document.querySelector('#btnSend').addEventListener('click', onClick);
    const area = document.getElementsByTagName('textarea')[0];
    const bestRestaurantArea = document.getElementById('bestRestaurant').children[2];
    const bestWorkersArea = document.getElementById('workers').children[2];
    let restaurants = {};

    function onClick() {
        const info = JSON.parse(area.value);
        let bestRestaurant = {};
        let bestAvgSalary = 0;

        for (const el of info) {
            const tokens = el.split(' - ');
            const restaurantName = tokens[0];
            const workers = tokens.slice(1)[0].split(', ');

            if (!(restaurants.hasOwnProperty(restaurantName))) restaurants[restaurantName] = {};

            for (const el of workers) {
                const [worker, salary] = el.split(' ');
                restaurants[restaurantName][worker] = Number(salary);
            }
        }

        for (const currentRestaurant in restaurants) {
            let totalSalary = 0;
            const totalWorkers = Object.keys(restaurants[currentRestaurant]).length;

            for (const currentWorker in restaurants[currentRestaurant]) {
                totalSalary += restaurants[currentRestaurant][currentWorker];
            }

            const currentAvgSalary = totalSalary / totalWorkers;
            if (currentAvgSalary > bestAvgSalary) {
                bestAvgSalary = currentAvgSalary;
                bestRestaurant = {
                    name: currentRestaurant,
                    avgSalary: bestAvgSalary,
                    bestSalary: Math.max(...Object.values(restaurants[currentRestaurant])),
                    workers: restaurants[currentRestaurant]
                }
            }

        }
        const {name, avgSalary, bestSalary} = bestRestaurant;
        bestRestaurantArea.textContent = `Name: ${name} Average Salary: ${avgSalary.toFixed(2)} Best Salary: ${bestSalary.toFixed(2)}`;

        const sortedWorkers = Object.entries(bestRestaurant['workers']).sort((a, b) => b[1] - a[1]);
        for (const [name, salary] of sortedWorkers) {
            bestWorkersArea.textContent += `Name: ${name} With Salary: ${salary} `;
        }
    }
}
