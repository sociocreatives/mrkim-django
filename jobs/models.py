from django.db import models

# Create your models here.
class Category(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='images/category/')
    name= models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Category"
    
    def __str__(self):
        return self.name

        