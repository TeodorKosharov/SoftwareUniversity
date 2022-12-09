const url = 'http://localhost:3030/jsonstore/collections/students';
const table = document.querySelector('tbody');
document.getElementById('form').addEventListener('submit', onSubmit);


async function onSubmit(event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    const firstName = formData.get('firstName');
    const lastName = formData.get('lastName');
    const facultyNumber = formData.get('facultyNumber');
    const grade = formData.get('grade');

    if (firstName === '' || lastName === '' || facultyNumber === '' || grade === '') {
        alert('Inputs must be filled!');
        throw new Error('Inputs must be filled!');
    }

    const newRecord = {
        firstName: firstName, lastName: lastName, facultyNumber: facultyNumber, grade: grade
    };
    await fetch(url, {
        method: 'post', headers: {
            'Content-Type': 'application/json'
        }, body: JSON.stringify(newRecord)
    });
    event.target.reset();

    const response = await fetch(url);
    const data = Object.values(await response.json());
    data.forEach(obj => {
        const newTableRow = document.createElement('tr');
        newTableRow.innerHTML = `
        <td>${obj.firstName}</td>
        <td>${obj.lastName}</td>
        <td>${obj.facultyNumber}</td>
        <td>${obj.grade}</td>
        `;
        table.append(newTableRow);
    });
}
