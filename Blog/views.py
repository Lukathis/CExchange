from django.shortcuts import render,get_object_or_404
from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from Blog.models import Article, Category, Author

import markdown2

# Create your views here.


# class TestBootstrapView(ListView):
#     template_name = "bootstrap_test.html"

# 索引页
#   引用模板: Blog/index.html
#   上下文名字: article_list
class IndexView(ListView):
    template_name = 'Blog/index.html'
    context_object_name = 'article_list'

    def get_queryset(self):
        article_list = Article.objects.all()
        # !可在此加上body用markdown转换内容
        for article in article_list:
            article.body = markdown2.markdown(article.body, extras=['fenced-code-blocks'],)
        return article_list

# 详情页
#   引用模板: Blog/detail.html
#   上下文名字: article_detail
class ArticleDetailView(DetailView):
    model = Article
    template_name = 'Blog/detail.html'
    context_object_name = 'article_detail'
    # 将主键链接为url定位地中的关键字参数
    pk_url_kwarg = 'article_id'

    def get_object(self, queryset=None):
        article_detail = super(ArticleDetailView, self).get_object()
        # !可在此加上body用markdown转换内容
        article_detail.body = markdown2.markdown(article_detail.body, extras=['fenced-code-blocks'], )
        return article_detail

    # def detail(request, pk_id):
    #     detail_qs = get_object_or_404(Qs, pk=pk_id)
    #     return render(request, 'detail.html', {'detail': detail_qs})

# 分类页
#   引用模板: Blog/index.html
#   上下文名字: article_list
#   与索引页同用一个模板及标签名字
class CategoryView(ListView):
    template_name = 'Blog/index.html'
    context_object_name = 'article_list'

    def get_queryset(self):
        article_list = Article.objects.filter(category=self.kwargs['category_id'])
        # !可在此加上body用markdown转换内容
        for article in article_list:
            article.body = markdown2.markdown(article.body, extras=['fenced-code-blocks'], )
        return article_list

    # get_context_data可以额外传一些 *内容* 到 *模板*
    def get_context_data(self, **kwargs):
        kwargs['category_list'] = Category.objects.all().order_by('name')
        return super(CategoryView, self).get_context_data(**kwargs)
