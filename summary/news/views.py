from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Summary
import xlrd


# Create your views here.

def home(request):
    loc = "summary.xlsx"

    wrbk = xlrd.open_workbook(loc)
    sheet = wrbk.sheet_by_index(0)
    sheet.cell_value(0, 0)

    summary = []
    for i in range(sheet.nrows):
        summary.append(sheet.cell_value(i, 1))
    return render(request, 'home.html', {'summary': summary})


def texts(request):
    text_list = Summary.objects.all()
    return render(request, 'text.html', {'text_list': text_list})
