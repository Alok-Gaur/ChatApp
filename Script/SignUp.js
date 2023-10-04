// <<<<<<< HEAD
const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const main = document.getElementById('main');

signUpButton.addEventListener('click', () => {
	main.classList.add("right-panel-active");
});

signInButton.addEventListener('click', () => {
	main.classList.remove("right-panel-active");
});

// const signUpButton = document.getElementById('signUp');
// const signInButton = document.getElementById('signIn');
// const container = document.getElementById('container');

// signUpButton.addEventListener('click', () => {
// 	container.classList.add("right-panel-active");
// });

// signInButton.addEventListener('click', () => {
// 	container.classList.remove("right-panel-active");
// });

// function addLeftPanel() {
// 	const container = document.getElementById('container');
// 	container.classList.add("right-panel-active");
// }

// function removeLeftPanel() {
// 	const container = document.getElementById('container');
// 	container.classList.remove("right-panel-active");
// }
// >>>>>>> 34427bfbdc0ea6adeb99d29db7f354bacac117d2
