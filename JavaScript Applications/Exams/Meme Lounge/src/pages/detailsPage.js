import {html, render} from '../../node_modules/lit-html/lit-html.js';
import page from '../../node_modules/page/page.mjs';

let detailsTemplate;

export async function details(context) {
    const clickedMemeId = context.params.id;
    const clickedMeme = await fetch(`http://localhost:3030/data/memes/${clickedMemeId}`);
    const clickedMemeData = await clickedMeme.json();

    if (sessionStorage.userData !== undefined) {
        if (JSON.parse(sessionStorage.userData).id === clickedMemeData._ownerId) {
            detailsTemplate = (meme) => html`
                <section id="meme-details">
                    <h1>Meme Title: ${meme.title}</h1>
                    <div class="meme-details">
                        <div class="meme-img">
                            <img alt="meme-alt" src="${meme.imageUrl}">
                        </div>
                        <div class="meme-description">
                            <h2>Meme Description</h2>
                            <p>${meme.description}</p>
                            <a class="button warning" href="/edit/${meme._id}">Edit</a>
                            <button class="button danger" @click="${deleting}">Delete</button>
                        </div>
                    </div>
                </section>
            `;
        } else {
            detailsTemplate = (meme) => html`
                <section id="meme-details">
                    <h1>Meme Title: ${meme.title}</h1>
                    <div class="meme-details">
                        <div class="meme-img">
                            <img alt="meme-alt" src="${meme.imageUrl}">
                        </div>
                        <div class="meme-description">
                            <h2>Meme Description</h2>
                            <p>${meme.description}</p>
                        </div>
                    </div>
                </section>
            `;
        }
    } else {
        detailsTemplate = (meme) => html`
                <section id="meme-details">
                    <h1>Meme Title: ${meme.title}
                    </h1>
                    <div class="meme-details">
                        <div class="meme-img">
                            <img alt="meme-alt" src="${meme.imageUrl}">
                        </div>
                        <div class="meme-description">
                            <h2>Meme Description</h2>
                            <p>
                                ${meme.description}
                            </p>
                        </div>
                    </div>
                </section>
            `
    }

    render(detailsTemplate(clickedMemeData), document.querySelector('main'));

    async function deleting() {
        const choice = confirm('Do you want to delete the meme?');
        if (choice) {
            await fetch(`http://localhost:3030/data/memes/${clickedMemeId}`, {
                method: 'delete',
                headers: {
                    'content-type': 'application/json',
                    'x-authorization': JSON.parse(sessionStorage.userData).token
                }
            });
            page.redirect('/memes');
        }
    }
}

// Функцията, която рендерира съдържанието (details(context)), на нея трябва да подадем параметър context. Този параметър има метод params,
// който съдържа id-то. В главния файл app.js трябва да имаме линк, който води към отделно meme: page('/memes/:id').
// Това id, което взимаме чрез метода params на context-а е всъщност id-то на кликнатото meme. Правим GET заявка към линка,
// използвайки id-то, след което извличаме данните и получаваме мемето. На полученото меме имаме атрибут _id, който можем
// да използваме за редиректване към страница за това меме.
// Когато създаваме meme, се запазва едно свойство _ownerId
// чрез което можем да проверим дали логнатия потребител го е създал или е от друг потребител. В sessionStorage-а имаме и свойство
// id, което съвпада с _ownerId
