
document.querySelector(".tickets").addEventListener('click', async (event) => {
    const btn = event.target.closest('.ticket-btn');
    const oldInput = document.querySelector('#modal-comment-field');

    //remove old comment field
    if (oldInput)
        oldInput.remove();

    if (!btn) return;

    //create comment field
    let commentInput = document.createElement('input');;
    commentInput.setAttribute("class", "form-control");
    commentInput.setAttribute("type", "text");
    commentInput.setAttribute("disabled", "");
    commentInput.setAttribute('id', 'modal-comment-field');

    //set comment field text
    if (btn.dataset.comments != "")
        commentInput.setAttribute("placeholder", btn.dataset.comments);
    else
        commentInput.setAttribute("placeholder", "No comments");

    //add comment field to modal
    modalBody = document.querySelector('.modal-body');
    modalBody.appendChild(commentInput);

    //id
    document.querySelector('#modal-ticket-id').textContent = btn.dataset.id;
    //timestamp
    document.querySelector('#modal-ticket-date').textContent = btn.dataset.date;
    //author
    document.querySelector('#modal-ticket-author').textContent = btn.dataset.author;
    //status
    document.querySelector('#modal-ticket-status').textContent = btn.dataset.status;

})