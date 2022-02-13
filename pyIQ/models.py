from django.db import models

# Create your models here.

class Question(models.Model):
    """ Questions and options """
    question = models.CharField(max_length=255, null=True)
    opt_1 = models.CharField(max_length=200, null=True)
    opt_2 = models.CharField(max_length=200, null=True)
    opt_3 = models.CharField(max_length=200, null=True)
    opt_4 = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        """return string representation of our questions"""
        return '%s %s %s %s %s' % (self.question, self.opt_1 ,self.opt_2, self.opt_3 ,self.opt_4)
    
