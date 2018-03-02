from django.contrib import admin

from .models import Person, Contact,Address,PersonName,PersonChurch

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['name','dob','email','job','gender','company_name']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    '''
        Admin View for Contact
    '''
    list_display = ['phone_num','home_num','person']

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    '''
        Admin View for Address
    '''
    list_display = ['street1','street2','city','postal_code','person']

@admin.register(PersonName)
class PersonNameAdmin(admin.ModelAdmin):
    '''
        Admin View for PersonName
    '''
    list_display = ['k_fname','k_lname','e_fname','e_lname','person']


@admin.register(PersonChurch)
class PersonChurchAdmin(admin.ModelAdmin):
    '''
        Admin View for PersonChurch
    '''
    list_display = ['registered_date','vehicle_license','baptized_date','baptized_church','infant_baptized_church',
    'infant_baptized_date','person_status','position_type','last_church_name','last_church_leader',
    'friends_in_church','volunteer_experience','person']
