//Activator for Extra Ingredients Input Rows:
describe("Test for activating extra Ingredients Input Rows", function() {
    
    var ingredientFieldID = [ingredientRow2, ingredientRow8, ingredientRow14, ingredientRow20];
    var ingredientField = $("#"+ingredientFieldID).hide();
    
    expect(ingredientField).toHaveBeenCalledWith('ingredientRow2','ingredientRow8','ingredientRow14','ingredientRow20');
    
});

//Activator for Extra Method Step Input Rows:
describe("Test for activating extra Method Step Input Fields", function(){
    
    $("#method_step5").keyup(function(){
        $("#method_step6").show();
    });
    
})