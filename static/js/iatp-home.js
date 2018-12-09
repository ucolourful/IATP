//IATP 首页 JS
layui.use(['element', 'form', 'jquery', 'layer'], function () {
    let $ = layui.jquery;
    let layer = layui.layer;
    let form = layui.form;
    initProduct();

    $("#user-menu dd").on("click", function () {
        $(this).removeClass();
        if (this.id === "user-info") {
            layer.msg("基本资料");
        }
        if (this.id === "user-set") {
            layer.msg("个人设置")
        }
    });

    // 侧边导航栏监听
    $("#side-list li").on("click", function () {
        layer.msg($(this).attr("data-value"));
        $("#body-content").html($(this).attr("data-value"));
    });

    function initProduct() {
        $("select[name=product-search]").empty();
        $.ajax({
            type: "GET",
            url: "/products/",
        }).done(function (res) {
            var optionString = "<option value=\'\'>请搜索产品线</option>";
            var products = res.msg;
            for (var i = 0; i < products.length; i++) {
                optionString += "<option value=\'" + products[i].productname + "\'>" + products[i].productname + "</option>";
            }
            console.log(optionString);
            $("select[name=product-search]").append(optionString);
            form.render();
        });
    };
});``