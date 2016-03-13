from django.db import models

class Author(models.Model):
    name = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length = 100) 

    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name_plural = 'categories'
    
class Tag(models.Model):
    name = models.CharField(max_length = 100) 
    
    def __str__(self):
        return self.name
    
class Article(models.Model):
    title = models.CharField(max_length = 1000)
    post = models.TextField()
    draft = models.BooleanField()
    publish_date = models.DateTimeField()
    author = models.ForeignKey(Author)
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag)

class Comment(models.Model):
    name = models.CharField(max_length = 200)
    email = models.CharField(max_length = 200)
    comment_text = models.TextField()
    article = models.ForeignKey(Article, on_delete = models.CASCADE)
