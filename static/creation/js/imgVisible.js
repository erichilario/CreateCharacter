// Toggles the visibility of images used in user-guide, data-dictionary and data-model templates
function toggler(z) {
	var x = document.getElementById(z);
	if (x.style.visibility === 'visible') {
		x.style.visibility = 'hidden';
	} else {
		x.style.visibility = 'visible';
	}
}