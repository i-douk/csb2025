from django.http import HttpResponse


# Create your views here.

def addPageView(request):
	first = request.GET.get('first')
	second = request.GET.get('second')
	return HttpResponse(int(first) + int(second))
	

def multiplyPageView(request):
	first = request.GET.get('first')
	second = request.GET.get('second')
	return HttpResponse(int(first) * int(second))
	
