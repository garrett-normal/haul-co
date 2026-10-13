document.getElementById('submissionModal').addEventListener('bs.dismiss', function () {
    // Target the form inside the modal and reset it
    const form = this.querySelector('form');
    if (form) {
        form.reset();
    }
});