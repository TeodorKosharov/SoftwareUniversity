import {html, render} from '../../node_modules/lit-html/lit-html.js';

export async function showMemes() {
    const memes = await (await fetch('http://localhost:3030/data/memes?sortBy=_createdOn%20desc')).json();
    let allMemesTemplate;

    if (memes.length > 0) {
        allMemesTemplate = html`
        <section id="meme-feed">
            <h1>All Memes</h1>
            <div id="memes">
                ${memes.map(meme => html`
                    <div class="meme">
                        <div class="card">
                            <div class="info">
                                <p class="meme-title">${meme.title}</p>
                                <img class="meme-image" alt="meme-img" src="${meme.imageUrl}">
                            </div>
                            <div id="data-buttons">
                                <a class="button" href="/memes/${meme._id}">Details</a>
                            </div>
                        </div>
                    </div>
                    </div>
                    </section>`)}
    `;

    } else {
        allMemesTemplate = html`
        <section id="meme-feed">
            <h1>All Memes</h1>
            <div id="memes">
                <p class="no-memes">No memes in database.</p></div>
        </section>`;
    }

    render(allMemesTemplate, document.querySelector('main'));
}
