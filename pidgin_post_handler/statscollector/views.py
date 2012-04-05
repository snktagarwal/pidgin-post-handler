# Create your views here.
from django.http import HttpResponse
from statscollector.models import *

def index(request):
  return HttpResponse("Pidgin! Stats collector URL API")

def collect(request):

  if request.method == 'GET':

    # Check if we have uname and im_service parameters
    q = request.GET
    print q
    if 'uname' in q and 'im_service' in q:

      uname = q.__getitem__('uname')
      im_service = q.__getitem__('im_service')

      if im_service in IM_SERVICE_NICK:

        # Save the object to the DB
        user_sub = UserStatSub()
        user_sub.uname = uname
        user_sub.im_service = im_service
        user_sub.save()

        response = 'Thanks <i>' + uname + '</i> to submit report for im <i>' + im_service + '</i>. Your request has been recorded'
      else: response = 'im_service incorrect. Try ' + ' '.join(IM_SERVICE_NICK)
    else: response = 'Incorrect GET request. Try /uname=xx&im_service=xx'

    return HttpResponse(response)
