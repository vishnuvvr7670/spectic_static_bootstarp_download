from django.shortcuts import render

# Create your views here.
def specific_bootstrap_download(request):
    return render(request,'specific_bootstrap_download.html')