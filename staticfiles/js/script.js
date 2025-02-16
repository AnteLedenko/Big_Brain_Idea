document.addEventListener('DOMContentLoaded', () => {
    const themeToggle = document.getElementById('themeToggle');

    if (localStorage.getItem('theme') === 'dark') {
        document.body.classList.add('dark-theme');
        document.querySelector('header').classList.add('dark-theme');
        document.querySelector('nav').classList.add('dark-theme');
        document.querySelector('footer').classList.add('dark-theme');
        themeToggle.textContent = 'Light Mode';
    }

    themeToggle.addEventListener('click', () => {
        document.body.classList.toggle('dark-theme');
        document.querySelector('header').classList.toggle('dark-theme');
        document.querySelector('nav').classList.toggle('dark-theme');
        document.querySelector('footer').classList.toggle('dark-theme');
        const isDark = document.body.classList.contains('dark-theme');
        themeToggle.textContent = isDark ? 'Light Mode' : 'Dark Mode';

        localStorage.setItem('theme', isDark ? 'dark' : 'light');
    });
});
