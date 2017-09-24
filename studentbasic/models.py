from django.db import models

# Create your models here.


class Primary(models.Model):
    admin_no = models.IntegerField()
    name = models.CharField(max_length=25)
    kidato = models.IntegerField()
    darasa = models.CharField(max_length=1)
    dob = models.DateTimeField()
    kcpe_mark = models.IntegerField()
    county = models.CharField(max_length=10)
    year_of_completion = models.IntegerField()
    parent_contact = models.CharField(max_length=10)

    def __str__(self):
        return self.name

