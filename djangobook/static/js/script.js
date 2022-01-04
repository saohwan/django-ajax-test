$(document).ready(function(){
    const loadForm = function () {
        const btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-book .modal-content").html("");
                $("#modal-book").modal("show");
            },
            success: function (data) {
                $("#modal-book .modal-content").html(data.html_form);
            }
        });
    };

    const saveForm = function () {
        const form = $(this);
        $.ajax({
            url: form.attr("action"),
            data: form.serialize(),
            type: form.attr("method"),  // 폼테그에 정의된 method 가 post or get 에 따라 자동 정의.
            dataType: 'json',
            success: function (data) {
                if (data.form_is_valid) {
                    $("#book-table tbody").html(data.html_book_list);
                    $("#modal-book").modal("hide");
                } else {
                    $("#modal-book .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };

    /* Binding */
    $(".js-create-book").click(loadForm);
    $("#modal-book").on("submit", ".js-book-create-form", saveForm);

    // Update book
    $("#book-table").on("click", ".js-update-book", loadForm);
    $("#modal-book").on("submit", ".js-book-update-form", saveForm);

    // Delete book
    $("#book-table").on("click", ".js-delete-book", loadForm);
    $("#modal-book").on("submit", ".js-book-delete-form", saveForm);

});