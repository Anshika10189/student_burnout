// Theme Toggle

const body = document.body;
const themeBtn = document.getElementById("theme-btn");

// Load saved theme
window.onload = function () {

    const savedTheme = localStorage.getItem("theme");

    if (savedTheme === "dark") {
        body.classList.add("dark");
        themeBtn.innerHTML = "☀️ Light Mode";
    } else {
        body.classList.remove("dark");
        themeBtn.innerHTML = "🌙 Dark Mode";
    }
};

// Toggle Theme
function toggleTheme() {

    body.classList.toggle("dark");

    if (body.classList.contains("dark")) {
        localStorage.setItem("theme", "dark");
        themeBtn.innerHTML = "☀️ Light Mode";
    } else {
        localStorage.setItem("theme", "light");
        themeBtn.innerHTML = "🌙 Dark Mode";
    }
}