class Garden {
    constructor(spaceAvailable) {
        this.spaceAvailable = spaceAvailable;
        this.plants = [];
        this.storage = [];
    }

    addPlant(plantName, spaceRequired) {
        if (this.spaceAvailable < spaceRequired) throw Error("Not enough space in the garden.");

        this.plants.push({
            plantName, spaceRequired, ripe: false, quantity: 0
        });
        this.spaceAvailable -= spaceRequired;
        return `The ${plantName} has been successfully planted in the garden.`;
    }

    ripenPlant(plantName, quantity) {
        if (!(this.plants.map(x => x.plantName).includes(plantName))) throw Error(`There is no ${plantName} in the garden.`);
        const plant = this.plants.filter(x => x.plantName === plantName)[0];

        if (plant.ripe === true) throw Error(`The ${plantName} is already ripe.`);
        if (quantity <= 0) throw Error("The quantity cannot be zero or negative.");
        plant.ripe = true;
        plant.quantity += quantity;

        if (quantity === 1) return `${quantity} ${plantName} has successfully ripened.`;
        if (quantity > 1) return `${quantity} ${plantName}s have successfully ripened.`;
    }

    harvestPlant(plantName) {
        if (!(this.plants.map(x => x.plantName).includes(plantName))) throw Error(`There is no ${plantName} in the garden.`);
        const plant = this.plants.filter(x => x.plantName === plantName)[0];
        if (plant.ripe === false) throw Error(`The ${plantName} cannot be harvested before it is ripe.`);
        this.plants = this.plants.filter(x => x.plantName !== plantName);
        this.storage.push({plantName: plant.plantName, quantity: plant.quantity});
        this.spaceAvailable += plant.spaceRequired;
        return `The ${plantName} has been successfully harvested.`;
    }

    generateReport() {
        const sortedPlants = (this.plants.map(x => x.plantName)).sort((a, b) => a.localeCompare(b));
        let result = `The garden has ${this.spaceAvailable} free space left.\n`;
        result += `Plants in the garden: ${sortedPlants.join(', ')}\n`;

        if (this.storage.length === 0) {
            result += "Plants in storage: The storage is empty.";
        } else {
            result += `Plants in storage: `;
            for (const plant of this.storage) {
                result += `${plant.plantName} (${plant.quantity}), `;
            }
        }
        return result.slice(0, result.length - 2);
    }

}
