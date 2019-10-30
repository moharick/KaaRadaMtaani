from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Mtaa(models.Model):
    mtaa_name = models.CharField(max_length=30)

    def create_mtaa(self):
        self.save()

    def delete_mtaa(self):
        self.delete()

    @classmethod
    def find_mtaa(cls,mtaa_id):
        mtaa = cls.objects.get(id=mtaa_id)
        return mtaa

    def update_mtaa(self,name):
        self.name = name
        self.save()


    def __str__(self):
        return f'{self.mtaa_name}'

class UserProfile(models.Model):
    first_name = models.CharField(max_length=20,blank=True)
    last_name = models.CharField(max_length=20,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    location = models.CharField(max_length=30,blank=True)
    mtaa_name = models.ForeignKey('Mtaa',on_delete=models.CASCADE,null=True,blank=True)

    def assign_mtaa(self,mtaa):
        self.mtaa= mtaa
        self.save()

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def __str__(self):
        return f'{self.user.username}'

class Biz(models.Model):
    name = models.CharField(max_length=30)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    biz_location = models.CharField(max_length=30,blank=True)
    biz_mtaa = models.ForeignKey('Mtaa',on_delete=models.CASCADE)
    email = models.EmailField()

    def create_biz(self):
        self.save()

    def delete_biz(self):
        self.delete()

    @classmethod
    def find_biz(cls,biz_id):
        biz = cls.objects.get(id=biz_id)
        return biz

    def update_biz(self,name):
        self.name = name
        self.save()

    def __str__(self):
        return f'{self.name}'