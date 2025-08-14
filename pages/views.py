from django.shortcuts import render

# Create your views here.
def home_page_view(request):
    return render(request=request, template_name='home.html')

def contact_page_view(request):
    return render(request=request, template_name='pages/contact.html')