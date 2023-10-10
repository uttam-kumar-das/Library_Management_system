
from django.contrib import admin
from django.urls import path
from library.views import *
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home, name='home'),
    path('addbook/',Add_book, name='addbook'),
    path('admin_home',admin_home, name='admin_home'),
    path('viewbook/',viewbook, name='viewbook'),
    path('returnbook/(?P<pid>[0-9]+)',returnbook,name='returnbook'),
    path('issuebook/',Issue_Book, name='issuebook'),
    path('Adminlogin/', Adminlogin, name='loginadmin'),
    path('signupstudent/',Signup_student, name='signupstudent'),
    path('registerstudent/',Registerstudent, name='registerstudent'),
    path('studentlogin/',Student_login, name='studentlogin'),
    path('vieworder/',ViewOrder, name='vieworder'),
    path('viewissue/',Viewissue, name='viewissue'),
    path('viewprofile/(?P<pid>[0-9]+)',viewprofile, name='viewprofile'),
    path('fine/(?P<pid>[0-9]+)',Fine,name='fine'),
    path('editprofile/(?P<pid>[0-9]+)',edit,name='editprofile'),
    path('editstudent/(?P<pid>[0-9]+)',editstudent,name='editstudent'),
    path('editbook/(?P<pid>[0-9]+)',edit_book,name='editbook'),
    path('deletestudent/(?P<pid>[0-9]+)',deletestudent,name='deletestudent'),
    path('deletebook/(?P<pid>[0-9]+)',bookdelete,name='deletebook'),
    path('fine2/(?P<pid>[0-9]+)',Fine2,name='fine2'),
    path('logout/',Logout,name='logout'),
    path('viewstudent/',viewstudent, name='viewstudent')


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

