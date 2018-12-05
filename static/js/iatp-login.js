//IATP 登录页 JS
layui.use(['layer', 'jquery', 'element', 'form'], function () {
    let layer = layui.layer;
    let $ = layui.jquery;
    let form = layui.form;


// 监听登录按钮
    $("#login-submit").on("click", function () {
        // 验证用户名密码
        if ($.trim($("#username").val()) === "") {
            layer.msg("请输出用户名");
            return false;
        }
        if ($.trim($("#password").val()) === "") {
            layer.msg("请输入密码");
            return false;
        }

    });

// 监听重置按钮
    $("#login-reset").on("click", function () {
        $(".iatp-login-item-input").val("");
    });

// 监听回车键，触发登录事件
    $(document).keyup(function (event) {
        if (event.keyCode === 13) {
            $("#login-submit").trigger("click");
        }
    });
})
;