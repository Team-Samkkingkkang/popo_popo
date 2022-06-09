const body = document.querySelector('body');
const modal = document.querySelector('.board_modal');
const btnOpenPopup = document.querySelectorAll('.image_click');

function show(a) {
    console.log(a[0])
    $(".board_temp").html('<img class="board_modal_image" src="'+a[0]+'">');
}


for (var btn in btnOpenPopup) {
    btnOpenPopup[btn].addEventListener('click', () => {
        modal.classList.toggle('show');

        if (modal.classList.contains('show')) {
            body.style.overflow = 'hidden';
        }
    });

    modal.addEventListener('click', (event) => {
        if (event.target === modal) {
            modal.classList.toggle('show');

            if (!modal.classList.contains('show')) {
                body.style.overflow = 'auto';
            }
        }
    });
}