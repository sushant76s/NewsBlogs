from django.db import models

# Create your models here.

class Blog(models.Model):
    blog_id = models.AutoField
    blog_image = models.ImageField(upload_to="blogImages", default='' ,null=True, blank=True)
    blog_title = models.CharField(max_length=200)
    blog_info = models.CharField(max_length=500)
    blog_date = models.DateField()


    # class Meta:
    #     ordering = ["-date_created"]

    def __str__(self):
        return self.blog_title
