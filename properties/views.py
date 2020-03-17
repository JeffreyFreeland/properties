from django.http import HttpResponse
from django.views import generic

from .models import Property


# Create your views here.
def hello_world(request):
    return HttpResponse("<h1>Hello World</h1>")

class PropertiesIndex(generic.ListView):
    model = Property
    template_name = "properties/properties.html"
    paginate_by = 100

    def get_queryset(self):
        return Property.objects.all()