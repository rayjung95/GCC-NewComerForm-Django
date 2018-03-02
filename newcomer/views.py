from django.shortcuts import render
from django.http import HttpResponse
from .models import Person, Address, Contact, PersonName, PersonChurch
from django.http import Http404

from .forms import NewComerForm


def home(request):
    persons = Person.objects.all()
    addresses = Address.objects.all()
    return render(request, 'home.html', {'persons':persons})

def person_detail(request,id):
    try:
        person = Person.objects.get(id=id)
    except Person.DoesNotExist:
        raise Http404('Person not found')
        
    return render(request,'person_detail.html',{'person':person})


def register(request):
    sent=False
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NewComerForm(request.POST)
        # check whether it's valid:
        if form.is_valid():

            k_fname = form.cleaned_data['k_fname']
            k_lname = form.cleaned_data['k_lname']
            e_fname = form.cleaned_data['e_fname']
            e_lname = form.cleaned_data['e_lname']

            email = form.cleaned_data['email']
            dob = form.cleaned_data['dob']
            job = form.cleaned_data['job']
            company_name = form.cleaned_data['company_name']
            phone_num = form.cleaned_data['phone_num']
            home_num = form.cleaned_data['home_num']
            street1 = form.cleaned_data['street1']
            street2 = form.cleaned_data['street2']
            city = form.cleaned_data['city']
            postal_code = form.cleaned_data['postal_code']

            vehicle_license = form.cleaned_data['vehicle_license']
            baptized_date = form.cleaned_data['baptized_date']
            baptized_church = form.cleaned_data['baptized_church']
            infant_baptized_church = form.cleaned_data['infant_baptized_church']
            infant_baptized_date = form.cleaned_data['infant_baptized_date']
            person_status = form.cleaned_data['person_status']
            position_type = form.cleaned_data['position_type']
            last_church_name = form.cleaned_data['last_church_name']
            last_church_leader = form.cleaned_data['last_church_leader']
            friends_in_church = form.cleaned_data['friends_in_church']
            volunteer_experience = form.cleaned_data['volunteer_experience']


            save_person = Person(name=k_fname+" "+k_lname, dob=dob, email=email, job=job, company_name=company_name)
            save_person.save()
            save_contact = Contact(phone_num=phone_num, home_num=home_num, person=save_person)
            save_contact.save()
            save_address = Address(street1=street1, street2=street2, city=city, postal_code=postal_code, person=save_person)
            save_address.save()
            save_personname = PersonName(k_fname=k_fname, k_lname=k_lname, e_fname=e_fname, e_lname=e_lname, person=save_person)
            save_personname.save()
            save_personchurch = PersonChurch(vehicle_license=vehicle_license,baptized_date=baptized_date,
            baptized_church=baptized_church,infant_baptized_church=infant_baptized_church,infant_baptized_date=infant_baptized_date,
            person_status=person_status,position_type=position_type,last_church_name=last_church_name,last_church_leader=last_church_leader,
            friends_in_church=friends_in_church,volunteer_experience=volunteer_experience,person=save_person)
            save_personchurch.save()
            



            sent = True

            for x in form.cleaned_data:
                # print ("if %s: %s") % (x, form.cleaned_data[x])
                print (x+" : "+ str(form.cleaned_data[x]))



            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NewComerForm()
    return render(request,'register.html',{'sent':sent})



# def get_name(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = NameForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             name = form.cleaned_data['your_name']
#             print(name)
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
            

#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = NameForm()

#     return render(request, 'name.html')



