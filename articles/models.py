from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    img = models.ImageField(upload_to='', blank=True, null=True)
    thumbnail = ProcessedImageField(
        upload_to='',
        processors=[Thumbnail(100, 100)],  # 처리할 작업목록
        format='JPEG',  # 최종 저장 포맷
        options={'quality': 100},
        blank=True,
        null=True)  # 저장 옵션
