class VegetableStore {
    constructor(owner, location) {
        this.owner = owner;
        this.location = location;
        this.availableProducts = [];
    }

    loadingVegetables(vegetables) {
        let addedVegetables = new Set();
        for (const el of vegetables) {
            let [vegetable, quantity, price] = el.split(' ');
            addedVegetables.add(vegetable);
            const currentProduct = {
                type: vegetable, quantity: Number(quantity), price: Number(price)
            };

            if (this.availableProducts.map(x => x.type).includes(currentProduct.type)) {
                for (const product of this.availableProducts) {
                    if (product.type === currentProduct.type) {
                        product.quantity += currentProduct.quantity;
                        if (currentProduct.price > product.price) product.price = currentProduct.price;
                    }
                }
            } else this.availableProducts.push(currentProduct);
        }
        return `Successfully added ${Array.from(addedVegetables).join(', ')}`;
    }

    buyingVegetables(selectedProducts) {
        let totalPrice = 0.00;

        for (const el of selectedProducts) {
            let [type, quantity] = el.split(' ');

            if (!((this.availableProducts.map(x => x.type)).includes(type))) {
                throw Error(`${type} is not available in the store, your current bill is $${totalPrice.toFixed(2)}.`);
            }

            const selected = this.availableProducts.filter(x => x.type === type)[0];

            if (selected.quantity < quantity) {
                throw Error(`The quantity ${quantity} for the vegetable ${type} is not available in the store, your current bill is $${totalPrice.toFixed(2)}.`);
            }

            totalPrice += selected.price * quantity;
            selected.quantity -= quantity;
        }
        return `Great choice! You must pay the following amount $${totalPrice.toFixed(2)}.`;
    }

    rottingVegetable(type, quantity) {

        if (!(this.availableProducts.map(x => x.type).includes(type))) {
            throw Error(`${type} is not available in the store.`);
        }

        const selected = this.availableProducts.filter(x => x.type === type)[0];

        if (quantity > selected.quantity) {
            selected.quantity = 0;
            return `The entire quantity of the ${type} has been removed.`;
        }

        selected.quantity -= quantity;
        return `Some quantity of the ${type} has been removed.`;
    }

    revision() {
        let result = 'Available vegetables:';
        for (const product of this.availableProducts.sort((a, b) => a.price - b.price)) {
            result += `\n${product.type}-${product.quantity}-$${product.price}`;
        }

        return result + `\nThe owner of the store is ${this.owner}, and the location is ${this.location}.`;
    }
}
