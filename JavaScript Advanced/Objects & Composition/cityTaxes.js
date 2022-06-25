function cityTaxes(name, population, treasury) {
    const result = {
        name,
        population,
        treasury,
        taxRate: 10,
        collectTaxes() {
            this.treasury += this.population * this.taxRate;
        },
        applyGrowth(percentage) {
            this.population += percentage / 100 * this.population;
        },
        applyRecession(percentage) {
            this.treasury -= percentage / 100 * this.treasury;
        }
    }
    return result;
}
