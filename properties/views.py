from django.http import HttpResponse
from django.views import generic

from django_tables2 import SingleTableView

from .models import Property
from .tables import PropertyTable


# Create your views here.
def hello_world(request):
    return HttpResponse("<h1>Hello World</h1>")

class PropertiesIndex(SingleTableView):
    model = Property
    table_class = PropertyTable
    template_name = "properties/properties.html"
    # paginate_by = 100

    def get_queryset(self):
        return Property.objects.all()
