class Restaurant {
    constructor(budgetMoney) {
        this.budgetMoney = budgetMoney;
        this.menu = {};
        this.stockProducts = {};
        this.history = [];
    }

    loadProducts(productsArr) {
        for (const el of productsArr) {
            let [productName, productQuantity, productTotalPrice] = el.split(' ');
            productQuantity = Number(productQuantity);
            productTotalPrice = Number(productTotalPrice);

            if (this.budgetMoney >= productTotalPrice) {
                this.budgetMoney -= productTotalPrice;
                if (!(this.stockProducts.hasOwnProperty(productName))) {
                    this.stockProducts[productName] = productQuantity;
                } else {
                    this.stockProducts[productName] += productQuantity;
                }
                this.history.push(`Successfully loaded ${productQuantity} ${productName}`);
            } else {
                this.history.push(`There was not enough money to load ${productQuantity} ${productName}`);
            }
        }
        return this.history.join('\n');
    }

    addToMenu(meal, neededProducts, price) {
        if (this.menu.hasOwnProperty(meal)) return `The ${meal} is already in the our menu, try something different.`;
        this.menu[meal] = {};
        this.menu[meal].products = neededProducts;
        this.menu[meal].price = price;

        const totalMeals = Object.keys(this.menu).length;
        if (totalMeals === 1) return `Great idea! Now with the ${meal} we have 1 meal in the menu, other ideas?`;
        return `Great idea! Now with the ${meal} we have ${totalMeals} meals in the menu, other ideas?`;
    }

    showTheMenu() {
        if (Object.keys(this.menu).length === 0) return 'Our menu is not ready yet, please come later...';

        let result = '';
        for (const meal in this.menu) {
            result += `${meal} - $ ${this.menu[meal].price}\n`;
        }
        return result.trim();
    }

    makeTheOrder(meal) {
        if (!(this.menu.hasOwnProperty(meal))) return `There is not ${meal} yet in our menu, do you want to order something else?`;
        const selectedMeal = this.menu[meal];
        let areProductsAvailable = true;

        for (const el of selectedMeal.products) {
            let [product, quantity] = el.split(' ');
            if (!(this.stockProducts.hasOwnProperty(product))) {
                areProductsAvailable = false;
                break;
            }
            if (this.stockProducts[product] < quantity) {
                areProductsAvailable = false;
                break;
            }
        }

        if (areProductsAvailable === true) {
            for (const el of selectedMeal.products) {
                let [product, quantity] = el.split(' ');
                if (this.stockProducts.hasOwnProperty(product)) {
                    if (this.stockProducts[product] >= quantity) {
                        this.stockProducts[product] -= quantity;
                    }
                }
            }
        } else {
            return `For the time being, we cannot complete your order (${meal}), we are very sorry...`;
        }
        this.budgetMoney += selectedMeal.price;
        return `Your order (${meal}) will be completed in the next 30 minutes and will cost you ${selectedMeal.price}.`;
    }
}
