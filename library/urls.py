from django.urls import path
from .views import Home,Admin,Student,adminsignup_view,adminsignin_view,addbook_view,BookView,adminclick_view

urlpatterns = [
	path('home/',Home,name='home'),
	path('admin/',Admin,name='admin'),
	path('student/',Student,name='student'),
	path('adminsignup/',adminsignup_view,name='adminsignup'),
	path('addbook/',addbook_view,name='addbook'),
	path('bookview/',BookView,name='bookview'),
    path('login/',adminclick_view,name='login'),
    ]