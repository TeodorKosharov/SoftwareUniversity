window.addEventListener('load', solve);

function solve() {
    const genreField = document.getElementById('genre');
    const nameField = document.getElementById('name');
    const authorField = document.getElementById('author');
    const dateField = document.getElementById('date');
    const addButton = document.getElementById('add-btn');
    const collectionSongsDiv = document.querySelector('.all-hits-container');
    const savedSongsDiv = document.querySelector('.saved-container');

    addButton.addEventListener('click', adding);

    function adding(event) {
        event.preventDefault();
        if (genreField.value !== '' && nameField.value !== '' && authorField.value !== '' && dateField.value !== '') {
            const newDiv = document.createElement('div');
            newDiv.classList.add('hits-info');
            newDiv.innerHTML = `
            <img src="./static/img/img.png">
            <h2>Genre: ${genreField.value}</h2>
            <h2>Name: ${nameField.value}</h2>
            <h2>Author: ${authorField.value}</h2>
            <h3>Date: ${dateField.value}</h3>
            <button class="save-btn">Save song</button>
            <button class="like-btn">Like song</button>
            <button class="delete-btn">Delete</button>`;

            collectionSongsDiv.appendChild(newDiv);
            const [saveButton, likeButton, deleteButton] = Array.from(newDiv.querySelectorAll('button'));
            saveButton.addEventListener('click', saving);
            likeButton.addEventListener('click', liking);
            deleteButton.addEventListener('click', deleting);

        }

        genreField.value = '';
        nameField.value = '';
        authorField.value = '';
        dateField.value = '';
    }

    function liking(event) {
        event.target.disabled = true;
        const likesParagraph = document.querySelector('.likes p');
        const currentLikes = Number(likesParagraph.textContent.replace('Total Likes: ', ''));
        likesParagraph.textContent = `Total Likes: ${(currentLikes + 1).toString()}`;
    }

    function saving(event) {
        const currentDiv = event.target.parentElement;
        const [saveButton, likeButton] = Array.from(currentDiv.querySelectorAll('button'));
        currentDiv.removeChild(saveButton);
        currentDiv.removeChild(likeButton);
        savedSongsDiv.appendChild(currentDiv);
    }

    function deleting(event) {
        event.target.parentElement.remove();
    }
}
