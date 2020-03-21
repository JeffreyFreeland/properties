import django_tables2 as tables

from .models import Property


class PropertyTable(tables.Table):
    class Meta:
        model = Property
        template_name = "django_tables2/bootstrap.html"
        fields = ("address", "city", "state", "zip", )
