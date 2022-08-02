from django.http import HttpResponse
from django.shortcuts import render
from .model import survey



def view_Test(request) :
    return render(
        request,
        "chi2app/test.html",
        {"msg":"ok"}
    )


# Create your views here.
# 주문내역 전체 조회(리스트+튜플 사용)
def view_DB_Test(request):
    
    df = survey.getDBTest()

    #return HttpResponse(df)

    context = {"msg" : df}

    return render(
        request,
        "chi2app/test.html",
        context
    )
    
# survey 테이블 생성하기
def createTable(request) :
    survey.createTableSurvey()
    
    return HttpResponse("Create OK....")