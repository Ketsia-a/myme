from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from tinymce.models import HTMLField
import datetime as dt
from phone_field import PhoneField
from django.dispatch import receiver

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=150)
    
    def __str__(self):
        return self.name

class Profile (models.Model):
    user = models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=128)
    status = models.ForeignKey(Department,null=False,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username
    
    @receiver(post_save, sender=User)
    def update_user_profile(sender, instance, created, **kwargs):
         if created:
            Profile.objects.create(user=instance)
            instance.profile.save()  

    @classmethod
    def filter_by_department(cls, department):
        problem = Problem.objects.filter(department__name=department).all()
        return problem    
        
        
class Problem(models.Model):
    names = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pics/',blank=True)
    description = HTMLField()
    phone = PhoneField(blank=True, help_text='Contact phone number')
    department = models.ForeignKey(Department,null=False,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        self.names
    
    
    def save_problem(self):
        self.save()    

    def delete_problem(self):
        self.delete()

    def __str__(self):
        return self.names
    
    @classmethod
    def filter_by_department(cls, department):
        problem = Problem.objects.filter(department__name=department).all()
        return problem   
    
    @classmethod
    def update_problem(cls,id,problem):
        update_image = cls.objects.filter(id = id).update(problem = problem)

        return update_image


class Tip(models.Model):
    pic = models.ImageField(upload_to='images/', blank=True)
    problem = models.ForeignKey(Problem,on_delete=models.CASCADE, related_name='tips', null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='tips')
    tip = models.TextField(max_length=500, blank=True, default='Stay safe, Do not panic help is on the way')
    created = models.DateTimeField(auto_now_add=True, blank=True)
    
    def save_tip(self):
        self.save()
    
    @classmethod
    def get_tip(cls):
        tips = Tip.objects.all()
        return tips       

    def delete_tip(self):
        self.delete() 
    
    def __str__(self):
        return self.tip
    
    class Meta:
        ordering = ["-pk"]