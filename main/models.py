from django.db import models

# Create your models here.
class User(models.Model):
    u_id = models.AutoField(primary_key=True)
    u_email = models.CharField(max_length=100)
    u_password = models.CharField(max_length=255)
    u_membership = models.CharField(max_length=10)
    u_credit_company = models.CharField(max_length=10)
    u_credit_number = models.CharField(max_length=16)
    u_credit_date = models.DateField(default=0)
    u_name = models.CharField(max_length=100)
    u_birth = models.DateField(default=0)

    def __str__(self):
        return str(
            self.u_id) + self.u_email + self.u_password + self.u_membership + self.u_credit_company + self.u_credit_number + \
               str(self.u_credit_date) + self.u_name + str(self.u_birth)

class Client(models.Model):
    c_id = models.AutoField(primary_key=True)
    c_email = models.CharField(max_length=100)
    c_password = models.CharField(max_length=255)
    c_name = models.CharField(max_length=100)
    c_phone = models.CharField(max_length=30)
    c_company = models.CharField(max_length=300)
    c_department = models.CharField(max_length=100)

    def __str__(self):
        return str(
            self.c_id) + self.c_email + self.c_password + self.c_name + self.c_phone + self.c_company + self.c_department
