# importing the necessary libraries
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa  

# defining the function to convert an HTML file to a PDF file
def html_to_pdf(template_src, context_dict={}):
     template = get_template(template_src)
     html  = template.render(context_dict)
     result = BytesIO()
     pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
     if not pdf.err:
         return HttpResponse(result.getvalue(), content_type='application/pdf')
     return None










# from io import BytesIO
# from django.template.loader import get_template
# import xhtml2pdf.pisa as p
# import uuid
# from django.conf import settings

# def save_pdf(param:dict):
#     template=get_template('invoice.html')
#     html=template.render(param)
#     response=BytesIO()
#     pdf=p.pisaDocument(BytesIO(html.encode('UTF-8')),response)
#     file_name=uuid.uuid4

#     try:
#         with open(str(settings.BASE_DIR)+'media/pdfs/{file_name}.pdf','wb+') as
#             pdf=p.pisaDocument(BytesIO(html.encode('UTF-8')),output)
#     except Exception as e:
#         print(e)

#     if pdf.err:
#         return '',False
#     else:
#         return file_name,True
        




