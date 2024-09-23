from django.db import models

# Create your models here.
class Notice(models.Model):
    id = models.AutoField(primary_key=True)     # 자동으로 증가하는 값
    title = models.CharField(max_length=200)            # 제목
    contents = models.TextField()                       # 내용
    views = models.IntegerField()                       # 조회수
    create_date = models.DateTimeField(auto_now=True)   # 생성일

    def __str__(self):
        return self.title