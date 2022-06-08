const body = document.querySelector('body');
const modal = document.querySelector('.board_modal');
const btnOpenPopup = document.querySelectorAll('.image_click');

function show(a) {
    let temp;
    temp = '<div><img class="board_modal_image" style="width: 3rem" src="'+a[0]+'"></div>' // 다이어리 이미지
    temp += '<div><div><img class="board_modal_user_image" src="'+a[1]+'">' // 닉네임 이미지
    temp += '<div class="board_modal_user_nickname">'+a[2]+'</div>' // 닉네임
    temp += '<div class="board_modal_share_date">'+a[3]+'</div></div>' // 공유 시간
    temp += '<div><div class="board_modal_content">'+a[4]+'</div></div>' // 내용
    temp += '</div>'
    $(".board_modal_body").html(temp);
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