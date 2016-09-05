from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Article(models.Model):
    STATUS_CHOICE = (
        ('d', 'Draft'),
        ('p', 'Published'),
    )

    # 以下为文章基本字段 #Travis
    # 文章基本信息,题目+摘要+正文
    title = models.CharField('标题', max_length=70)
    abstract = models.CharField('摘要', max_length=150, blank=False, null=False, help_text="必选,请勿空白")
    body = models.TextField('正文')
    title_pic = models.ImageField('题图', upload_to='pic_folder/', blank=True, null=True)

    # 作者信息,外键链接注册作者表
    author = models.ForeignKey('Author', verbose_name='作者', null=False)

    # 文章时间戳
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_modified_time = models.DateTimeField('创建时间', auto_now_add=True)

    # 文章统计量
    views = models.PositiveIntegerField('浏览量', default=0)
    thumbs = models.PositiveIntegerField('点赞量', default=0)

    # 文章分类,外键链接分类
    category = models.ForeignKey('Category', verbose_name='分类', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-last_modified_time']


class Category(models.Model):
    genre = models.CharField('类型', max_length=20)

    def __str__(self):
        return self.genre


class Author(models.Model):
    nick_name = models.CharField('昵称', max_length=20)

    def __str__(self):
        return self.nick_name