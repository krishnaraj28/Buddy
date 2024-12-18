from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from .import views
urlpatterns = [
    path("home/", views.index),
    path("about/", views.about),
    path("service/", views.service),
    path('register/', views.register),
    path('login/', views.user_login),
    path('registration-success/', views.registration_success, name='registration_success'),
    path('userdashboard/', views.user_dashboard_view),
    path('admindashboard/', views.admin_dashboard_view),
    path('logout/', views.custom_logout, name='logout'),
    path('account/', views.my_account, name='myaccount'),
    path('profile/', views.view_profile, name='view_profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('createprofile/', views.create_profile, name='create_profile'),
    path('create_event/', views.create_event, name='create_event'),
    path('event_success/', views.event_success, name='event_success'),

    path('event_list/', views.event_list, name='event_list'),
    path('upcoming_events/', views.upcoming_events, name='upcoming_events'),
    
    path('event_detail/', views.event_detail, name='event_detail'),
    path('cancel/<int:event_id>/', views.delete_event, name='delete_event'),


    path('uploadresourse/', views.upload_resource, name='upload_resource'),
    path('resourselist/', views.resource_list, name='resource_list'),
    #path('resourse_success/', views.resourse_success, name='resourcesucess'),

    path('<int:resource_id>/like/', views.like_resource, name='like_resource'),
    path('searchresourse/', views.resource_search, name='search_resource'),

     path('resourse_detail/', views.resourse_detail, name='resourse_detail'),
    path('<int:resourse_id>/cancel/', views.delete_resourse, name='delete_resourse'),

    path('submit/', views.quiz, name='submit_quiz'),
    path('quiz/', views.quiz, name='quiz'),


    path('book/', views.book_appointment, name='book_appointment'),
    path('list/', views.appointment_list, name='appointment_list'),

    
    path('appointment_detail/', views.appointment_detail, name='appointment_detail'),

    path('<int:appointment_id>/', views.appointment_detail, name='appointment_detail'),
    path('<int:appointment_id>/accept/', views.accept_appointment, name='accept_appointment'),
    path('<int:appointment_id>/reject/', views.reject_appointment, name='reject_appointment'),
    path('b_cancel/<int:appointment_id>/', views.cancel_booking, name='cancel_booking'),

    path('faculty/', views.doc_list, name='doc_list'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


