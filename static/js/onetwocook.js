  $(document).ready(function(){
  
    //Materialize - Dropdown feature in forms:
    $('select').material_select();
    
    //Allows user to print a recipe page:
    function print(){
        window.print();
    }
    
    $("#printButton").click(function(){
        print();
    });
    
    /*Allows full access users to upload photo of their recipe on 
    Add a Recipe page */
    function upload(){
        document.getElementById("uploadFile").multiple;
    }
    $("#uploadFile").click(function(){
        upload();
    });
    
    //Materialize - provides hint on function of feature:
    $('.tooltipped').tooltip();
    
    //Materialize - Side Navigation (Smaller screen viewing only):
    $(".button-collapse").sideNav();
    
    //Scores out completed methods one by one:
    $(".method-step1").click(function(){
        $(".method-step1").toggleClass("score");
    });
    $(".method-step2").click(function(){
        $(".method-step2").toggleClass("score");
    });
    $(".method-step3").click(function(){
        $(".method-step3").toggleClass("score");
    });
    $(".method-step4").click(function(){
        $(".method-step4").toggleClass("score");
    });
    $(".method-step5").click(function(){
        $(".method-step5").toggleClass("score");
    });
    $(".method-step6").click(function(){
        $(".method-step6").toggleClass("score");
    });
    $(".method-step7").click(function(){
        $(".method-step7").toggleClass("score");
    });
    $(".method-step8").click(function(){
        $(".method-step8").toggleClass("score");
    });
    $(".method-step9").click(function(){
        $(".method-step9").toggleClass("score");
    });
    $(".method-step10").click(function(){
        $(".method-step10").toggleClass("score");
    });
    
    //Activator for Extra Ingredients Input Rows:
    $("#ingredientRow2, #ingredientRow3, #ingredientRow4, #ingredientRow5, #ingredientRow6, #ingredientRow7, #ingredientRow8, #ingredientRow9, #ingredientRow10, #ingredientRow11, #ingredientRow12, #ingredientRow13, #ingredientRow14, #ingredientRow15, #ingredientRow16, #ingredientRow17, #ingredientRow18, #ingredientRow19, #ingredientRow20").hide();
    $("#ingredient1_name").keydown(function(){
      $("#ingredientRow2").show();
    });
    $("#ingredient2_name").keydown(function(){
      $("#ingredientRow3").show();
    });
    $("#ingredient3_name").keydown(function(){
      $("#ingredientRow4").show();
    });
    $("#ingredient4_name").keydown(function(){
      $("#ingredientRow5").show();
    });
    $("#ingredient5_name").keydown(function(){
      $("#ingredientRow6").show();
    });
    $("#ingredient6_name").keydown(function(){
      $("#ingredientRow7").show();
    });
    $("#ingredient7_name").keydown(function(){
      $("#ingredientRow8").show();
    });
    $("#ingredient8_name").keydown(function(){
      $("#ingredientRow9").show();
    });
    $("#ingredient9_name").keydown(function(){
      $("#ingredientRow10").show();
    });
    $("#ingredient10_name").keydown(function(){
      $("#ingredientRow11").show();
    });
    $("#ingredient11_name").keydown(function(){
      $("#ingredientRow12").show();
    });
    $("#ingredient12_name").keydown(function(){
      $("#ingredientRow13").show();
    });
    $("#ingredient13_name").keydown(function(){
      $("#ingredientRow14").show();
    });
    $("#ingredient14_name").keydown(function(){
      $("#ingredientRow15").show();
    });
    $("#ingredient15_name").keydown(function(){
      $("#ingredientRow16").show();
    });
    $("#ingredient16_name").keydown(function(){
      $("#ingredientRow17").show();
    });
    $("#ingredient17_name").keydown(function(){
      $("#ingredientRow18").show();
    });
    $("#ingredient18_name").keydown(function(){
      $("#ingredientRow19").show();
    });
    $("#ingredient19_name").keydown(function(){
      $("#ingredientRow20").show();
    });
    
    //Activator for Extra Method Steps Input Rows:
    $("#method_step2, #method_step3, #method_step4, #method_step5, #method_step6, #method_step7, #method_step8, #method_step9, #method_step10").hide();
    $("#method_step1").keydown(function(){
      $("#method_step2").show();
    });
    $("#method_step2").keydown(function(){
      $("#method_step3").show();
    });
    $("#method_step3").keydown(function(){
      $("#method_step4").show();
    });
    $("#method_step4").keydown(function(){
      $("#method_step5").show();
    });
    $("#method_step5").keydown(function(){
      $("#method_step6").show();
    });
    $("#method_step6").keydown(function(){
      $("#method_step7").show();
    });
    $("#method_step7").keydown(function(){
      $("#method_step8").show();
    });
    $("#method_step8").keydown(function(){
      $("#method_step9").show();
    });
    $("#method_step9").keydown(function(){
      $("#method_step10").show();
    });
    
    //Opening Modal - Deleting Recipe or Cuisine created by user
    $('.modal').modal();

    $(".scrollspy").scrollSpy();
    
    $('.tabs').tabs();
    
    $('#deleteInput').click(function(){
      document.getElementById('img_path').value = '';
    });
});