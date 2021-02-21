
$(document).ready(function() {


var addproof_fields = $("#addressproof");
addproof_fields.hide();

var sales_fields= $("#sales");
sales_fields.hide();

var cctv_fields= $("#cctv");
cctv_fields.hide();




$('#id_request_type').change(function() {
    if ($(this).val() == "AddressProof") {
        addproof_fields.show();
    } else {
        addproof_fields.hide();
    }
    if ($(this).val() == "SalesAgreement") {
        sales_fields.show();
    } else {
        sales_fields.hide();
    }
    if ($(this).val() == "CCTV") {
        cctv_fields.show();
    } else {
        cctv_fields.hide();
    }
    
    
    

});


    
 });




