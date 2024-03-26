const agreeCheckbox = document.getElementById('agreeCheckbox');
		const continueButton = document.querySelector('button');
		continueButton.disabled = true;

		agreeCheckbox.addEventListener('change', () => {
			continueButton.disabled = !agreeCheckbox.checked;
		});