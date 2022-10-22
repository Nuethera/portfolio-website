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
            window.location.href = "/dashboard/";
        },
        error: function(res){
            console.log(res);
            $error.text(res.responseJSON.error);
        }
    })
    
    e.preventDefault();

})

$("form[name=login-form]").submit(function(e){
    
    var $form = $(this);
    var $error = $form.find('.error');
    var data = $form.serialize();

    $.ajax({
        url:"../user/login/",
        type:"POST",
        data:data,
        dataType: "json",
        success: function(res){
            window.location.href = "/dashboard/";
        },
        error: function(res){
            console.log(res);
            $error.text(res.responseJSON.error);
        }
    })
    
    e.preventDefault();

}); 
document.getElementById("greeting");
const hour = new Date().getHours();
const welcomeTypes = ["Good Morning", "Good Afternoon", "Good Evening"];
let welcomeText = "";

if (hour < 12) welcomeText = welcomeTypes[0];
else if (hour < 18) welcomeText = welcomeTypes[1];
else welcomeText = welcomeTypes[2];

greeting.innerHTML = welcomeText;