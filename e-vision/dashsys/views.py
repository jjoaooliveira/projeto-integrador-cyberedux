from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required


def painel(request):
    return render(request, 'painel.html')

