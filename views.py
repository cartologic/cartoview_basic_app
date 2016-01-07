from django.http import HttpResponseRedirect
from django.shortcuts import render

from cartoview.app_manager.models import *
from forms import BasicAppForm
from .models import *

APP_NAME = 'cartoview_basic_app'
VIEW_TPL = "%s/index.html" % APP_NAME
NEW_EDIT_TPL = "%s/new.html" % APP_NAME


def view(request, resource_id):
    basic_app_obj = BasicApp.objects.get(pk=resource_id)
    context = {'basic_app': basic_app_obj}
    return render(request, VIEW_TPL, context)


def save(request, app_form):
        basic_app_obj = app_form.save(commit=False)
        # get app by name and add it to app instance.
        basic_app_obj.app = App.objects.get(name=APP_NAME)
        # get current user and add it as app instance owner.
        basic_app_obj.owner = request.user
        basic_app_obj.save()
        # redirect to app instance details after saving instance.
        return HttpResponseRedirect(reverse('appinstance_detail', kwargs={'appinstanceid': basic_app_obj.pk}))


#
def new(request):
    if request.method == 'POST':
        app_form = BasicAppForm(request.POST, prefix='app_form')
        return save(request, app_form)

    else:
        # form is invalid.
        context = {'app_form': BasicAppForm(prefix='app_form')}
        return render(request, NEW_EDIT_TPL, context)


def edit(request, resource_id):
    basic_app_obj = BasicApp.objects.get(pk=resource_id)
    if request.method == 'POST':
        app_form = BasicAppForm(request.POST, prefix='app_form', instance=basic_app_obj)
        return save(request, app_form)

    else:
        # form is invalid.
        context = {'app_form': BasicAppForm(prefix='app_form', instance=basic_app_obj)}
        return render(request, NEW_EDIT_TPL, context)
