from django.db import models

# Create your models here.
# 자료형 타입
# 숫자형 : IntegerField, FloatField
# 문자형 : CharField, TextField, EmailField, URLField
# 날짜형 : DateTimeField, DateField, TimeField
# 기타유형 : BooleanField, FileField, ImageField, NullBooleanField, SlugField

# 필드 속성
# primary_key : PK설정, PK 설정이 없을 경우 ID열을 자동 생성
# max_length : 데이터 길이 설정
# blank : 공백 허용 여부 (브라우저의 데이터가 없어도 됨을 의미)
# null : null 값 허용 여부 (DB에 null 값 저장 가능)
# default : 기본값 설정
class Post(models.Model):
    postname = models.CharField(max_length=50)
    contents = models.TextField()
    mainphoto = models.ImageField(blank=True, null=True)
    # Post 클래스를 문자열로 출력할 시 postname을 반환함
    def __str__(self):
        return self.postname