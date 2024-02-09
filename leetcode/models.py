from django.db import models



# Create your models here.
class Code(models.Model):
    # user_id, problem, code
    class Meta:
        app_label = "code"

    user_id = models.IntegerField()
    problem_id = models.IntegerField()
    code = models.TextField()