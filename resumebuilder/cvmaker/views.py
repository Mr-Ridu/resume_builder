from django.shortcuts import render,redirect
from .models import Resume,Education,experiance,certification,awards
from .forms import basicforms,educationform,experianceform,certificateform,awardsform
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def home (request):
    c_p =  get_client_ip(request)
    return render (request, 'home.html',{'c_p':c_p})

 
def basic (request,resume_id=None):
    if request.method == 'POST':
        if resume_id is None:
            form = basicforms(request.POST, request.FILES)  # Include request.FILES for file uploads
            if form.is_valid():
                new_resume = form.save()
                return redirect('education', resume_id=new_resume.id)
            else:
                print(form.errors)
        else:
            update_resume = Resume.objects.get(id=resume_id)
            if request.method == 'POST':
                form = basicforms(request.POST, request.FILES, instance=update_resume)
                if form.is_valid():
                    form.save()
                    return redirect('education', resume_id=resume_id)
            else:
                print(form.errors)
    else:
        form = basicforms()
        try:
            show = Resume.objects.get(id=resume_id)
        except ObjectDoesNotExist:
            show=None
        return render (request, 'resume_data/basic.html',{'show':show,'resume_id':resume_id})
    return render (request, 'resume_data/basic.html',{'resume_id':resume_id})


def education (request,resume_id):
    in_education = Resume.objects.get(id = resume_id)
    if request.method == 'POST':
        form = educationform(request.POST) 
        if form.is_valid():
            form.instance.resume = in_education
            form.save()
            return redirect('experiances', resume_id)
        else:
            print(form.errors)
    else:
        form = educationform()
        try:
            show = Education.objects.filter(id=resume_id)
            print(show,111)
        except ObjectDoesNotExist:
            show=None
            print(show,2222)
        return render (request, 'resume_data/education.html',{'show':show,'resume_id':resume_id})

    return render (request, 'resume_data/education.html',{'in_education':in_education,'resume_id':resume_id})


def experiances(request,resume_id):
    in_experiance = Resume.objects.get(id = resume_id )
    edu = Education.objects.filter(resume=in_experiance)
    if request.method == 'POST':
        form = experianceform(request.POST) 
        if form.is_valid():
            form.instance.resume = in_experiance
            form.save()
            return redirect('certificate', resume_id)
        else:
            print(form.errors)
    else:
        form=experianceform()
    context={
            'edu':edu,
            'in_experiance':in_experiance,
            'resume_id':resume_id
            }
    return render (request, 'resume_data/experiances.html',context)



def certificate(request,resume_id):
    in_certificate = Resume.objects.get(id =resume_id)
    edu = Education.objects.filter(resume=in_certificate)
    exp = experiance.objects.filter(resume=in_certificate)
    if request.method == 'POST':
        form = certificateform(request.POST) 
        if form.is_valid():
            form.instance.resume = in_certificate
            form.save()
            return redirect('award', resume_id)
        else:
            print(form.errors)
    else:
        form= certificateform()
    context={
        'edu':edu,
        'in_certificate':in_certificate,
        'exp':exp,
         'resume_id':resume_id
    }
    return render (request, 'resume_data/certificate.html',context)

def award(request,resume_id):
    in_award = Resume.objects.get(id =resume_id)
    edu = Education.objects.filter(resume=in_award)
    exp = experiance.objects.filter(resume=in_award)
    cer = certification.objects.filter(resume=in_award)
    if request.method == 'POST':
        form = awardsform(request.POST) 
        if form.is_valid():
            form.instance.resume = in_award
            form.save()
            return redirect('cv', resume_id)
        else:
            print(form.errors)
    else:
        form= awardsform()
    context={
        'edu':edu,
        'in_award':in_award,
        'exp':exp,
        'cer':cer,
        'resume_id':resume_id
    }
    return render (request, 'resume_data/award.html',context)



def cv (request,resume_id):
    resu = Resume.objects.get(id=resume_id)
    edu = Education.objects.filter(resume=resu)
    exp = experiance.objects.filter(resume=resu)
    cer = certification.objects.filter(resume=resu)
    awrd = awards.objects.filter(resume=resu)
    context={
        'resu':resu,
        'edu':edu,
        'exp':exp,
        'cer':cer,
        'awrd':awrd
    }
    return render (request, 'cv.html',context)