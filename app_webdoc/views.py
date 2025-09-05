from django.shortcuts import render

def webdoc(request):
    return render(request, 'webdoc.html', {})
