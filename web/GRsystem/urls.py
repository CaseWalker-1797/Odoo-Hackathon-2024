from django.urls import path
from . import views
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('signin/', auth_views.LoginView.as_view(template_name='GRsystem/signin.html'), name='signin'),
    path('logout/', auth_views.LogoutView.as_view(template_name='Grsystem/logout.html'), name='logout'),
    path('logout/done/', auth_views.LogoutView.as_view(template_name='registration/logout_done.html'), name='logout_done'),
    # path('logout/',views.logout,name='logout'),
    path('password/', views.change_password, name='change_password'),
    path('passwords/', views.change_password_g, name='change_password_g'),
    path('counter/', views.counter, name='counter'),
    path('solved/', views.solved, name='solved'),
    path('login/', views.login, name='login'),
    path('list/', views.list, name='list'),
    path('pdf/', views.pdf_view, name='view'),
    path('pdf_g/', views.pdf_viewer, name='view'),

    # path('ment/', views.patient_ment, name='ment_list'),
    # path('result/', views.patient_result, name='result'),
    path('diagnosis/predict/', views.MakePredict, name='predict'),
    # path('result/ment/', views.MakeMent, name='ment'),
    path('diagnosis/', views.diagnosis, name='diagnosis'),
    
    path('council/',views.council, name='council'),
    path('getHelp/',views.getHelp, name='getHelp'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('login_redirect/', views.login_redirect, name='login_redirect'),
    path('slist/', views.slist,),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('complaints/', views.complaints, name='complaints'),
    path('allcomplaints/', views.allcomplaints, name='allcomplaints'),
    path('mentalhealthresource/',views.mentalhealthresource,name='mentalhealthresource'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='GRsystem/password_reset.html'
         ),
         name='password_reset'),
    path('password-reset-done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='GRsystem/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='GRsystem/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='GRsystem/password_reset_complete.html'
         ),
         name='password_reset_complete'),
]
