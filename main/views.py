from django.views.generic import TemplateView


class IndexPage(TemplateView):
    """
    Main page of this application.
    Render form for CV file uploading
    """
    template_name = 'index.html'
