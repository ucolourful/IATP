//IATP 首页 JS
layui.use(['element', 'form', 'jquery', 'layer'], function () {
    let $ = layui.jquery;
    let layer = layui.layer;

    $("#user-menu dd").on("click",function () {
       $(this).removeClass();
       if ( this.id === "user-info" ){
           layer.msg("基本资料");
       }
       if ( this.id === "user-set" ){
           layer.msg("个人设置")
       }
    });

    // 侧边导航栏监听
    $("#side-list li").on("click", function () {
        layer.msg($(this).attr("data-value"));
        $("#body-content").html($(this).attr("data-value"));
    });
});