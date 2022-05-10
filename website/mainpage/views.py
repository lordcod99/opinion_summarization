from django import http
from django.shortcuts import render
from django.http import HttpResponse
from .models import data
from .forms import inputForm
from .modelx import Summary


def home_veiw(request):
    form =  inputForm(request.POST or None)
    ctx = {}
    sg = False
    if form.is_valid():
        form.save()
        input = data.objects.last()
        # print(input.input_data)
        smry = Summary.get_summary(input.input_data)
        sg = True
        # form =  inputForm()

        ctx['smry'] =  smry
    ctx['form'] = form
    ctx['sg']=sg

    return render(request, 'home.html',ctx)




