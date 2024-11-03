from datetime import timezone
from django.db import models
from datetime import date

# Create your models here.
from applications.globals.models import ExtraInfo , DepartmentInfo

  
class SpecialRequest(models.Model):
    request_maker = models.ForeignKey(ExtraInfo, on_delete=models.CASCADE)
    request_date = models.DateTimeField(default=date.today)
    brief = models.CharField(max_length=20, default='--')
    request_details = models.CharField(max_length=200)
    upload_request = models.FileField(blank=True)
    status = models.CharField(max_length=50,default='Pending')
    remarks = models.CharField(max_length=300, default="--")
    request_receiver = models.CharField(max_length=30, default="--")

    def __str__(self):
        return str(self.request_maker.user.username)


class Announcements(models.Model):
    maker_id = models.ForeignKey(ExtraInfo, on_delete=models.CASCADE)
    ann_date = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=200)
    batch = models.CharField(max_length=40,default="Year-1")
    department = models.CharField(max_length=40,default="ALL")
    programme = models.CharField(max_length=10)
    upload_announcement = models.FileField(upload_to='department/upload_announcement', null=True, default=" ")
    def __str__(self):
        return str(self.maker_id.user.username)
    
class Information(models.Model):
    department = models.OneToOneField(
        DepartmentInfo,
        on_delete=models.CASCADE,
    )

    phone_number = models.BigIntegerField()
    email = models.CharField(max_length=200)
    facilites = models.TextField()
    labs = models.TextField()


class Lab(models.Model):
    department = models.OneToOneField(
        DepartmentInfo,
        on_delete=models.CASCADE,
    )
    location = models.CharField(max_length=200)  # Adjust max_length as needed
    name = models.CharField(max_length=100)  # Adjust max_length as needed
    capacity = models.IntegerField()  # You can adjust the field type if needed

    # def __str__(self):
    #     return f"{self.name} ({self.department})"  # Displays lab name with department for clarity

class Feedback(models.Model):
    department = models.CharField(max_length=50)  # no need to validate department name
    rating = models.CharField(max_length=20)
    remark = models.TextField()

    def __str__(self):
        return f"{self.department} - {self.rating}"