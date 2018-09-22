from django.db import models

# Create your models here.
def test(models.Model):
	x = models.CharField(blank = True)
	y = models.IntegerField(null = True)
	z = models.CharField(default = 'F')
	w = models.DateTimeField(auto_now = True)

