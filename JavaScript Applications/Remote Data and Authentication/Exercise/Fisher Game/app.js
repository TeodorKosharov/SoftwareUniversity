export function updateNavi() {
    const currentLocation = getFileName();
    const anchors = Array.from(document.querySelectorAll('a'));
    const currentAnchor = anchors.filter(a => a.textContent === currentLocation)[0];

    for (const a of anchors) {
        if (a === currentAnchor || currentLocation === 'Index') {
            a.className = 'active';
            break;
        } else {
            a.className = '';
        }
    }

    if (sessionStorage.userData !== undefined) {
        document.querySelector('#guest').style.display = 'none';
        document.querySelector('#user').style.display = 'inline-block';
        document.querySelector('.email').textContent = `Welcome, ${JSON.parse(sessionStorage.userData).email}`;
    } else {
        document.querySelector('#guest').style.display = 'inline-block';
        document.querySelector('#user').style.display = 'none';
        document.querySelector('.email').textContent = `Welcome, guest`;
    }
}

function getFileName() {
    const location = window.location.pathname.split('/');
    const filename = location[location.length - 1];
    const name = filename.split('.')[0];
    return name[0].toUpperCase() + name.slice(1);
}

if (getFileName() === 'Index') {
    updateNavi();
}

document.getElementById('logout').addEventListener('click', async () => {
    await fetch('http://localhost:3030/users/logout', {
        method: 'get',
        headers: {
            'x-authorization': JSON.parse(sessionStorage.userData).token
        }
    });
    sessionStorage.clear();
    updateNavi();
    window.location.href = 'http://localhost:63342/JS%20Applications/Remote%20Data%20and%20Authentication/Exercise/Fisher%20Game/src/home.html';
});
