from django.db import models

# Create your models here.
from main.models import Client


class MovieProgram(models.Model):
    m_id = models.AutoField(primary_key=True)
    m_genre = models.CharField(max_length=100)
    m_title = models.TextField(default="")
    m_info = models.TextField(default="")
    m_age = models.IntegerField(default=0)
    m_director = models.CharField(max_length=100)
    m_time = models.IntegerField(default=0)  # 기준 값 분
    m_cast = models.TextField(default="")
    m_date = models.DateField(default=0)  # save() 할 때 재 정의해서 데이터 값을 넣는다.
    m_file = models.TextField(default="")  # url.path 입력
    m_cid = models.ForeignKey(Client, on_delete=models.CASCADE)
    m_request_date = models.DateField(auto_now_add=True)
    m_state = models.IntegerField(default=0) # 0대기 1승인 2거절

def __str__(self):
    return str(self.m_id)+self.m_genre+self.m_title+self.m_info+str(self.m_age)+self.m_director+\
           str(self.m_time)+self.m_cast+str(self.m_date)+self.m_file+\
           str(self.m_cid)+str(self.m_request_date)+str(self.m_state)