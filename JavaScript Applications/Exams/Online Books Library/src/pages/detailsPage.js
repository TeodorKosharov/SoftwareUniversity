import {html, render} from '../../node_modules/lit-html/lit-html.js';

export async function details(context) {
    const clickedBookId = context.params.id;
    const clickedBook = await (await fetch(`http://localhost:3030/data/books/${clickedBookId}`)).json();
    let detailsTemplate;

    if (sessionStorage.userData !== undefined && JSON.parse(sessionStorage.userData).id === clickedBook._ownerId) {
        detailsTemplate = (book) => html`
            <section id="details-page" class="details">
                <div class="book-information">
                    <h3>${book.title}</h3>
                    <p class="type">Type: ${book.type}</p>
                    <p class="img"><img src=${book.imageUrl}></p>
                    <div class="actions">
                        <!-- Edit/Delete buttons ( Only for creator of this book )  -->
                        <a class="button" href="/edit/${book._id}">Edit</a>
                        <a class="button" href="/deleting/${book._id}">Delete</a>
                    </div>
                </div>
                <div class="book-description">
                    <h3>Description:</h3>
                    <p>${book.description}</p>
                </div>
            </section>
        `;
    } else {
        detailsTemplate = (book) => html`
            <section id="details-page" class="details">
                <div class="book-information">
                    <h3>${book.title}</h3>
                    <p class="type">Type: ${book.type}</p>
                    <p class="img"><img src=${book.imageUrl}></p>
                </div>
                <div class="book-description">
                    <h3>Description:</h3>
                    <p>${book.description}</p>
                </div>
            </section>
        `;
    }

    render(detailsTemplate(clickedBook), document.querySelector('main'));
}
