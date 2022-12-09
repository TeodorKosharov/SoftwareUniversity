document.querySelector('form').addEventListener('submit', async (event) => {
    event.preventDefault();
    const formData = new FormData(event.target);
    const email = formData.get('email');
    const password = formData.get('password');
    event.target.reset();

    if (email === '' || password === '') {
        return alert('All fields are required!');
    }

    const response = await fetch('http://localhost:3030/users/login', {
        method: 'post', headers: {
            'content-type': 'application/json'
        }, body: JSON.stringify({email, password})
    });

    const data = await response.json();
    sessionStorage.setItem('token', data.accessToken);
    sessionStorage.setItem('id', data._id);
    window.location.href = 'http://localhost:63342/JS%20Applications/Remote%20Data%20and%20Authentication/Lab/Cookbook%20Part%202/index.html?_ijt=gu5o2tt92de18dmlr1thpjrpc8&_ij_reload=RELOAD_ON_SAVE';
});
