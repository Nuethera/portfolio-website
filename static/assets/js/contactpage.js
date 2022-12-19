
$( document ).ready(function() {
    $('.dt').each(function() {
        a = $(this).text();
        d = Date.parse(a);
        dt = new Date(d);
        $(this).text(dt.toLocaleString('en-GB'));
    });
});