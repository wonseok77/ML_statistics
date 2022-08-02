from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import Curriculum

def index1(request):
    return HttpResponse('<u>Hello</u>')

def main(request):
    return HttpResponse('<u>Main</u>')

def index3(request):
    return HttpResponse('<u>환영합니다.</u>')

def index6(request):
    return HttpResponse('<u>안녕하세요~ 오늘은 비가 옵니다.</u>')


def insert_one(request):
    msg = ""
    # 줄바꿈 <br>
    #1-linux 입력
    Curriculum.objects.create(id=1, name='linux')
    msg += "1-linux 입력 성공 <br>"

    return HttpResponse(msg)

def insert(request):
    msg = ""
    # 줄바꿈 <br>
    #1-linux 입력
    Curriculum.objects.create(name='linux')
    msg += "1-linux 입력 성공 <br>"
    
    # 2-python 입력
    c = Curriculum(name='python')
    c.save()
    msg += "2-python 입력 성공 <br>"
        
    # 3-html/css/js 입력
    Curriculum(name='3-html/css/js').save()
    msg += "3-html/css/js 입력 성공 <br>"
        
    # 4-django 입력
    Curriculum(name='django').save()
    msg += "4-django 입력 성공 <br>"

    return HttpResponse(msg)

# first/show 
# 전체 조회
def show(request) :
    data = Curriculum.objects.all()
    
    msg = ""
    for dt in data :
        msg += dt.name + "<br>"
        
    return HttpResponse(msg)

# 한건 조회
# first/oneshow
def oneshow(request):
    onedata = Curriculum.objects.get(pk=3)
    return HttpResponse(onedata.name)

def show2(request):
    return render(
        request,
        "firstapp/show2.html",
        {}
    )
    
def show3(request):
    data = Curriculum.objects.all()
    
    return render(
        request,
        "firstapp/show3.html",
        {"data" : data}
    )
    
def show4(request):
    data = Curriculum.objects.all()
    
    return render(
        request,
        "firstapp/show4.html",
        {"data" : data}
    )
    
# 수정하기
def update(request):
    data = Curriculum.objects.get(pk=1)
    data.name = "linux_update"
    data.save()
    return HttpResponse("수정 성공")

# 삭제하기
def delete(request):
    data = Curriculum.objects.get(pk=1)
    data.delete()
    return HttpResponse("삭제 성공")