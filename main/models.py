from django.db import models
from django.urls import reverse

# Create your models here.

class Company(models.Model):
    cname = models.CharField(max_length=60)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    logo = models.ImageField(upload_to="company_logos/")
    webpage = models.URLField(null=True, blank=True, max_length=200)
    const_center = models.PositiveSmallIntegerField()
    

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companys"

    def __str__(self):
        return self.cname

    def get_absolute_url(self):
        return reverse("Company_detail", kwargs={"pk": self.pk})
    


