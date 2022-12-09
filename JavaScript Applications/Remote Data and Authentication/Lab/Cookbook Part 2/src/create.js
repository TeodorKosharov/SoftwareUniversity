document.querySelector('form').addEventListener('submit', async (event) => {
    event.preventDefault();
    const formData = new FormData(event.target);
    const name = formData.get('name');
    const imgUrl = formData.get('img');
    const ingredients = formData.get('ingredients').split('\n');
    const steps = formData.get('steps').split('\n');
    const id = sessionStorage.id;
    event.target.reset();

    if (name === '' || imgUrl === '' || ingredients === [] || steps === []) {
        return alert('All fields are required!');
    }

    await fetch('http://localhost:3030/jsonstore/cookbook/recipes', {
        method: 'post',
        headers: {
            'content-type': 'application/json',
            'x-authorization': sessionStorage.token
        },
        body: JSON.stringify({name, imgUrl, ingredients, steps, '_id': id})
    });
    window.location.href = 'http://localhost:63342/JS%20Applications/Remote%20Data%20and%20Authentication/Lab/Cookbook%20Part%202/index.html?_ijt=gu5o2tt92de18dmlr1thpjrpc8&_ij_reload=RELOAD_ON_SAVE';
});
