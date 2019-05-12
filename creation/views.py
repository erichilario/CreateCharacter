from django.shortcuts import render
from django.http import HttpResponse

def index_old(request):
	html_var = 'f strings'
	html_ = f"""<!DOCTYPE html>
	<html lang=en>

	<head>
	</head>
	<body>
	<h1>Create Character</h1>
	<p>This is where you create a {html_var} coming through</p>
	</body>
	</html>
	"""
	return HttpResponse(html_)

def index(request):
	#html_var = 'hi'
	return render(request, "base.html", {"html_var": True})
	#return HttpResponse("Create index")