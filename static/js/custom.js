$(document).ready(function () {
    //JS for education header to toggle P element
    $(".ed").click(function () {
        $(".edPara").slideToggle("slow");
    });
    //will add red to h_line classes
    $("#h_line").hover(function () {
        $("#h_line").addClass("h3_color");
    });
    /*this will apply larger font size to the active h2 element
    by adding the h3_font_size class but
    not the other h3 elements by removing class h3_font_size from them*/
    $("#h_climate").hover(function () {
        $("#h_electric").removeClass("h3_font_size");
        $("#h_education").removeClass("h3_font_size");
        $("#h_climate").addClass("h3_font_size");

    });
    $("#h_electric").hover(function () {
        $("#h_climate").removeClass("h3_font_size");
        $("#h_education").removeClass("h3_font_size");
        $("#h_electric").addClass("h3_font_size");
    });
    $("#h_education").hover(function () {
        $("#h_climate").removeClass("h3_font_size");
        $("#h_electric").removeClass("h3_font_size");
        $("#h_education").addClass("h3_font_size");
    });
    //adds slideTogggle to buttons to toggle press_effect buttons open and closed
    $("#press_effect1").click(function () {
        $("#pressText1").slideToggle('slow');
    });
    $("#press_effect2").click(function () {
        $("#pressText2").slideToggle('slow');
    });
    $("#press_effect3").click(function () {
        $("#pressText3").slideToggle('slow');
    });
})
