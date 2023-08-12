from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View,TemplateView,FormView
from app.forms import *
# Create your views here.
#fbv string
def fbv_string(request):
    return HttpResponse('this is function based views string')

#cbv string
class cbv_string(View):
    def get(self,request):
        return HttpResponse('<h1>this CLASS BASED VIEWS string <h1>')

#fbv template
def fvb_temp(request):
    return render(request,'fvb_temp.html')

#cbv template rendering
class cbv_temp(View):
    def get(self,request):
        return render(request,'cbv_temp.html')

#cbv rendering
class Cbv_render(View):
    def get(self,request):
        d={'name':'BASHEER ANSARI','age':24}
        return render(request,'data_render.html',d)

#insert fbv
def insert_fbv(request):
    SFO=StudentForm()
    d={'SFO':SFO}
    if request.method=='POST':
        SFD=StudentForm(request.POST)
        if SFD.is_valid():
            SFD.save()
            return HttpResponse('data is inserted successfully.')
    return render(request,'insert_fbv.html',d)

#insert cbv
class Cbv_insert(View):
    def get(self,request):
        SFO=StudentForm()
        d={'SFO':SFO}
        return render(request,'cbv_insert.html',d)
    def post(self,request):
        SFD=StudentForm(request.POST)
        if SFD.is_valid():
            SFD.save()
            return HttpResponse('data is inserted using CBV')

#cbv template rendering with context
class TempDataRender(TemplateView):
    template_name='tempDataRender.html'

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['name']='BASHEER ANSARI'
        context['age']=24
        return context

#cbv template rendering with form object as context 
class TVStudentForm(TemplateView):
    template_name='TVStudentForm.html'

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        SFO=StudentForm()
        context['SFO']=SFO
        return context

    def post(self,request):
        SFD=StudentForm(request.POST)
        if SFD.is_valid():
            SFD.save()
            return HttpResponse('data is inserted into DB.')
        
#cbv using FormView 
class FVform(FormView):
    template_name='FVform.html'
    form_class=StudentForm
    def form_valid(self,form):
        form.save()
        return HttpResponse('data is inserted using FormView')