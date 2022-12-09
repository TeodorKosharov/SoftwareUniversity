import page from '../node_modules/page/page.mjs';

const mainElement = document.querySelector('main');
page(showInfo);
page('/home', () => mainElement.innerHTML += `<h2>Home view</h2>`);
page('/about', () => mainElement.innerHTML += `<h2>About view</h2>`);
page('/contact', () => mainElement.innerHTML += `<h2>Contact view</h2>`);

page('/catalog', showDetails);
page('/catalog/:id', (context) => {
    const clickedProduct = `Product ${context.path[context.path.length - 1]} was clicked`;
    mainElement.innerHTML += clickedProduct;
});
page.start();


function showDetails() {
    mainElement.innerHTML = `
    <a href="/catalog/p1">Product 1</a>
    <a href="/catalog/p2">Product 2</a>
    <a href="/catalog/p3">Product 3</a>
    `;
}

function showInfo(context, next) {
    mainElement.innerHTML = `<h2>Info: </h2>`;
    next();
}
