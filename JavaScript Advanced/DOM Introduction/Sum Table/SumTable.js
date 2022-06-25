function sumTable() {
    const elements = document.querySelectorAll('td');
    let sum = 0;
    for (let index = 1; index < elements.length - 1; index+=2) {
        sum += Number(elements[index].textContent);
    }
    document.getElementById('sum').textContent = String(sum);
}
