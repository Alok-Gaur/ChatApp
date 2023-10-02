// const signUpButton = document.getElementById('signUp');
// const signInButton = document.getElementById('signIn');
// const container = document.getElementById('container');

// signUpButton.addEventListener('click', () => {
// 	container.classList.add("right-panel-active");
// });

// signInButton.addEventListener('click', () => {
// 	container.classList.remove("right-panel-active");
// });

function addLeftPanel() {
	const container = document.getElementById('container');
	container.classList.add("left-panel-active");
}

function removeLeftPanel() {
	const container = document.getElementById('container');
	container.classList.remove("left-panel-active");
}