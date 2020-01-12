from django import forms


class CVUploadForm(forms.Form):
    cv_file = forms.FileField(
        label='Your CV file',
        required=True,
        validators=[],
        widget=forms.FileInput(attrs={'class': 'form-control-file'})
    )
