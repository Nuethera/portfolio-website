$("form[name=signup-form]").submit(function(e){
    
    var $form = $(this);
    var $error = $form.find('.error');
    var data = $form.serialize();

    $.ajax({
        url:"../user/signup/",
        type:"POST",
        data:data,
        dataType: "json",
        success: function(res){
            window.location.href = "/";
        },
        error: function(res){
            console.log(res);
            $error.text(res.responseJSON.error);
        }
    })
    
    e.preventDefault();

})