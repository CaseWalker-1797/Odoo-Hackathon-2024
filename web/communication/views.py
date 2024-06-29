from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Grievance, Message, Thread
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from .models import Grievance

class GrievanceDetailView(DetailView):
    model = Grievance
    template_name = 'GRsystem/communication/grievance_detail.html'
    
    def get_object(self, queryset=None):
        grievance_id = self.kwargs.get('grievance_id')
        return get_object_or_404(Grievance, id=grievance_id)

class SendMessageView(LoginRequiredMixin, View):
    def post(self, request, grievance_id):
        content = request.POST['content']
        grievance = get_object_or_404(Grievance, pk=grievance_id)
        message = Message.objects.create(grievance=grievance, sender=request.user, content=content)
        return redirect('grievance_detail', grievance_id=grievance.id)

class ReplyToMessageView(LoginRequiredMixin, View):
    def post(self, request, message_id):
        content = request.POST['content']
        message = get_object_or_404(Message, pk=message_id)
        thread = Thread.objects.create(message=message, sender=request.user, content=content)
        return redirect('grievance_detail', grievance_id=message.grievance.id)
