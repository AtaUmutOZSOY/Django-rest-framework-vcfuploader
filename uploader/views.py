from django.shortcuts import redirect, render
from uploader.forms import VcfDocumentForm
# Create your views here.
def model_form_upload(request):
    if request.method == 'POST':
        form = VcfDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = VcfDocumentForm()
    return render(request, 'core/model_form_upload.html', {
        'form': form
    })