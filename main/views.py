import io

from django.views.generic import TemplateView
from time import time

from main.cv_parser import CVParser
from main.forms import CVUploadForm


class IndexPage(TemplateView):
    """
    Main page of this application.
    Render form for CV file uploading
    Return extracted from CV skills
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
            start = time()
            # create ByteIo object for resume parser
            cv_file = request.FILES['cv_file']
            io_file = io.BytesIO(cv_file.read())
            io_file.name = cv_file.name

            # extract skills
            parser = CVParser(resume=io_file,)
            skills = parser.extract_skills()
            skills = ', '.join(skills)
            end = time()

            return self.response_class(
                request=self.request,
                template=self.template_cv_responce,
                context={"skills": skills, 'used_time': end - start},
                using=self.template_engine,
            )

        else:
            return self.response_class(
                request=self.request,
                template=self.get_template_names(),
                context={"form": form},
                using=self.template_engine,
            )
