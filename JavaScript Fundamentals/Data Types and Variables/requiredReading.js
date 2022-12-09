function reading(bookPages, redPagesPerHour, mustReadDays) {
    let hours = bookPages / redPagesPerHour;
    let result = hours / mustReadDays;
    console.log(result);
}