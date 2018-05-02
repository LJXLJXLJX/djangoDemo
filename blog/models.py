from django.db import models

# Create your models here.


'''
生成数据表
执行
python manage.py makemigrations blog(即应用名)
会生成migrations生成一个0001_initial.py
python manage.py migrate
model中到数据移植到刚刚创建到文件中
python manage.py sqlmigrate blog(应用名) 0001(文件id)
数据导入到db中
'''


class Article(models.Model):
    title = models.CharField(max_length=32, default='Title')
    content = models.TextField(null=True)
    pub_time = models.DateTimeField(null=True)

    def __str__(self):
        return self.title
