const body = document.querySelector('body');
const modal = document.querySelector('.board_modal');
const btnOpenPopup = document.querySelectorAll('.image_click');
const closeBtn = modal.querySelector(".close-area")

function show(a) {
    let temp;
    temp = '<div class="board_modal_body_body"><div class="board_modal_body_img"><img class="board_modalimage"  src="' + a[0] + '"></div>' // 다이어리 이미지
    temp += '<div class="board_modal_body_body_content"><div class="writer"><img class="board_modal_user_image" src="' + a[1] + '">' // 닉네임 이미지
    temp += '<div class="board_modal_user_nickname">' + a[2] + '</div>' // 닉네임
    temp += '<div class="board_modal_share_date">' + a[3] + '</div></div>' // 공유 시간
    temp += '<div><div class="board_modal_content">' + a[4] + '</div></div>' // 내용
    temp += '</div></div>'
    $(".board_modal_close").html('X');
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

function like_button(diary_id) {
    console.log('hello!')

    $.ajax({
        url: 'likes',
        type: 'GET',
        data: {'diary_id': diary_id},
        dataType: 'json',
        success: function (a) {
            console.log('success')
            console.log('ㅋㅋ', a['status'])
            console.log(a['current_diary'])
        },
        error: function (error){
            console.log('error occured')
        }

    })
}

function share_status(status) {
    let share_status = status;
    let share_id = document.querySelector('input[name="share_id"]').value;

    $.ajax({
        url: 'share_status',
        type: 'GET',
        data: {
            'share_status': share_status,
            'share_id': share_id
        },
        dataType: 'json',
        success: function (data) {
            console.log(data['share'])
            if (data['share'] === 'True') {
                $(".modal_share").html(`<button class="send_btn" onclick="share_status('False')" type="button">공유중지</button>`);
            } else if (data['share'] === 'False') {
                $(".modal_share").html(`<button class="send_btn" onclick="share_status('True')" type="button">공유하기</button>`);
            }
        },
    })
}