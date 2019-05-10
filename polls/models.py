from django.db import models

# 创建两个模型，Question 和 Choice
# Question有两个字段：问题和出版日期
# Choice有两个字段：选择文本和投票纪录


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)