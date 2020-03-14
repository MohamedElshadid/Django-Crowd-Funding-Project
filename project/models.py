from django.db import models
# Create your models here.
class Project(models.Model):
    
    p_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=40)
    details = models.CharField(max_length=200)
    total_target = models.IntegerField()
    current_amout = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    tags = models.CharField(max_length=200)
    category = models.ForeignKey("category.Category",on_delete=models.CASCADE,null=True)
    user = models.ForeignKey("user.User",on_delete=models.CASCADE,null=True)


# Image Class
class Images(models.Model):
    image_id = models.AutoField(primary_key=True)
    image_name = models.ImageField(upload_to='images/')
    project = models.ForeignKey("Project",on_delete=models.CASCADE,null=True)


# Donation Model
class Donation(models.Model):
    donate_id = models.AutoField(primary_key=True)
    donate_amount = models.IntegerField()
    proejct = models.ForeignKey("Project",on_delete=models.CASCADE,null=True)


# Repor Project Model
class Report(models.Model):
    report_id = models.AutoField(primary_key=True)
    report_content = models.CharField(max_length=255)
    proejct = models.ForeignKey("Project",on_delete=models.CASCADE,null=True)
    user = models.ForeignKey("user.User",on_delete=models.CASCADE,null=True)