const box = document.getElementById("newTicketCommentField");
const elm = document.getElementById("characterCount");

box.addEventListener("input", (e) => {
    elm.textContent = box.value.length;
});