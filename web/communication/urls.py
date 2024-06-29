from django.urls import path
from . import views

urlpatterns = [  
    path('grievance/<int:grievance_id>/', views.GrievanceDetailView.as_view(), name='grievance_detail'),
    path('grievance/<int:grievance_id>/send_message/', views.SendMessageView.as_view(), name='send_message'),
    path('message/<int:message_id>/reply/', views.ReplyToMessageView.as_view(), name='reply_to_message'),
]
