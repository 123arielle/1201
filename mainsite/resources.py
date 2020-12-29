from import_export import resources
from .models import HelloVisit

class HelloVisitResource(resources.ModelResource):
    class Meta:
        model = HelloVisit