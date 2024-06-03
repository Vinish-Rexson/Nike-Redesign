const container = document.getElementById('container');
const registerBtn = document.getElementById('register');
const loginBtn = document.getElementById('login');

if (mode === 'signup') {
    container.classList.add("active");
}
loginBtn.addEventListener('click', () => {
    container.classList.remove("active");
});

if (mode === 'login') {
    container.classList.remove("active");
}
registerBtn.addEventListener('click', () => {
    container.classList.add("active");
});
