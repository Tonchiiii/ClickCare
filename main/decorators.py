from django.shortcuts import redirect
from .models import Record

def checkup_done(view_func):
	def wrapper_func(request, *args, **kwargs):		
		user_record = Record.objects.get(user=request.user)
		validation_record = user_record.validation_abstract
		if validation_record:
			return redirect('main-home')
		else:
			return view_func(request, *args, **kwargs)
	return wrapper_func
    #change main-home to results page's name in urls.py