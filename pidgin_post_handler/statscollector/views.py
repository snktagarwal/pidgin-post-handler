# Create your views here.
from django.http import HttpResponse

def index(request):
  return HttpResponse("Pidgin! Stats collector URL API")

def collect(request):

  if request.method == 'GET':

    # Check if we have uname and im_service parameters
    q = request.GET
    print q
    if 'uname' in q and 'im_service' in q:
      response = 'Thanks <i>' + q.__getitem__('uname') + '</i> to submit report for im <i>' + q.__getitem__('im_service') + '</i>. Your request has been recorded'
      hr = HttpResponse(response)
    else: hr = HttpResponse('Incorrect GET request. Try /uname=xx&im_service=xx')

    return hr
