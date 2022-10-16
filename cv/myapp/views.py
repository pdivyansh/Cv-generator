from re import template
from django.shortcuts import render
from .models import Profile
import pdfkit
from django.http import HttpResponse
from django.template import loader
import io
import os
# Create your views here.
def accept(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        summary=request.POST.get('summary')
        education=request.POST.get('education')
        experience=request.POST.get('experience')
        certificate=request.POST.get('certificate')
        project=request.POST.get('project')
        career_objective=request.POST.get('career_objective')
        skill=request.POST.get('skill')
        profile=Profile(name=name,email=email,phone=phone,summary=summary,education=education
        ,experience=experience,certificate=certificate,
        project=project,career_objective=career_objective,skill=skill
        )
        profile.save()
    return render(request,'myapp/accept.html')

#def resume(request,id):
    # user_profile=Profile.objects.get(pk=id)
    # return render(request,'myapp/resume.html',{'user_profile':user_profile})

def resume(request,id):
    
    user_profile = Profile.objects.get(pk=id)
    template = loader.get_template('myapp/resume.html')
    html = template.render({'user_profile':user_profile})
    options ={
        'page-size':'Letter',
        'encoding':"UTF-8",
    }
    #SET TO UR PATH
    config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltox\bin\wkhtml.exe')
 
    #Must be 'option=options' and add 'configuration=config'
    pdf = pdfkit.from_string(html,False,options=options,configuration=config)
    response = HttpResponse(pdf,content_type='application/pdf')
 
    #filename must be included in contentdisposition
    response['Content-Disposition'] ='attachment'
    filename='resume.pdf'
 
    return response

def list(request):
    profiles=Profile.objects.all()
    return render(request,'myapp/list.html',{'profiles':profiles})