import {html, render} from '../../node_modules/lit-html/lit-html.js';

export async function dashboardPage() {
    const books = await (await fetch('http://localhost:3030/data/books?sortBy=_createdOn%20desc')).json();
    let dashboardTemplate;

    if (books.length > 0) {
        dashboardTemplate = (allBooks) => html`
        <section id="dashboard-page" class="dashboard">
            <h1>Dashboard</h1>
            <!-- Display ul: with list-items for All books (If any) -->
            <ul class="other-books-list">
                ${allBooks.map(book => html`<li class="otherBooks">
                    <h3>${book.title}</h3>
                    <p>Type: ${book.type}</p>
                    <p class="img"><img src="${book.imageUrl}"></p>
                    <a class="button" href="/dashboard/${book._id}">Details</a>
                </li>`)}
            </ul>
        </section>
    `;
    }
    else {
        dashboardTemplate = (allBooks) => html`
    <section id="dashboard-page" class="dashboard">
        <h1>Dashboard</h1>
        <!-- Display paragraph: If there are no books in the database -->
        <p class="no-books">No books in database!</p>
    </section>`;
    }

    render(dashboardTemplate(books), document.querySelector('main'));
}
