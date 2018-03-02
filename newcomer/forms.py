from django import forms
    
GENDER_CHOICES = [('M', 'Male'), ('F', 'Female')]
class NewComerForm(forms.Form):

    # name = forms.CharField(max_length=100)
    dob = forms.DateField()
    email = forms.EmailField()
    job = forms.CharField(max_length=30, required=False)
    # gender = forms.MultipleChoiceField(required=False,choices=GENDER_CHOICES)
    company_name = forms.CharField(max_length=100, required=False)

    phone_num = forms.CharField(max_length=100)
    home_num = forms.CharField(max_length=100)

    street1 = forms.CharField(max_length=100)
    street2 = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    postal_code = forms.CharField(max_length=100)

    k_fname = forms.CharField(max_length=100)
    k_lname = forms.CharField(max_length=100)
    e_fname = forms.CharField(max_length=100)
    e_lname = forms.CharField(max_length=100)

    vehicle_license = forms.CharField(max_length=100)
    baptized_date = forms.DateField()
    baptized_church = forms.CharField(max_length=100)
    infant_baptized_church = forms.CharField(max_length=100)
    infant_baptized_date = forms.DateField()
    person_status = forms.CharField(max_length=100)
    position_type = forms.CharField(max_length=100)
    last_church_name = forms.CharField(max_length=100)
    last_church_leader = forms.CharField(max_length=100)
    friends_in_church = forms.CharField(max_length=100)
    volunteer_experience = forms.CharField(max_length=100)
