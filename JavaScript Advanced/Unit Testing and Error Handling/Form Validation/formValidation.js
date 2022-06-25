function validate() {
    const username = document.getElementById('username');
    const email = document.getElementById('email');
    const password = document.getElementById('password');
    const confirmPassword = document.getElementById('confirm-password');
    const companyBox = document.getElementById('company');
    const companyNumber = document.getElementById('companyNumber');
    const submit = document.getElementById('submit');

    const usernamePattern = new RegExp('^[A-Za-z0-9]{3,20}$');
    const passwordsPattern = new RegExp('^[A-Za-z0-9_]{5,15}$');
    const emailPattern = new RegExp('^[^@.]+@[^@]*\.[^@]+$');
    const companyNumPattern = new RegExp('^[0-9]{4}$');

    companyBox.addEventListener('change', () => {
        const additionalInfo = document.getElementById('companyInfo');
        if (companyBox.checked) additionalInfo.style.display = 'block';
        else {
            additionalInfo.style.display = 'none';
            companyNumber.value = '';
        }
    });

    submit.addEventListener('click', submitFunc);

    function submitFunc(event) {
        event.preventDefault();
        !usernamePattern.test(username.value) ? username.style.borderColor = 'red' : username.style.border = 'none';
        !(passwordsPattern.test(password.value)) ? password.style.borderColor = 'red' : password.style.border = 'none';
        !(passwordsPattern.test(confirmPassword.value)) || password.value !== confirmPassword.value ? confirmPassword.style.borderColor = 'red' : confirmPassword.style.border = 'none';
        !(emailPattern.test(email.value)) ? email.style.borderColor = 'red' : email.style.border = 'none';
        if (companyBox.checked && companyNumPattern.test(companyNumber.value)) {
            companyNumber.style.border = 'none';
        } else if (companyBox.checked && !(companyNumPattern.test(companyNumber.value))) {
            companyNumber.style.borderColor = 'red';
        }

        if ([username, email, password, confirmPassword, companyNumber].filter(x => x.style.borderColor !== 'red').length === 5) {
            document.getElementById('valid').style.display = 'block';
        } else {
            document.getElementById('valid').style.display = 'none';
        }
    }
}
