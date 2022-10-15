"""Django Pages views"""
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    """Home page view"""

    template_name = "home.html"


class AboutPageView(TemplateView):
    """About page view"""

    template_name = "about.html"
