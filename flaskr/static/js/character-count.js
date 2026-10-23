const box = document.getElementById("newTicketCommentField");
const elm = document.getElementById("characterCount");

document.getElementById("newTicketCommentField").addEventListener("input", (e) => {
    elm.textContent = box.value.length;
});