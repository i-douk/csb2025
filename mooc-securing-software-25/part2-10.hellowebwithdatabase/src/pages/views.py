from django.http import HttpResponse
from .models import Message


# Create your views here.

def homePageView(request):
	content = 'Hello Web!';

		
	return HttpResponse(content)

def dbMessageView(request):

	id = request.GET.get('id')

	contentarr = Message.objects.get(id__exact=id) 

	return HttpResponse(contentarr.content)
