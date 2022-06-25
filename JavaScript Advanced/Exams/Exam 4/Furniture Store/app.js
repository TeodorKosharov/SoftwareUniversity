window.addEventListener('load', solve);

function solve() {
    const modelField = document.getElementById('model');
    const yearField = document.getElementById('year');
    const descriptionField = document.getElementById('description');
    const priceField = document.getElementById('price');
    const addButton = document.getElementById('add');
    const tableBody = document.getElementById('furniture-list');
    const totalPriceField = document.querySelector('.total-price');
    addButton.addEventListener('click', adding);

    function adding(event) {
        event.preventDefault();
        if (modelField.value !== '' && descriptionField.value !== '' && yearField.value >= 0 && priceField.value >= 0) {
            const infoRow = document.createElement('tr');
            const additionalRow = document.createElement('tr');
            infoRow.className = 'info';
            additionalRow.className = 'hide';

            infoRow.innerHTML = `
            <td>${modelField.value}</td>
            <td>${Number(priceField.value).toFixed(2)}</td>
            <td>
                <button class="moreBtn">More Info</button>
                <button class="buyBtn">Buy it</button>
            </td>`;

            additionalRow.innerHTML = `
            <td>Year: ${yearField.value}</td>
            <td colspan="3">Description: ${descriptionField.value}</td>`;

            tableBody.appendChild(infoRow);
            tableBody.appendChild(additionalRow);

            const [moreButton, buyButton] = Array.from(infoRow.querySelectorAll('button'));
            moreButton.addEventListener('click', showingMoreInfo);
            buyButton.addEventListener('click', buying);

        }

        modelField.value = '';
        descriptionField.value = '';
        yearField.value = '';
        priceField.value = '';
    }

    function showingMoreInfo(event) {
        const currentState = event.target.textContent;
        event.target.textContent === 'More Info' ? event.target.textContent = 'Less Info' : event.target.textContent = 'More Info';
        const currentRow = event.target.parentElement.parentElement;
        const hiddenSectionIndex = Array.from(tableBody.children).indexOf(currentRow) + 1;
        const hiddenSection = Array.from(tableBody.children)[hiddenSectionIndex];
        currentState === 'More Info' ? hiddenSection.style.display = 'contents' : hiddenSection.style.display = 'none';
    }

    function buying(event) {
        event.target.parentElement.parentElement.remove();
        const price = Number(Array.from(event.target.parentElement.parentElement.querySelectorAll('td'))[1].textContent);
        totalPriceField.textContent = (Number(totalPriceField.textContent) + price).toFixed(2);
    }
}
