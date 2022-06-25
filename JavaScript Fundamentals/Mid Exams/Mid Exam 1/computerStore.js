function solve(arr) {
    let discount = false;
    let totalPrice = 0;
    let taxes = 0;
    let priceWithoutTaxes = 0;

    for (let el of arr) {
        if (el == 'regular') break;
        else if (el == 'special') discount = true;
        else if (Number(el) < 0) console.log("Invalid price!");
        else {
        totalPrice += Number(el);
        taxes += 0.20 * Number(el);
        }
    }    
    priceWithoutTaxes = totalPrice;
    totalPrice += taxes;
    if (discount) totalPrice -= 0.10 * totalPrice;
    if (totalPrice == 0) console.log("Invalid order!");
    else {
        console.log("Congratulations you've just bought a new computer!");
        console.log(`Price without taxes: ${priceWithoutTaxes.toFixed(2)}$`);
        console.log(`Taxes: ${taxes.toFixed(2)}$`);
        console.log('-----------');
        console.log(`Total price: ${totalPrice.toFixed(2)}$`);
    }
}
