from django.shortcuts import render
from .models import Primary
from .forms import PrimaryCreateForm

# Create your views here.


def primary_create(request):
    if request.method == 'POST':
        form=PrimaryCreateForm(request.POST)
        if form.is_valid():
            form.save()
            #cd=form.cleaned_data
            return render(request, 'created.html')
    else:
        form=PrimaryCreateForm()

    return render(request, 'basic.html')

