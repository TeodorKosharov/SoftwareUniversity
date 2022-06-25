function deleteByEmail() {

    const input = document.querySelector('input');
    const enteredEmail = input.value;
    const tbody = document.querySelector('tbody');
    const rows = Array.from(tbody.children);
    let isEmailFound = false;

    for (const row of rows) {
        const [name, email] = Array.from(row.children);
        const currentEmail = email.textContent;
        if (enteredEmail === currentEmail) {
            email.parentElement.parentElement.removeChild(row);
            isEmailFound = true;
            break;
        }
    }

    if (isEmailFound) document.getElementById('result').textContent = 'Deleted';
    else document.getElementById('result').textContent = 'Not found.';

}
