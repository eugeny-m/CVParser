import io

from django.views.generic import TemplateView
from main.forms import CVUploadForm


class IndexPage(TemplateView):
    """
    Main page of this application.
    Render form for CV file uploading
    """
    template_name = 'index.html'
    template_cv_responce = 'cv_response.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['form'] = CVUploadForm()
        return data

    def post(self, request):
        form = CVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # create ByteIo object for resume parser
            cv_file = request.FILES['cv_file']
            io_file = io.BytesIO(cv_file.read())
            io_file.name = cv_file.name

            return self.response_class(
                request=self.request,
                template=self.template_cv_responce,
                # context={"skills": []},
                context={"skills": ['python', 'django']},
                using=self.template_engine,
            )

        else:
            return self.response_class(
                request=self.request,
                template=self.get_template_names(),
                context={"form": form},
                using=self.template_engine,
            )
