from django.db import models

# Create your models here.
from main.models import Client


class TvProgram(models.Model):
    t_id = models.AutoField(primary_key=True)
    t_genre = models.CharField(max_length=100)
    t_title = models.TextField(default="")
    t_info = models.TextField(default="")
    t_age = models.IntegerField(default=0)
    t_director = models.CharField(max_length=100)
    t_season = models.IntegerField(default=0)
    t_episode = models.IntegerField(default=1)
    t_episode_title = models.TextField(default="")
    t_time = models.IntegerField(default=0)  # 기준 값 분
    t_cast = models.TextField(default="")
    t_date = models.DateField(default=0)  # save() 할 때 재 정의해서 데이터 값을 넣는다.
    t_episode_info = models.TextField(default="")
    t_file = models.TextField(default="")  # url.path 입력
    t_cid = models.ForeignKey(Client, on_delete=models.CASCADE)
    t_request_date = models.DateField(auto_now_add=True)
    t_state = models.IntegerField(default=0) # 0대기 1승인 2거절

def __str__(self):
    return str(self.t_id)+self.t_genre+self.t_title+self.t_info+str(self.t_age)+self.t_director+str(self.t_season)+str(self.t_episode)+\
           self.t_episode_title+str(self.t_time)+self.t_cast+str(self.t_date)+self.t_episode_info+self.t_file+\
           str(self.t_cid)+str(self.t_request_date)+str(self.t_state)