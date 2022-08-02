from django.shortcuts import render

# Create your views here.

def sample_01(request) :
    return render(
        request,
        "frontendapp/01_sample.html",
        {}
    )
    
def index_01(request) :
    return render(
        request,
        "frontendapp/01_index.html",
        {}
    )
    
def index_02(request) :
    return render(
        request,
        "frontendapp/02_index_css.html",
        {}
    )
    
def index_03(request) :
    return render(
        request,
        "frontendapp/03_index_css.html",
        {}
    )
    
def index_04(request) :
    return render(
        request,
        "frontendapp/04_index_css.html",
        {}
    )
    
def index_05(request) :
    return render(
        request,
        "frontendapp/05_index_css.html",
        {}
    )
    
def index_06(request) :
    return render(
        request,
        "frontendapp/06_index_css.html",
        {}
    )