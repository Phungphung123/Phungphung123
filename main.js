// Đảm bảo mã này được đặt trong tệp main.js hoặc được liên kết với HTML của bạn

// Lấy các phần tử từ DOM
const signInButton = document.getElementById("signInButton");
const overlay = document.getElementById("overlay");
const loginForm = document.getElementById("loginForm");
const closeButton = document.getElementById("closeButton");

// Hiển thị form đăng nhập
signInButton.addEventListener("click", () => {
    loginForm.style.display = "block";
    overlay.style.display = "block";
});

// Ẩn form đăng nhập
closeButton.addEventListener("click", () => {
    loginForm.style.display = "none";
    overlay.style.display = "none";
});

// Ẩn form khi nhấn vào overlay
overlay.addEventListener("click", () => {
    loginForm.style.display = "none";
    overlay.style.display = "none";
});

// Đảm bảo mã này được đặt trong tệp main.js hoặc được liên kết với HTML của bạn
document.addEventListener("DOMContentLoaded", () => {
    // Lấy các phần tử từ DOM
    const signInButton = document.getElementById("signInButton");
    const overlay = document.getElementById("overlay");
    const loginForm = document.getElementById("loginForm");
    const closeButton = document.getElementById("closeButton");

    const signUpButton = document.querySelector(".header__sign-up");
    const signUpOverlay = document.getElementById("signUpOverlay");
    const signUpForm = document.getElementById("signUpForm");
    const closeSignUpButton = document.getElementById("closeSignUpButton");

    // Hiển thị form đăng nhập
    signInButton.addEventListener("click", () => {
        loginForm.style.display = "block";
        overlay.style.display = "block";
    });

    // Ẩn form đăng nhập
    closeButton.addEventListener("click", () => {
        loginForm.style.display = "none";
        overlay.style.display = "none";
    });

    // Ẩn form khi nhấn vào overlay
    overlay.addEventListener("click", () => {
        loginForm.style.display = "none";
        overlay.style.display = "none";
    });

    // Hiển thị form đăng ký
    signUpButton.addEventListener("click", () => {
        signUpForm.style.display = "block";
        signUpOverlay.style.display = "block";
    });

    // Ẩn form đăng ký
    closeSignUpButton.addEventListener("click", () => {
        signUpForm.style.display = "none";
        signUpOverlay.style.display = "none";
    });

    // Ẩn form đăng ký khi nhấn vào overlay
    signUpOverlay.addEventListener("click", () => {
        signUpForm.style.display = "none";
        signUpOverlay.style.display = "none";
    });
});
