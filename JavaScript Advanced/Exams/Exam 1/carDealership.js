class CarDealership {
    constructor(name) {
        this.name = name;
        this.availableCars = [];
        this.soldCars = [];
        this.totalIncome = 0;
    }

    addCar(model, horsepower, price, mileage) {
        if (model === '' || horsepower < 0 || price < 0 || mileage < 0) throw Error('Invalid input!');
        this.availableCars.push({
            model, horsepower, price, mileage
        });

        return `New car added: ${model} - ${horsepower} HP - ${mileage.toFixed(2)} km - ${price.toFixed(2)}$`;
    }

    sellCar(model, desiredMileage) {
        if (!(this.availableCars.map(x => x.model).includes(model))) throw Error(`${model} was not found!`);

        const foundCar = this.availableCars.filter(x => x.model === model)[0];

        if (!(foundCar.mileage <= desiredMileage)) {
            if (Math.abs(foundCar.mileage - desiredMileage) <= 40000) {
                foundCar.price -= 0.05 * foundCar.price;
            } else if (Math.abs(foundCar.mileage - desiredMileage) > 40000) {
                foundCar.price -= 0.10 * foundCar.price;
            }
            this.availableCars.splice(this.availableCars.indexOf(foundCar), 1);
        }
        this.soldCars.push({
            model, horsepower: foundCar.horsepower, price: foundCar.price
        });
        this.totalIncome += foundCar.price;
        return `${model} was sold for ${foundCar.price.toFixed(2)}$`;

    }

    currentCar() {
        if (this.availableCars.length === 0) return "There are no available cars";
        let result = '-Available cars:';
        this.availableCars.forEach(car => result += `\n---${car.model} - ${car.horsepower} HP - ${car.mileage.toFixed(2)} km - ${car.price.toFixed(2)}$`);
        return result;
    }

    salesReport(criteria) {
        if (criteria !== 'horsepower' && criteria !== 'model') throw Error('Invalid criteria!');
        else if (criteria === 'horsepower') this.soldCars.sort((a, b) => b.horsepower - a.horsepower);
        else if (criteria === 'model') this.soldCars.sort((a, b) => a.model.localeCompare(b.model));
        let result = `-${this.name} has a total income of ${this.totalIncome.toFixed(2)}$\n-${this.soldCars.length} cars sold:`;
        this.soldCars.forEach(car => result += `\n---${car.model} - ${car.horsepower} HP - ${car.price.toFixed(2)}$`);
        return result;
    }
}
