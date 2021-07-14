from django.shortcuts import render

# Create your views here.

def BootstrapFilterView(request):
    return render(request, "bootstrap_form.html")
