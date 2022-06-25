function solve() {
    const recipientField = document.getElementById('recipientName');
    const titleField = document.getElementById('title');
    const messageField = document.getElementById('message');
    const [addButton, resetButton] = Array.from(document.querySelectorAll('button'));
    const mailsSection = document.querySelector('.list-mails #list');
    const sentMailsSection = document.querySelector('.sent-mails .sent-list');
    const deletedMailsSection = document.querySelector('.trash .delete-list');

    addButton.addEventListener('click', adding);
    resetButton.addEventListener('click', (event) => {
        event.preventDefault();
        recipientField.value = '';
        titleField.value = '';
        messageField.value = '';
    });

    function adding(event) {
        event.preventDefault();

        if (recipientField.value !== '' && titleField.value !== '' && messageField.value !== '') {
            const newLi = document.createElement('li');
            newLi.innerHTML = `
            <h4>Title: ${titleField.value}</h4>
            <h4>Recipient Name: ${recipientField.value}</h4>
            <span>${messageField.value}</span>
            <div id="list-action">
                <button type="submit" id="send">Send</button>
                <button type="submit" id="delete">Delete</button>
            </div>
            `;
            mailsSection.appendChild(newLi);
            const [sendButton, deleteButton] = Array.from(newLi.querySelectorAll('button'));
            sendButton.addEventListener('click', sending);
            deleteButton.addEventListener('click', deleting);
        }

        recipientField.value = '';
        titleField.value = '';
        messageField.value = '';
    }

    function sending(event) {
        const [name, title] = Array.from(event.target.parentElement.parentElement.querySelectorAll('h4'));
        event.target.parentElement.parentElement.remove();
        const sendedMailLi = document.createElement('li');
        sendedMailLi.innerHTML = `
        <span>To: ${name.textContent.replace('Title: ', '')}</span>
        <span>Title: ${title.textContent.replace('Recipient Name: ', '')}</span>
        <div class="btn">
            <button type="submit" class="delete">Delete</button>
        </div>`;
        sentMailsSection.appendChild(sendedMailLi);
        const deleteBtn = sendedMailLi.querySelector('button');
        deleteBtn.addEventListener('click', secondDeleting);
    }

    function deleting(event) {
        const liForRemoving = event.target.parentElement.parentElement;
        const [title, name] = Array.from(liForRemoving.querySelectorAll('h4'));
        liForRemoving.remove();
        const newLi = document.createElement('li');
        newLi.innerHTML = `
        <span>To: ${name.textContent.replace('Recipient Name: ', '')}</span>
        <span>${title.textContent}</span>
        `;
        deletedMailsSection.appendChild(newLi);
    }

    function secondDeleting(event) {
        const liForRemoving = event.target.parentElement.parentElement;
        const [name, title] = Array.from(liForRemoving.querySelectorAll('span'));
        liForRemoving.remove();
        const newLi = document.createElement('li');
        newLi.innerHTML = `
        <span>To: ${name.textContent.replace('Recipient Name: ', '')}</span>
        <span>${title.textContent}</span>
        `;
        deletedMailsSection.appendChild(newLi);
    }

}

solve()
