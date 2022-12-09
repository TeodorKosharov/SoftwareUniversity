const url = 'http://localhost:3030/jsonstore/phonebook';

function attachEvents() {
    const loadButton = document.getElementById('btnLoad');
    const createButton = document.getElementById('btnCreate');
    const personField = document.getElementById('person');
    const phoneField = document.getElementById('phone');
    const phonebookList = document.getElementById('phonebook');

    loadButton.addEventListener('click', loading);
    createButton.addEventListener('click', creating);
    let loadedNames = [];

    async function loading() {
        const response = await fetch(url);
        const data = Object.values(await response.json());
        data.forEach(obj => {
            if (!(loadedNames.includes(obj.person))) {
                const newLi = document.createElement('li');
                const deleteButton = document.createElement('button');
                deleteButton.textContent = 'Delete';
                deleteButton.addEventListener('click', deleting);
                newLi.textContent = `${obj.person}: ${obj.phone}`;
                newLi.append(deleteButton);
                phonebookList.append(newLi);
                loadedNames.push(obj.person);
            }
        });
    }

    async function creating() {
        if (personField.value === '') {
            alert('Person input must not be empty!');
            throw new Error('Person input must not be empty!');
        }

        if (phoneField.value === '') {
            alert('Phone input must not be empty!');
            throw new Error('Phone input must not be empty!');
        }

        loadedNames.push(personField.value);
        const newRecord = {person: personField.value, phone: phoneField.value};
        await fetch(url, {
            method: 'post', headers: {
                'Content-Type': 'application/json'
            }, body: JSON.stringify(newRecord)
        });
        const newLi = document.createElement('li');
        const deleteButton = document.createElement('button');
        deleteButton.addEventListener('click', deleting);
        deleteButton.textContent = 'Delete';
        newLi.textContent = `${newRecord.person}: ${newRecord.phone}`;
        newLi.append(deleteButton);
        phonebookList.append(newLi);
        personField.value = '';
        phoneField.value = '';
    }

    async function deleting(event) {
        event.target.parentElement.remove();
        const name = event.target.parentElement.textContent.slice(0, event.target.parentElement.textContent.indexOf(':'));
        loadedNames.splice(loadedNames.indexOf(name), 1);
        const data = Object.values(await (await fetch(url)).json());
        const neededId = data.filter(record => record.person === name)[0]._id;
        await fetch(url + `/${neededId}`, {
            method: 'delete'
        });
    }
}

attachEvents();