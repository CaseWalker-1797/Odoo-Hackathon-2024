from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

from django.core.validators import RegexValidator
from datetime import datetime

class Meta:

    app_label = 'GRsystem'
class Profile(models.Model):
    typeuser =(('employee','employee'),('hradmin', 'hradmin'))
    COL=(('Ahmedabad','Ahmedabad'),('Gandhinagar','Gandhinagar')) #change IT names
    user =models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    Branch=models.CharField(max_length=100,choices=COL,blank=False)
    phone_regex =RegexValidator(regex=r'^\d{10,10}$', message="Phone number must be entered in the format:Up to 10 digits allowed.")
    contactNumber = models.CharField(validators=[phone_regex], max_length=10, blank=True) 
    type_user=models.CharField(max_length=20,default='student',choices=typeuser)
    CB=(('IT Department',"IT Department"),('HR Department',"HR Department"),('Logistics Department',"Logistics Department"),('D Staff ',"D Staff "))
    Department=models.CharField(choices=CB,max_length=29,default='IT Department')
    def __str__(self):
        return self.Branch
    def __str__(self):
        return self.user.username
    
    

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

'''@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()'''


class Complaint(models.Model):
    STATUS =((1,'Solved'),(2, 'InProgress'),(3,'Pending'))
    TYPE=(('Workplace',"Workplace"),('Hardware',"Hardware"),('Management',"Management"),('IT',"IT"),('Other',"Other"))
    id = models.BigAutoField(primary_key=True)

    Subject=models.CharField(max_length=200,blank=False,null=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    
    Type_of_complaint=models.CharField(choices=TYPE,null=True,max_length=200)
    Description=models.TextField(max_length=4000,blank=False,null=True)
    Time = models.DateField(auto_now=True)
    status=models.IntegerField(choices=STATUS,default=3)
    
   
    def __init__(self, *args, **kwargs):
        super(Complaint, self).__init__(*args, **kwargs)
        self.__status = self.status

    def save(self, *args, **kwargs):
        if self.status and not self.__status:
            self.active_from = datetime.now()
        super(Complaint, self).save(*args, **kwargs)
    
    def __str__(self):
     	return self.get_Type_of_complaint_display()
    def __str__(self):
 	    return str(self.user)

class Grievance(models.Model):
    guser=models.OneToOneField(User,on_delete=models.CASCADE,default=None)
    id = models.BigAutoField(primary_key=True)
    def __str__(self):
        return self.guser
    

class Medical(models.Model):
    s1 = models.CharField(max_length=250,null=True)
    s2 = models.CharField(max_length=250,null=True)
    s3 = models.CharField(max_length=250,null=True)
    s4 = models.CharField(max_length=250,null=True)
    s5 = models.CharField(max_length=250,null=True)
    disease = models.CharField(max_length=200)
    medicine = models.CharField(max_length=200)
    patient = models.ForeignKey(
        User, related_name="patient", on_delete=models.CASCADE)
    doctor = models.ForeignKey(
        User, related_name="doctor", on_delete=models.CASCADE, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.disease

class Ment(models.Model):
    approved = models.BooleanField(default=False)
    time = models.CharField(max_length=200, null=True)
    patient = models.ForeignKey(
        User, related_name="pat", on_delete=models.CASCADE)
    doctor = models.ForeignKey(
        User, related_name="dor", on_delete=models.CASCADE, null=True)
    ment_day = models.DateTimeField(null=True)
    medical = models.ForeignKey(
        Medical, related_name="medical", on_delete=models.CASCADE, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.approved


class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}: {self.message}'



class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
