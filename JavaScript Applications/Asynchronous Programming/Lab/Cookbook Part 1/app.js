const recipes = Object.entries(await (await fetch('http://localhost:3030/jsonstore/cookbook/recipes')).json());
const root = document.querySelector('main');

function creatingElement(element, attr, content) {
    const createdEl = document.createElement(element);

    if (attr === 'text') {
        createdEl.textContent = content;
    } else if (attr === 'src') {
        createdEl.src = content;
    }

    return createdEl;
}

recipes.forEach(recipe => {
    const data = recipe[1];

    const previewArticle = document.createElement('article');
    previewArticle.dataset.recipeId = data._id;
    previewArticle.className = 'preview';

    const titleDiv = creatingElement('div');
    titleDiv.className = 'title';
    const h2 = creatingElement('h2', 'text', data.name);

    const smallDiv = creatingElement('div');
    smallDiv.className = 'small';
    const img = creatingElement('img', 'src', data.img);

    titleDiv.appendChild(h2);
    smallDiv.appendChild(img);
    previewArticle.appendChild(titleDiv);
    previewArticle.appendChild(smallDiv);
    root.appendChild(previewArticle);
    previewArticle.addEventListener('click', moreInfo);

});

async function moreInfo(event) {
    const article = event.currentTarget;
    const recipeId = event.currentTarget.dataset.recipeId;
    const recipeData = await (await fetch(`http://localhost:3030/jsonstore/cookbook/details/${recipeId}`)).json();
    // {_id: '01', name: 'Recipe 1', img: 'assets/lasagna.jpg', steps: Array(3), ingredients: Array(4)}

    const [firstDiv, secondDiv] = article.children;
    firstDiv.className = 'band';
    secondDiv.className = 'description';


    firstDiv.removeChild(firstDiv.querySelector('h2'));
    const title = creatingElement('h2', 'text', recipeData.name);
    article.insertBefore(title, firstDiv);

    // filling the first div with needed data:

    // first mini div:

    const thumbDiv = creatingElement('div');
    thumbDiv.className = 'thumb';
    const img = creatingElement('img', 'src', recipeData.img);
    thumbDiv.appendChild(img);
    firstDiv.appendChild(thumbDiv);

    // second mini div:

    const ingredientsDiv = creatingElement('div');
    ingredientsDiv.className = 'ingredients';

    const ingredientsTitle = creatingElement('h3', 'text', 'Ingredients:');
    ingredientsDiv.appendChild(ingredientsTitle);

    const list = creatingElement('ul');
    recipeData.ingredients.forEach(item => {
        const newItem = creatingElement('li', 'text', item);
        list.appendChild(newItem);
    });
    ingredientsDiv.appendChild(list);
    firstDiv.appendChild(ingredientsDiv);

    // filling the second div with needed data:

    secondDiv.removeChild(secondDiv.querySelector('img'));
    const descriptionTitle = creatingElement('h3', 'text', 'Preparation:');
    secondDiv.appendChild(descriptionTitle);
    recipeData.steps.forEach(step => {
        const stepPara = creatingElement('p', 'text', step);
        secondDiv.appendChild(stepPara);
    });

    article.removeEventListener('click', moreInfo);
}
