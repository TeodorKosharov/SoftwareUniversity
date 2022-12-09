function solve() {
    const firstNameField = document.getElementById('fname');
    const lastNameField = document.getElementById('lname');
    const emailField = document.getElementById('email');
    const birthField = document.getElementById('birth');
    const positionField = document.getElementById('position');
    const salaryField = document.getElementById('salary');
    const hireButton = document.getElementById('add-worker');
    const tableBody = document.getElementById('tbody');
    const totalSalarySpan = document.getElementById('sum');

    hireButton.addEventListener('click', hiring);

    function hiring(event) {
        event.preventDefault();
        if (firstNameField.value !== '' && lastNameField.value !== '' && emailField.value !== '' && birthField.value !== '' && positionField.value !== '' && salaryField.value !== '') {
            const newTableRow = document.createElement('tr');
            newTableRow.innerHTML = `
            <td>${firstNameField.value}</td>
            <td>${lastNameField.value}</td>
            <td>${emailField.value}</td>
            <td>${birthField.value}</td>
            <td>${positionField.value}</td>
            <td>${salaryField.value}</td>
            <td><button class="fired">Fired</button> <button class="edit">Edit</button></td>
            `;

            tableBody.appendChild(newTableRow);
            totalSalarySpan.textContent = ((Number(totalSalarySpan.textContent) + Number(salaryField.value)).toFixed(2)).toString();

            const [firedButton, editButton] = Array.from(newTableRow.querySelectorAll('button'));
            firedButton.addEventListener('click', firing);
            editButton.addEventListener('click', editing);
        }

        firstNameField.value = '';
        lastNameField.value = '';
        emailField.value = '';
        birthField.value = '';
        positionField.value = '';
        salaryField.value = '';
    }

    function firing(event) {
        const currentRow = event.target.parentElement.parentElement;
        const salary = Array.from(currentRow.children)[5];
        totalSalarySpan.textContent = ((Number(totalSalarySpan.textContent) - Number(salary.textContent)).toFixed(2)).toString();
        currentRow.remove();
    }

    function editing(event) {
        const currentRow = event.target.parentElement.parentElement;
        const [fname, lname, email, birth, pos, salary] = Array.from(currentRow.children);
        firstNameField.value = fname.textContent;
        lastNameField.value = lname.textContent;
        emailField.value = email.textContent;
        birthField.value = birth.textContent;
        positionField.value = pos.textContent;
        salaryField.value = salary.textContent;

        totalSalarySpan.textContent = ((Number(totalSalarySpan.textContent) - Number(salary.textContent)).toFixed(2)).toString();
        currentRow.remove();
    }
}

solve()
