function date(year, month, day) {
    day++;
    if (day > 30) {
        day = 1;
        month++;
        if (month > 12) {
            month = 1;
            year++;
        }
    }
    console.log(`${year}-${month}-${day}`); 
}
