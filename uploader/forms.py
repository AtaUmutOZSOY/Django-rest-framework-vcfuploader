from django import forms
from uploader.models import VcfFile

class VcfDocumentForm(forms.ModelForm):
    class Meta:
        model = VcfFile
        fields = ('description', 'document', )