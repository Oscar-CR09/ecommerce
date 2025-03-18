from .models import Category


def menu_links(request):
    #links = list(Category.objects.all())
    links = Category.objects.all()
    #links = list(Category.objects.all().values('id', 'category_name', 'slug'))
    
    return dict(links=links)
