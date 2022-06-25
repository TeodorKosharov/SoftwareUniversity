function solve() {
    const text = document.getElementById('text').value.split(' ');
    const convention = document.getElementById('naming-convention').value;
    const resultField = document.getElementById('result');
    let result = '';

    if (convention === 'Pascal Case' || convention === 'Camel Case') {
        for (const el of text) {
            for (let index = 0; index < el.length; index++) {
                if (index === 0) result += el[index].toUpperCase();
                else result += el[index].toLowerCase();
            }
        }
        if (convention === 'Camel Case') result = result[0].toLowerCase() + result.slice(1);
    } else {
        result = 'Error!';
    }

    resultField.textContent = result;
}
