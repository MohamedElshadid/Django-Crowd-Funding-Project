from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Comments(models.Model):
    comment_id = models.AutoField(primary_key=True)
    comment_body = models.CharField(max_length=60)
    project = models.ForeignKey("project.Project",on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)


# Repor Project Model
class ReportComment(models.Model):
    report_id = models.AutoField(primary_key=True)
    report_content = models.CharField(max_length=255)
    comment = models.ForeignKey("Comments",on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)