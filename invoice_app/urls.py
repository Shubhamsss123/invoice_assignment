

from django.urls import path
from . import views
# from .views import GeneratePdf
urlpatterns = [
    path('new',views.trial,name='trial_name'),
    path('',views.invoice_home,name='invoice name'),
    path('submitted',views.submit_view,name='submit name'),
    # path('pdf/', GeneratePdf.as_view()), 
    
]
