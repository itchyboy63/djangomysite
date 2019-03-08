from django.shortcuts import render


# Create your views here.
def index(request):
    #return HttpResponse('HELLO FROM YICHI')
    return render(request,'posts/index.html')
