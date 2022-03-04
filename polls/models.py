from django.db import models

from django.db import models
# 위 구문은 삭제하면 안됨.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    free-type = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text
        # 이 함수는.. question_text에 문자열을 제대로 표현하기 위해 함수를 사용
