function attachEvents() {
    document.getElementById('refresh').addEventListener('click', refreshing);
    document.getElementById('submit').addEventListener('click', submitting);
    const messagesArea = document.getElementById('messages');
    const url = 'http://localhost:3030/jsonstore/messenger';
    const nameField = document.querySelector('input[name="author"]');
    const messageField = document.querySelector('input[name="content"]');


    async function refreshing() {
        nameField.value = '';
        messageField.value = '';
        messagesArea.value = '';
        const response = await fetch(url);
        const data = Object.values(await response.json());
        data.forEach(obj => messagesArea.value += `${obj.author}: ${obj.content}\n`);
    }

    async function submitting() {
        nameField.value = '';
        messageField.value = '';

        if (nameField.value === '' || messageField.value === '') {
            alert('Inputs must not be empty!');
            throw new Error('Inputs must not be empty!');
        }

        if (nameField.value === '') {
            alert('Name field must not be empty!');
            throw new Error('Name field must not be empty!');
        }

        if (messageField.value === '') {
            alert('Message field must not be empty!');
            throw new Error('Message field must not be empty!');
        }

        await fetch(url, {
            method: 'post', headers: {
                'Content-Type': 'application/json'
            }, body: JSON.stringify({author: nameField.value, content: messageField.value})
        });
    }
}

attachEvents();