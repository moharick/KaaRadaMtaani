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