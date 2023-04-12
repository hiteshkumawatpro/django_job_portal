from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render(request , 'career.html')

def job(request):
    return render(request , 'Page-3.html')

def forms(request):
    return render(request , 'Page-4.html')

def formdata(request):
    if request.method == 'POST':
        appl_post= request.POST.get('select')
        firstname = request.POST.get('name-1')
        lstname = request.POST.get('name-2')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        street = request.POST.get('street')
        city = request.POST.get('city')
        country = request.POST.get('country')
        linked = request.POST.get('url')
        url = request.POST.get('url-1')
        message = request.POST.get('message')
        dic = {'var1' : appl_post , 'var2': firstname, 'var3' : lstname , 'var4':phone,
               'var5': email , 'var6' : street , 'var7': city , 'var8' : country , 'var9' : linked , 'var10': url , 'var11' : message}
    return render(request , 'Page-6.html' , dic)