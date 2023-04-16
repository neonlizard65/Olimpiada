var select_subdivision = document.getElementById("subdivision");
var select_employee = document.getElementById("employee_fio");

select_subdivision.onchange = () => {
    subdivision = select_subdivision.value;
    fetch("http://127.0.0.1:5000/employee").then((response) =>{
        response.json().then((data) =>{
            optionHTML = '';
            for(employee of data){
                console.log(employee);
                if(employee.subdivisionId == subdivision){
                    optionHTML += '<option value="' + employee.employeeID + '">' + employee.fio + '</option>';
                }
            }
            select_employee.innerHTML = optionHTML;
        });
    });
}; 