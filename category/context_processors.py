from .models import Category


def menu_links(request):
    #links = list(Category.objects.all())
    links = Category.objects.all()
    return dict(links=links)
