function clear_fields(element){
    console.log('asdas');
    var form = document.getElementsByTagName("form")[0];

    var inputs = form.getElementsByTagName("input");

    for(var i = 0; i < inputs.length; i++){
        if(inputs[i].type != "submit"){
            inputs[i].value = "";
        }
    }

    var selects = form.getElementsByTagName("select");

    for(var i = 0; i < inputs.length; i++){
        selects[i].selectedIndex = 0;
    }
}