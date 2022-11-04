$("form[name=contact-form]").submit(function(e){
    
    var $form = $(this);
    var $error = $form.find('.error');
    var data = $form.serialize();

    $.ajax({
        url:"/contact/",
        type:"POST",
        data:data,
        dataType: "json",
        success: function(res){
            alert(res.msg);
        },
        error: function(res){
            alert(res.responseJSON.error);
        }
    })
    
    $form[0].reset();
    e.preventDefault();

}); 


$("form[name=signup-form]").submit(function(e){
    
    var $form = $(this);
    var $error = $form.find('.error');
    var data = $form.serialize();

    $.ajax({
        url:"/user/signup/",
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
const gr = $("#greeting")[0];
const hour = new Date().getHours();
const welcomeTypes = ["Good Morning", "Good Afternoon", "Good Evening"];
let welcomeText = "";

if (hour < 12) welcomeText = welcomeTypes[0];
else if (hour < 18) welcomeText = welcomeTypes[1];
else welcomeText = welcomeTypes[2];

gr.innerHTML = welcomeText;

const year = new Date().getFullYear();
$('#cc')[0].innerHTML += year;


function show_signin() {
    $('#signin').removeClass('fbox-hidden');
    $('#login').addClass('fbox-hidden');    
}
function show_login() {
    $('#signin').addClass('fbox-hidden');
    $('#login').removeClass('fbox-hidden');    
}