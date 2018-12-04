//IATP 登录页 JS
layui.use(['layer', 'jquery'], function () {
    let layer = layui.layer;
    let $ = layui.jquery;

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
        // ajax 异步验证用户名密码
        $("#login-submit").attr("disabled", "disabled");
        $("#login-submit").css("background-color", "grey");
        $.ajax({
            type: "POST",
            url: "/login/",
            data: {username: $.trim($("#username").val()), password: $.trim($("#password").val())}
        }).done(function (res) {
            layer.msg(res.msg);
            if (res.status === 0) {
                setTimeout("window.location.href='/home/'", 2000)
            } else {
                $("#login-submit").removeAttr("disabled");
                $("#login-submit").css("background-color", "#009688");
            }
        });
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
});