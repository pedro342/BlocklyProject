from django.shortcuts import render

# Create your views here.
def BlocklyApp(request):
    return render(request, 'catalog/BlocklyApp.html')