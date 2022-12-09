window.addEventListener('load', solution);


function solution() {

    const nameField = document.getElementById('fname');
    const emailField = document.getElementById('email');
    const phoneField = document.getElementById('phone');
    const addressField = document.getElementById('address');
    const codeField = document.getElementById('code');
    const submitButton = document.getElementById('submitBTN');
    const editButton = document.getElementById('editBTN');
    const continueButton = document.getElementById('continueBTN');
    const previewList = document.getElementById('infoPreview');
    submitButton.addEventListener('click', submitting);
    editButton.addEventListener('click', editing);
    continueButton.addEventListener('click', finishing);


    function submitting() {

        if (nameField.value !== '' && emailField.value !== '') {
            previewList.innerHTML = `
            <li>Full Name: ${nameField.value}</li>
            <li>Email: ${emailField.value}</li>
            <li>Phone Number: ${phoneField.value}</li>
            <li>Address: ${addressField.value}</li>
            <li>Postal Code: ${codeField.value}</li>
            `;

            submitButton.disabled = true;
            editButton.disabled = false;
            continueButton.disabled = false;
        }

        nameField.value = '';
        emailField.value = '';
        phoneField.value = '';
        addressField.value = '';
        codeField.value = '';
    }

    function editing() {
        submitButton.disabled = false;
        editButton.disabled = true;
        continueButton.disabled = true;
        const items = Array.from(previewList.children);
        nameField.value = items[0].textContent.replace('Full Name: ', '');
        emailField.value = items[1].textContent.replace('Email: ', '');
        phoneField.value = items[2].textContent.replace('Phone Number: ', '');
        addressField.value = items[3].textContent.replace('Address: ', '');
        codeField.value = items[4].textContent.replace('Postal Code: ', '');
        previewList.innerHTML = '';
    }

    function finishing() {
        const block = document.getElementById('block');
        block.innerHTML = '';
        const newEl = document.createElement('h3');
        newEl.textContent = 'Thank you for your reservation!';
        block.appendChild(newEl);
    }
}
