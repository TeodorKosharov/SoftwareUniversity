function theatre(day, age) {
    let price;
    if (day == "Weekday") {
        if ((0 <= age && age <= 18) || (64 < age && age <= 122)) {
            price = 12;
        } else if (18 < age && age <= 64) {
            price = 18; 
        } else {
            price = "Error!";
        }
    } else if (day == "Weekend") {
        if ((0 <= age && age <= 18) || (64 < age && age <= 122)) {
            price = 15;
        } else if (18 < age && age <= 64) {
            price = 20;
        } else {
            price = "Error!";
        }
    } else {
        if (0 <= age && age <= 18) {
            price = 5;
        } else if (18 < age && age <= 64) {
            price = 12;
        } else if (64 < age && age <= 122) {
            price = 10;
        } else {    
            price = "Error!";
        }
    }
    console.log(price != "Error!" ? price + "$" : "Error!");
}
