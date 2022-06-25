function vacation(ppl, group, day) {
    let price = 0;

    if (day == 'Friday') {
        if (group == 'Students') {
            price = 8.45;
        } else if (group == 'Business') {
            price = 10.90;
        } else {
            price = 15;
        }
    } else if (day == 'Saturday') {
        if (group == 'Students') {
            price = 9.80;
        } else if (group == 'Business') {
            price = 15.60;
        } else {
            price = 20;
        }
    } else {
        if (group == 'Students') {
            price = 10.46;
        } else if (group == 'Business') {
            price = 16;
        } else {
            price = 22.50;
        }
    }
    let totalPrice = ppl * price;
    if (group == 'Students' && ppl >= 30) {
        totalPrice -= 0.15 * totalPrice;
    } else if (group == 'Business' && ppl >= 100) {
        totalPrice -= 10 * price;
    } else if (group == 'Regular' && ppl >= 10 && ppl <= 20) {
        totalPrice -= 0.05 * totalPrice;
    }

    console.log(`Total price: ${totalPrice.toFixed(2)}`);
}
