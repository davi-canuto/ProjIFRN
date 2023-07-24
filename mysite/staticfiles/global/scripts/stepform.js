let currentStep = 1;

function showStep(step) {
    const steps = document.getElementsByClassName('step');
    for (let i = 0; i < steps.length; i++) {
        steps[i].classList.remove('active');
    }
    document.getElementById('step' + step).classList.add('active');
}

function nextStep(step) {
    currentStep = step;
    showStep(step);
}

function prevStep(step) {
    currentStep = step;
    showStep(step);
}

showStep(currentStep);

