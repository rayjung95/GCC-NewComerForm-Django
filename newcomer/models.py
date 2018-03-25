from django.db import models

class Person(models.Model):
    # id = models.AutoField(primary_key=True)
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female')]
    name = models.CharField(max_length=100)
    dob = models.CharField(max_length=30)
    email = models.CharField(max_length=50, blank=True)
    job = models.CharField(max_length=30, blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1, blank=True)
    company_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Contact(models.Model):
    phone_num = models.CharField(max_length=100)
    home_num = models.CharField(max_length=100)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

class Address(models.Model):
    street1 = models.CharField(max_length=100)
    street2 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

class PersonName(models.Model):
    k_fname = models.CharField(max_length=100)
    k_lname = models.CharField(max_length=100)
    e_fname = models.CharField(max_length=100)
    e_lname = models.CharField(max_length=100)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

class PersonChurch(models.Model):
    registered_date = models.DateField(auto_now_add=True)
    vehicle_license = models.CharField(max_length=100)
    baptized_date = models.CharField(max_length=100)
    baptized_church = models.CharField(max_length=100)
    infant_baptized_church = models.CharField(max_length=100)
    infant_baptized_date = models.CharField(max_length=100)
    person_status = models.CharField(max_length=100)
    position_type = models.CharField(max_length=100)
    last_church_name = models.CharField(max_length=100)
    last_church_leader = models.CharField(max_length=100)
    friends_in_church = models.CharField(max_length=100)
    volunteer_experience = models.CharField(max_length=100)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
