let language = 'en';

function loadPage(navButton) {
	const selected = document.getElementsByClassName('selected')[0];

	if (selected != navButton) {
		const xhttp = new XMLHttpRequest();
		const content = document.getElementById('content');
		const page = navButton.id;

		if(page != 'index') {
			window.location.hash = page;
			window.document.title = `Augusto Gunsch | ${navButton.innerHTML}`;
		} else {
			history.replaceState(null, null, ' ');
			window.document.title = 'Augusto Gunsch';
		}

		xhttp.onload = function() {
			content.innerHTML = this.responseText;
		}
		xhttp.open('GET', `${language}/${page}`, true);

		selected.classList.remove('selected');
		navButton.classList.add('selected');
		content.innerHTML = '<p>Loading...</p>';

		xhttp.send();
	}
}

if(window.location.hash) {
	const page = window.location.hash.split('#')[1];
	const navButton = document.getElementById(page);
	console.log(navButton);
	loadPage(navButton);
}
