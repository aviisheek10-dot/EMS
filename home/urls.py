from django.urls import path
from django.contrib.auth import views as auth_views
from .views import home,create_event,event_detail, join_event, cancel_seat,my_bookings,my_events,cancel_event
urlpatterns= [
    path('',home, name="home"),
    path('create_event/',create_event, name="create_event"),
    path('event/<int:event_id>/', event_detail, name='event_detail'),
    path('event/<int:event_id>/join/', join_event, name='join_event'),
    path('event/<int:event_id>/cancel/', cancel_event, name='cancel_event'),

    path('event/<int:event_id>/seat/cancel/', cancel_seat, name='cancel_seat'),
    path('my/bookings/', my_bookings, name='my_bookings'),
    path('my/events/', my_events, name='my_events'),

    path('forgot-password/', auth_views.PasswordResetView.as_view(
        template_name='password_reset.html'
    ), name='password_reset'),
 
    path('forgot-password/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='password_reset_done.html'
    ), name='password_reset_done'),
 
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='password_reset_confirm.html'
    ), name='password_reset_confirm'),
 
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='password_reset_complete.html'
    ), name='password_reset_complete'),
]