from django.shortcuts import redirect, render
from .models import Post

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def blog(request):
    # 모든 데이터 변수에 저장 : models.의 클래스 이름.object.all()
    postlist = Post.objects.all()
    return render(request, 'main/blog.html', {'postlist':postlist})

def posting(request, pk):
    # primary key(pk)를 이용하여 하나의 게시글만 검색
    post = Post.objects.get(pk=pk)
    return render(request, 'main/posting.html', {'post': post})

def new_post(request):
    # form 태그의 method가 POST이면 데이터 추가 실행, GET이면 new_post.html 화면으로 이동
    if request.method == 'POST':
        # 사진 파일이 존재하는 확인, 있으면 사진 파일 저장, 없으면 사진 파일 저장 안함
        if request.POST['mainphoto']:
            # postname, contents, mainphote 데이터를 DB에 저장
            new_article = Post.objects.create(
                # request.POST[name에 적은 값] => 웹페이지에서 적은 값을 가지고 오는 방식
                postname = request.POST['postname'],
                contents = request.POST['contents'],
                mainphoto = request.POST['mainphoto'],
            )
        else: 
            new_article = Post.objects.create(
                postname = request.POST['postname'],
                contents = request.POST['contents'],
            )
        # urls.py 파일에 있는 주소를 실행하는 기능
        return redirect('/blog/')
    return render(request, 'main/new_post.html')

def remove_post(request, pk):
    # 데이터 베이스에서 삭제할 행을 변수에 저장
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        # 데이터베이스에서 post에 저장된 행을 삭제
        post.delete()
        # 목록 페이지 실행
        return redirect('/blog/')
    # get 방식의 경우 remove_post.html 화면을 실행
    return render(request, 'main/remove_post.html', {'Post':post})