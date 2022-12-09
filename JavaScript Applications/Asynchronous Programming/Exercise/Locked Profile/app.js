async function lockedProfile() {
    const profilesData = Object.values(await (await fetch('http://localhost:3030/jsonstore/advanced/profiles')).json());
    // {_id: 'fb352199-bcbc-4e1d-a1dc-ed346a6fb49a', username: 'John', email: 'john@users.bg', age: 31}

    const root = document.querySelector('main');

    profilesData.forEach(profile => {
        const profileDiv = document.createElement('div');
        profileDiv.className = 'profile';
        profileDiv.innerHTML = `
        <img src="./iconProfile2.png" class="userIcon" />
        <label>Lock</label>
        <input type="radio" name="user1Locked" value="lock" checked>
        <label>Unlock</label>
        <input type="radio" name="user1Locked" value="unlock"><br>
        <hr>
        <label>Username</label>
        <input type="text" name="user1Username" value="${profile.username}" disabled readonly />
        <div class="user1Username">
        <hr>
        <label>Email:</label>
        <input type="email" name="user1Email" value="${profile.email}" disabled readonly />
        <label>Age:</label>
        <input type="text" name="user1Age" value="${profile.age}" disabled readonly />
        </div>
        <button>Show more</button>
        `;
        root.appendChild(profileDiv);
        profileDiv.querySelector('.user1Username').style.display = 'none';
        profileDiv.querySelector('button').addEventListener('click', moreInfo);

    });

    function moreInfo(event) {
        const profileDiv = event.target.parentElement;
        const moreInfoDiv = profileDiv.querySelector('.user1Username');
        const lockInput = profileDiv.querySelector('input[value="lock"]');
        if (!lockInput.checked && moreInfoDiv.style.display === 'none') {
            moreInfoDiv.style.display = 'block';
            profileDiv.querySelector('button').textContent = 'Hide it';
        } else {
            moreInfoDiv.style.display = 'none';
            profileDiv.querySelector('button').textContent = 'Show more';
        }
    }
}
