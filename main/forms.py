import os

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


ACCEPTED_FILE_EXTENSIONS = ['.pdf', '.doc', '.docx']


def validate_file_type(value):
    name, ext = os.path.splitext(value.name)
    if ext not in ACCEPTED_FILE_EXTENSIONS:
        raise ValidationError(
            _('%(value)s is not %(extensions)s file type!'),
            params={
                'value': value.name,
                'extensions': '/'.join(ACCEPTED_FILE_EXTENSIONS)
            },
        )


class CVUploadForm(forms.Form):
    cv_file = forms.FileField(
        label='Your CV file',
        required=True,
        validators=[validate_file_type],
        widget=forms.FileInput(attrs={'class': 'form-control-file'}),
        help_text=f'Only {"/".join(ACCEPTED_FILE_EXTENSIONS)} could be accepted'
    )
