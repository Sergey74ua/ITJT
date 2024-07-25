from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, DeleteView
from .models import Language
from .forms import LanguageForm

def language(request):
    data = {
        'title': 'ITJT: Language',
        'langList': Language.objects.all()
    }
    return render(request, 'language.html', data)

def langCreate(request):
    error = ''
    if request.method == 'POST':
        form = LanguageForm(request.POST)
        if form.is_valid():
            form.save()
            file = request.FILES['upload']
            with open(f"/language/static/img/{file.name}", "wb+") as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            return redirect('language')
        else:
            error = 'Форма заполнена неверно'

    form = LanguageForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'language/langCreate.html', data)


class LangDetail(DetailView):
    model = Language
    template_name = 'language/langDetail.html'
    context_object_name = 'language'

class LangUpdate(UpdateView):
    model = Language
    template_name = 'language/langUpdate.html'
    form_class = LanguageForm

class LangDelete(DeleteView):
    model = Language
    success_url = '/language/'
    template_name = 'language/langDelete.html'
