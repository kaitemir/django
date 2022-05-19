from django.db import models

# Create your models here.
class News(models.Model):
    
    """ 
    эта модель описывает структуру новости в Базе Данных
    
    """
    title = models.CharField(max_length=50)
    desc = models.TextField(null=True, blank=True)
    author = models.CharField(max_length=150)
    create_date = models.DateTimeField(auto_now_add=True)
        
    class Meta:
        verbose_name = 'Новостъ'
        verbose_name_plural = 'Новости'
    
    def __str__(self):
        return f'id:{self.id} {self.title}'