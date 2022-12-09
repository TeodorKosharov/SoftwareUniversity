const url = 'http://localhost:3030/jsonstore/collections/books';
document.querySelector('form').addEventListener('submit', submitting);
document.getElementById('loadBooks').addEventListener('click', booksLoading);
document.querySelectorAll('.deleteBtn').forEach(button => button.addEventListener('click', deleting));
document.querySelectorAll('.editBtn').forEach(button => button.addEventListener('click', editing));

let bookId;
let editRow;

async function submitting(event) {
    event.preventDefault();

    const formData = new FormData(event.target);
    const title = formData.get('title');
    const author = formData.get('author');
    event.target.reset();

    if (title === '' || author === '') {
        alert('Inputs must not be empty!');
        throw new Error('Inputs must not be empty!');
    }


    await fetch(url, {
        method: 'post', headers: {
            'Content-Type': 'application/json'
        }, body: JSON.stringify({author, title})
    });

}

async function booksLoading() {
    const response = await fetch(url);
    const data = await response.json();
    const allBooks = Object.values(data);

    allBooks.forEach(obj => {
        if (!Array.from(document.querySelectorAll('.bookTitle')).map(x => x.textContent).includes(obj.title)) {
            const newRow = document.createElement('tr');
            newRow.innerHTML = `
                <td class="bookTitle">${obj.title}</td>
                <td class="bookAuthor">${obj.author}</td>
                <td>
                    <button class="editBtn">Edit</button>
                    <button class="deleteBtn">Delete</button>
                </td>
            `;
            document.getElementById('booksData').append(newRow);
            newRow.querySelector('.editBtn').addEventListener('click', editing);
            newRow.querySelector('.deleteBtn').addEventListener('click', deleting);
        }
    });

}

async function editing(event) {
    const currentRow = event.target.parentElement.parentElement;
    editRow = currentRow;
    const title = currentRow.querySelector('.bookTitle').textContent;
    const author = currentRow.querySelector('.bookAuthor').textContent;
    const response = await fetch(url);
    const data = await response.json();

    for (const id in data) {
        if (data[id].title === title) {
            bookId = id;
            document.querySelector('input[name="title"]').value = title;
            document.querySelector('input[name="author"]').value = author;
            const submitButton = document.querySelector('#formSubmit');
            document.querySelector('form').removeEventListener('submit', submitting);
            submitButton.addEventListener('click', editedSubmit);
            break;
        }
    }
}

async function editedSubmit(event) {
    event.preventDefault();
    const editedTitle = document.querySelector('input[name="title"]').value;
    const editedAuthor = document.querySelector('input[name="author"]').value;
    await fetch(url + `/${bookId}`, {
        method: 'put', headers: {
            'Content-Type': 'application/json'
        }, body: JSON.stringify({author: editedAuthor, title: editedTitle})
    });

    const [title, author] = editRow.children;
    title.textContent = editedTitle;
    author.textContent = editedAuthor;
    document.querySelector('input[name="title"]').value = '';
    document.querySelector('input[name="author"]').value = '';
    document.querySelector('#formSubmit').removeEventListener('click', editedSubmit);
    document.querySelector('form').addEventListener('submit', submitting);
}

async function deleting(event) {
    event.target.parentElement.parentElement.remove();
    const title = event.target.parentElement.parentElement.querySelector('.bookTitle').textContent;
    const response = await fetch(url);
    const data = Object.entries(await response.json());
    data.forEach(arr => {
        if (arr[1].title === title) {
            fetch(url + `/${arr[0]}`, {
                method: 'delete'
            });
        }
    });
}
