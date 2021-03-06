from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from articles.models import Category, Tag, Article, Comment
from articles.forms import CommentForm


class ArticleListView(generic.ListView):
    template_name = 'articles/list.html'
    paginate_by = 10
    model = None
    category = None
    pk_url_kwarg = None
    
    def get_queryset(self):
        if self.model is not None:
            self.category = get_object_or_404(self.model, pk = self.kwargs[self.pk_url_kwarg])
            
            return self.category.article_set.order_by('-publish_date').exclude(draft = True) 
        else:
            return Article.objects.order_by('-publish_date').exclude(draft = True)
    
    def get_context_data(self, **kwаrgs):
        context = super(ArticleListView, self).get_context_data(**kwаrgs)
        
        if self.category is not None:
            context['title'] = self.category.name
            
        return context
        
class CategoryListView(ArticleListView):
    model = Category
    pk_url_kwarg = 'cat_id'
    
class TagListView(ArticleListView):
    model = Tag
    pk_url_kwarg = 'tag_id'

        
def article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    comments = article.comment_set.order_by('pk')
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        
        if form.is_valid():
            comment = form.save(commit = False)
            comment.article = article
            comment.save()
            
            return HttpResponseRedirect(reverse('articles:article', kwargs = {'article_id' : article_id}) + '#comment-' + str(comment.id))
    else:
        form = CommentForm()
        
    return render(request, 'articles/article.html', {
        'article'  : article,
        'comments' : comments,
        'form'     : form
    })
    
