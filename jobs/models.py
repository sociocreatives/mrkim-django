from django.db import models

# Create your models here.
class Category(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='images/category/')
    name= models.CharField(max_length=50)
    description = models.TextField(null=True)

    class Meta:
        verbose_name_plural = "Main Categories"
    
    def __str__(self):
        return self.name

class MajorCategory(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='images/category/subcats')
    category = models.ForeignKey(Category, null=False, blank=False, on_delete=models.CASCADE)
    name= models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Major Sub Categories"
    
    def __str__(self):
        return self.name

        