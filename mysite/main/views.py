from django.shortcuts import redirect, render
from .models import *

# Create your views here.
def index(request):
    # template 폴더 안에 있는 폴더 및 html 파일의 경로를 설정
    return render(request, 'main/index.html')

def notice_list(request):
    # 모든 데이터 변수에 저장 : models.의 클래스 이름.object.all()
    # 데이터 베이스에 있는 Notice 정보를 모두 가져옴
    noticeList = Notice.objects.all()
    return render(request, 'main/notice_list.html', {'noticeList':noticeList})

def notice_view(request, pk):
    notice = Notice.objects.get(pk=pk)
    return render(request, 'main/notice_view.html', {'notice':notice})

def notice_add(request):
    if request.method == 'POST':
        new_notice = Notice.objects.create(                
            title = request.POST['title'],
            contents = request.POST['contents'],
            views = 0,       # 처음 생성 시 무조건 0이므로
        )
        return redirect('/notice/')
    return render(request, 'main/notice_add.html')

def notice_remove(request, pk):
    notice = Notice.objects.get(pk=pk)
    if request.method == 'POST':
        notice.delete()
        return redirect('/notice/')