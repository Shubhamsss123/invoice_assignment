from django.shortcuts import render,HttpResponse,redirect
from .models import invoice_model
# importing the necessary libraries
from django.http import HttpResponse
from django.views.generic import View
from .process import html_to_pdf 
from django.template.loader import render_to_string


def trial(request):
    return render(request,'home.html')

def invoice_home(request):
    
    if request.method=='POST':
        print(
            'request is post'
        )
       
        n=request.POST.get('name','')
        thing=request.POST.get('thing','')
        price=request.POST.get('price','')

        data=invoice_model(name=n,thing=thing,price=price)
        data.save()
        import datetime as t
        d=t.date.today()
        
        # return HttpResponse(f'your name is {name} and thing you buied is {thing} price is {price}')
        list={'name':n,'thing':thing,'price':price,'date':d}
        
            # list={'name':data.name,'thing':data.thing,'price':data.price}
        open('templates/pdf_new.html', "w").write(render_to_string('templates/pdf.html', list))
        # return render(request,'pdf_new.html')
        pdf = html_to_pdf('pdf_new.html')
            
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')
        # return render(request,'after.html',list)
        # return HttpResponse('dont used function')
    else:
        
        print('data is not saved')
    
        return render(request,'invoice.html')

def submit_view(request):
   
    return HttpResponse('we are not accepting response')




#Creating a class based view
# class GeneratePdf(View):
#      def get(self, request, *args, **kwargs):
         
#         # getting the template
#         data = invoice_model.objects.all().get(name=n)
#         print('hi',data.name)
#         print(data.thing)
#         print(data.price)
#         # list={'name':data.name,'thing':data.thing,'price':data.price}
#         open('templates/pdf_new.html', "w").write(render_to_string('templates/pdf.html', {'data': data}))
#         pdf = html_to_pdf('pdf_new.html')
         
#          # rendering the template
#         return HttpResponse(pdf, content_type='application/pdf')






# # Create your views here.
