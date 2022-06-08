function chk_form(form_name) {
    document.getElementById(form_name).submit();
}

function show(a) {
    $(".modal_content").html(a[0]);
    $(".modal_date").html(a[1]);
    $(".modal_img").html('<img src="' + a[2] + '" class="diary_img">');
    $(".modal_update").html('<a href="' + a[3] + '">수정하기</a>');
    $(".modal_delete").html('<a href="' + a[4] + '">삭제하기</a>');
    $(".modal_id").html('<input type="hidden" name="share_id" value="' + a[5] + '">');

    if (a[6] === "False") {
        $(".modal_share").html(`<button class="send_btn" onclick="share_status('True')" type="button">공유 하기</button>`);
    } else if (a[6] === "True") {
        $(".modal_share").html(`<button class="send_btn" onclick="share_status('False')" type="button">공유 중지</button>`);
    }
}

const body = document.querySelector('body');
const modal = document.querySelector('.modal');
const btnOpenPopup = document.querySelectorAll('.diary_image');

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
        }
    })
}
