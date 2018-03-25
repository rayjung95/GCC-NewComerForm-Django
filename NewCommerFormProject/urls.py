
from django.conf.urls import url
from django.contrib import admin
from newcomer import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.home, name='home'),
    url(r'^person/(\d+)/', views.person_detail, name='person_detail'),
    url(r'^register/', views.register, name='register'),
    # url(r'^register/', views.get_name, name='get_name')
]







