from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=40)
    image = models.URLField()
    
    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return f'{self.name}'
        

class Todo(models.Model):
    title = models.CharField(max_length=40)
    details = models.CharField(max_length=40)
    has_been_done = models.BooleanField(default=False)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_completion = models.DateTimeField(null=True)
    deadline_date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)