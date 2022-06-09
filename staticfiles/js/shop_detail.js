// 변수 선언 부분
let option_list = '';
let option_selected = {};
let option_price = {};
let option_name = [];

// 옵션 선택 버튼 (보이기 - 안보이기)
$(document).on("click", ".product_detail_body_content_select_btn", function () {
    if ($(this).next().css("display") === "none") {
        $(this).next().show();
    } else {
        $(this).next().hide();
    }
});

// 옵션 선택시 옵션 보이기 기능
function show_option(a) {

    // 딕셔너리 만들어 줌
    if (!option_selected[a[2]]) {
        option_selected[a[2]] = 1;
    }
    if (!option_price[a[2]]) {
        option_price[a[2]] = a[1];
    }
    sum();
    dict_to_list(option_selected);

    // 옵션 수량 선택
    option_list += '<div class="price_plus">' + '<div class="price_plus_product_name">' + a[0]
        + '<div class="option_select_price">' + a[1] + '원' + '</div>' + '</div>'
        + '<div class="price_plus_nums">'
        + '<button onclick="del(' + a[2] + ')" class="btn_minus">-</button>'
        + '<div class="price_plus_product_price" id="count' + a[2] + '">' + option_selected[a[2]] + '</div>'
        + '<button onclick="add(' + a[2] + ')" class="btn_plus">+</button>' + '</div>' + '</div>'
    $('.temp').html(option_list);

}

// +버튼 누르면 동작
function add(a) {
    option_selected[a] += 1
    $(`#count` + a).html(option_selected[a])
    dict_to_list(option_selected);
    sum();
}

//-버튼 누르면 동작
function del(a) {
    if (option_selected[a] > 1) {
        option_selected[a] -= 1
    }
    $(`#count` + a).html(option_selected[a])
    dict_to_list(option_selected);
    sum();

}

// 총 가격
function sum() {
    let total_sum = 0;
    for (var i in option_selected) {
        total_sum += option_selected[i] * option_price[i]
    }
    $('.total_sum').html(total_sum + '원');
}

function dict_to_list(dict_temp) {
    let dict_list = '{'
    for (var i in dict_temp) {
        dict_list += '"' + i + '"' + ':' + dict_temp[i] + ', '
    }
    dict_list += '}'
    console.log(dict_list)
    $('.basket_selected').html(`<input type="hidden" name="basket_selected" value='` + dict_list + `'>`);
    $('.buy_selected').html(`<input type="hidden" name="buy_selected" value='` + dict_list + `'>`);
}

function chk_form(form_name) {
    document.getElementById(form_name).submit();
}

// 장바구니 버튼 누르면 ajax수행됨.
/*function basket() {

    console.log(option_selected)
    $.ajax({
        url: '/basket/',
        type: 'POST',
        data: option_selected,
        dataType: 'json',
        success: function (data) {
            console.log(data['option_dict'])
            $('.hidden_option').html('<input type="hidden" name="option_dict" value="' + data['option_dict'] + '">')
        }
    })
}*/
