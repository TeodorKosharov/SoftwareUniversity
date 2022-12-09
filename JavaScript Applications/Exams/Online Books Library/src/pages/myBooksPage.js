import {html, render} from '../../node_modules/lit-html/lit-html.js';

export async function myBooksPage() {

    const userId = JSON.parse(sessionStorage.userData).id;
    const userBooks = await (await fetch(`http://localhost:3030/data/books?where=_ownerId%3D%22${userId}%22&sortBy=_createdOn%20desc`)).json();
    let myBooksTemplate;

    if (userBooks.length > 0) {
        myBooksTemplate = html`
        <section id="my-books-page" class="my-books">
            <h1>My Books</h1>
            <ul class="my-books-list">
                ${userBooks.map(book => html`
                    <li class="otherBooks">
                        <h3>${book.title}</h3>
                        <p>Type: ${book.type}</p>
                        <p class="img"><img src="${book.imageUrl}"></p>
                        <a class="button" href="/dashboard/${book._id}">Details</a>
                    </li>`)}
            </ul>
        </section>`;
    } else {
        myBooksTemplate = html`
        <section id="my-books-page" class="my-books">
            <h1>My Books</h1>
            <p class="no-books">No books in database!</p>
        </section>`;
    }
    render(myBooksTemplate, document.querySelector('main'));
}
