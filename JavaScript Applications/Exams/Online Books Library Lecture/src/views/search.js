import {html} from '../../node_modules/lit-html/lit-html.js';
import {bookPreview} from "./common.js";
import {getAllBooks, searchBooks} from "../api/data.js";

const searchTemplate = (books, onSearch, params = '') => html`
    <section id="search-page" class="dashboard">
        <h1>Search</h1>
        <form @submit="${onSearch}">
            <input type="text" name="search" value="${params}">
            <input type="submit" value="Search">
        </form>

        ${books.length === 0
                ? html`<p class="no-books">No results!</p>`
                : html`
                    <ul class="other-books-list">${books.map(bookPreview)}</ul>`
        }
    </section>
`;

export async function searchPage(context) {
    const params = context.queryString.split('=')[1];
    let books = [];

    if (params) {
        books = await searchBooks(decodeURIComponent(params));
    } else {
        books = await getAllBooks();
    }

    context.render(searchTemplate(books, onSearch, params));

    function onSearch(event) {
        event.preventDefault();
        const formData = new FormData(event.target);
        const search = formData.get('search');

        if (search) {
            context.page.redirect('/search?query=' +  encodeURIComponent(search))
        }
    }
}
