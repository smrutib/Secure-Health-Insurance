from django import forms

class upload_file_form(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

class claim_form(forms.Form):
    
    beneficiary_name = forms.CharField(max_length=100)
    beneficiary_id = forms.CharField(max_length=100)
    #provider_id = forms.IntegerField()
    speciality_description = forms.CharField(max_length=100)
    diagnosis_code = forms.IntegerField()
    submitted_amount = forms.IntegerField()
    amount_to_be_paid_by_medicare= forms.IntegerField()
    supplier_submitted_charges= forms.IntegerField()
    supplier_medicare_amount= forms.IntegerField()


