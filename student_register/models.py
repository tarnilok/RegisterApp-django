from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
class StudentInfo(models.Model):
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    mobile_number = PhoneNumberField(unique=True)
    
    GENDER = (
        ("female", "Female"),
        ("male", "Male"),
        ("other", "Other"),
    )
    
    gender=models.CharField(max_length=10, choices=GENDER)
    student_number = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50)
    
    PATH = {
        ("fullstack", "FullStack"),
        ("datascience", "DataScience"),
        ("awsdevops", "Aws&Devops")
    }
    
    path = models.CharField(max_length=20, choices=PATH)
    photo = models.ImageField(upload_to="profile_photos/", default="avatar.png")
    
    def __str__ (self):
        return f"{self.student_number} - {self.first_name} {self.last_name}"
    
    class Meta:
        ordering = ["student_number"]
        verbose_name_plural = "Student_List"
        db_table = "StudentInfo"
        
        
