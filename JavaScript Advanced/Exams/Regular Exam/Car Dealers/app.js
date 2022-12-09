window.addEventListener("load", solve);

function solve() {

    const makeField = document.getElementById('make');
    const modelField = document.getElementById('model');
    const yearField = document.getElementById('year');
    const fuelField = document.getElementById('fuel');
    const originalPriceField = document.getElementById('original-cost');
    const sellingPriceField = document.getElementById('selling-price');
    const publishButton = document.getElementById('publish');
    const tableBody = document.getElementById('table-body');
    const soldCarsList = document.getElementById('cars-list');
    const profitField = document.getElementById('profit');
    publishButton.addEventListener('click', publishing);

    function publishing(event) {
        event.preventDefault();
        // console.log(fuelField.options[fuelField.selectedIndex].value);

        if (makeField.value !== '' && modelField.value !== '' && yearField.value !== '' && fuelField.options[fuelField.selectedIndex].value !== '' && Number(sellingPriceField.value) > Number(originalPriceField.value)) {
            const newTableRow = document.createElement('tr');
            newTableRow.className = 'row';
            newTableRow.innerHTML = `
            <td>${makeField.value}</td>
            <td>${modelField.value}</td>
            <td>${yearField.value}</td>
            <td>${fuelField.options[fuelField.selectedIndex].value}</td>
            <td>${originalPriceField.value}</td>
            <td>${sellingPriceField.value}</td>
            <td>
                <button class="action-btn edit">Edit</button>
                <button class="action-btn sell">Sell</button>
            </td>
            `;
            tableBody.appendChild(newTableRow);
            const [editButton, sellButton] = Array.from(newTableRow.querySelectorAll('button'));
            editButton.addEventListener('click', editing);
            sellButton.addEventListener('click', selling);

        }

        makeField.value = '';
        modelField.value = '';
        yearField.value = '';
        originalPriceField.value = '';
        sellingPriceField.value = '';
    }

    function editing(event) {
        const currentRow = event.target.parentElement.parentElement;
        const rowElements = Array.from(currentRow.children);
        makeField.value = rowElements[0].textContent;
        modelField.value = rowElements[1].textContent;
        yearField.value = rowElements[2].textContent;
        originalPriceField.value = rowElements[4].textContent;
        sellingPriceField.value = rowElements[5].textContent;
        currentRow.remove();
    }

    function selling(event) {
        const currentRow = event.target.parentElement.parentElement;
        const rowElements = Array.from(currentRow.children);
        const newLi = document.createElement('li');
        newLi.className = 'each-list';
        newLi.innerHTML = `
        <span>${rowElements[0].textContent} ${rowElements[1].textContent}</span>
        <span>${rowElements[2].textContent}</span>
        <span>${Number(rowElements[5].textContent) - Number(rowElements[4].textContent)}</span>
        `;
        soldCarsList.appendChild(newLi);
        currentRow.remove();
        profitField.textContent = ((Number(profitField.textContent) + (Number(rowElements[5].textContent) - Number(rowElements[4].textContent))).toFixed(2)).toString();
    }
}
