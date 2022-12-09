async function solution() {
    const root = document.querySelector('section');
    const articles = Object.values(await (await fetch('http://localhost:3030/jsonstore/advanced/articles/list')).json());

    for (const article of articles) {
        const articleDiv = document.createElement('div');
        articleDiv.className = 'accordion';
        articleDiv.innerHTML = `
            <div class="head">
                <span>${article.title}</span>
                <button class="button" id="${article._id}">More</button>
            </div>
            <div class="extra">
                <p>${await getContent(article._id)}</p>
            </div>`;
        const moreInfoButton = articleDiv.querySelector('button');
        moreInfoButton.addEventListener('click',() => {
            const extraInfo = articleDiv.querySelector('.extra');
            if (window.getComputedStyle(extraInfo).display === 'none') {
                extraInfo.style.display = 'block';
                moreInfoButton.textContent = 'Less';
            } else {
                extraInfo.style.display = 'none';
                moreInfoButton.textContent = 'More';
            }

        });
        root.appendChild(articleDiv);
    }

    async function getContent(id) {
        return (await (await fetch(`http://localhost:3030/jsonstore/advanced/articles/details/${id}`)).json()).content;
    }

}

solution();
