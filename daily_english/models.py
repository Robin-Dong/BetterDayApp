from django.db import models


# Create your models here.
class DailyEnglish(models.Model):
    pic_url = models.CharField(max_length=200, verbose_name='图片链接', unique=True)
    created_time = models.CharField(max_length=20, verbose_name='图片原始时间')
    pub_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    display = models.PositiveIntegerField(default=0,verbose_name="展示次数")

    def __str__(self):
        return 'en_img'+str(self.id)

    class Meta:
        ordering = ["created_time"]
        verbose_name = "DailyEnglish"
        verbose_name_plural = "DailyEnglish"

    def increase_display(self):
        self.display += 1
        self.save(update_fields=['display'])


class DailyQuote(models.Model):
    quote = models.CharField(max_length=100, verbose_name='每日一句', unique=True)
    note = models.CharField(max_length=200, verbose_name='翻译', unique=True)
    pub_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    display = models.PositiveIntegerField(default=0, verbose_name="展示次数")

    def __str__(self):
        return 'quote' + self.pub_time.strftime("%y%m%d")

    class Meta:
        ordering = ["pub_time"]
        verbose_name = "DailyQuoto"
        verbose_name_plural = "DailyQuoto"

    def increase_display(self):
        self.display += 1
        self.save(update_fields=['display'])


class DailyImg(models.Model):
    title = models.CharField(max_length=50, verbose_name='图名')
    img_url = models.CharField(max_length=100, verbose_name='图片链接', unique=True)
    pub_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    display = models.PositiveIntegerField(default=0, verbose_name="展示次数")

    def __str__(self):
        return 'img' + self.pub_time.strftime("%y%m%d")

    class Meta:
        ordering = ["pub_time"]
        verbose_name = "DailyImg"
        verbose_name_plural = "DailyImg"

    def increase_display(self):
        self.display += 1
        self.save(update_fields=['display'])


