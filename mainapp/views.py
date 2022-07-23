from django.shortcuts import render

# Create your views here.
def frontpage(request):
    context={}
    template_name ='mainapp/frontpage.html'
    return render(request, template_name, context)
def aboutpage(request):
    context={}
    template_name ='mainapp/aboutpage.html'
    return render(request, template_name, context)
def contactpage(request):
    context={}
    template_name ='mainapp/contactpage.html'
    return render(request, template_name, context)
