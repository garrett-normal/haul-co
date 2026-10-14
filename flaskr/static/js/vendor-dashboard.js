// document.addEventListener('DOMContentLoaded', function() {
//     document.getElementById('submissionModal').addEventListener('bs.dismiss', function () {
//         // Target the form inside the modal and reset it
//         const form = this.querySelector('form');
//         console.log(form);
//         if (form) {
//             form.reset();
//         }
//     });
// });

document.querySelector('#submission-modal').addEventListener('click', async (event) => {
    const btn = event.target.closest('#modal-close');
    const form = document.getElementById('submission-form');

    if (!btn || !form) { return }
   
    form.reset();
});