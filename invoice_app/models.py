from django.db import models


# Create your models here.
class invoice_model(models.Model):

    name=models.TextField(max_length=200)
    thing=models.TextField(max_length=200)
    price=models.IntegerField()

    def __str__(self):
        return (
            f"{self.name} | {self.thing}"
        )
    


# importing the necessary libraries
from django.http import HttpResponse
from django.views.generic import View
from .process import html_to_pdf 

#Creating a class based view
class GeneratePdf(View):
     def get(self, request, *args, **kwargs):
         
        # getting the template
        pdf = html_to_pdf('invoice.html')
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')