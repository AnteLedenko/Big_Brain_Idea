// This script implements a dark mode toggle with theme persistence using localStorage.

document.addEventListener('DOMContentLoaded', () => {
    const themeToggle = document.getElementById('themeToggle');

    // Check if 'dark' theme is saved in localStorage and apply it if found
    if (localStorage.getItem('theme') === 'dark') {
        document.body.classList.add('dark-theme');
        document.querySelector('header').classList.add('dark-theme');
        document.querySelector('nav').classList.add('dark-theme');
        document.querySelector('footer').classList.add('dark-theme');
        themeToggle.textContent = 'Light Mode';
    }

    // Add an event listener for theme toggle button
    themeToggle.addEventListener('click', () => {
        // Toggle the 'dark-theme' class on key elements
        document.body.classList.toggle('dark-theme');
        document.querySelector('header').classList.toggle('dark-theme');
        document.querySelector('nav').classList.toggle('dark-theme');
        document.querySelector('footer').classList.toggle('dark-theme');
        // Update the button text based on the current theme
        const isDark = document.body.classList.contains('dark-theme');
        themeToggle.textContent = isDark ? 'Light Mode' : 'Dark Mode';

        // Save the current theme to localStorage
        localStorage.setItem('theme', isDark ? 'dark' : 'light');
    });
});
