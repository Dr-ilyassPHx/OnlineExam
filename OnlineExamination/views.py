from django.shortcuts import render, redirect, get_object_or_404
from .forms import LoginForm, RegisterForm, RegisterFormMentor,RegisterFormStaff
from django.http import HttpResponse
from .forms import EditProfileForm
from .models import Student, Question, Exams, StudyMentor, Staff
from django.contrib import messages
from django.db.models import F
from django.template import RequestContext




def base(request):
    # user1 = request.session['z']
    return render(request, 'base.html', {'user1': 'user1'})


def categories_processor(request):
    user1 = request.session['z']
    return {'user1': user1}


def profile(request):
    if request.session.has_key('z'):
        us = request.session['z']
        name = request.session['name']
        user = Student.objects.filter(user=us)
        instance = get_object_or_404(Student, user=us)
        context = {
            'user': user,
            'ur': us,
            'instance': instance,
            'exam_name': name,
        }
        return render(request, 'profile.html', context)


def profile_form(request):
    form = EditProfileForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    context = {"form": form}
    return render(request, 'profile_edit.html', context)


def profile_details(request, user=None):
    instance = get_object_or_404(Student, user=user)
    context = {
        'user': instance.user,
        'instance': instance,
    }
    return render(request, 'profile_details.html', context)


def profile_update(request, user=None):
    if request.session.has_key('z'):
        instance = get_object_or_404(Student, user=user)
        form = EditProfileForm(request.POST or None, request.FILES or None, instance=instance)
        exam_name = request.session['name']
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, "Successfully Saved")
            return redirect("profile")
        context = {
            "ur": instance.user,
            "instance": instance,
            "form": form,
            'exam_name':exam_name,
        }
        return render(request, 'profile_edit.html', context)


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, "Successfully saved")
            return  redirect('/login')
    else:
        form = RegisterForm()

    return render(request, 'reg_form.html', {'form': form})



def registerMentor(request):
    if request.method == 'POST':
        form = RegisterFormMentor(request.POST, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, "Successfully saved Mentor")
            return  redirect('/loginm')
    else:
        form = RegisterFormMentor()

    return render(request, 'regM_form.html', {'form': form})

def registerStaff(request):
    if request.method == 'POST':
        form = RegisterFormStaff(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, "Successfully saved Staff")
            return  redirect('/logins')
    else:
        form = RegisterFormStaff()

    return render(request, 'regS_form.html', {'form': form})


def treat_app(request, user=None):

    #mentor.update(Approved= True)
    ur = request.GET['parameter']
    instance = get_object_or_404(StudyMentor, user=user)
    mentor = StudyMentor.objects.get(user=user)
    # staff = Staff.objects.get(user=ur)

    contex = {
        'mentor'   :mentor,
        'user': instance.user,
        'firstname':mentor.FirstName,
        'lastname' : mentor.LastName,
        'phone'    : mentor.phone,
        'email'    : mentor.email,
        'n_id'     : mentor.national_ID,
        'subject'  : mentor.subject,
        'n_id_img' : mentor.get_photo_url,
        'address'  : mentor.address,
        'instance' : instance,
        'ur'       : ur,
    }
    return render(request, 'approve.html' ,contex)

def AccRej_app(request, user=None):
    # instance = get_object_or_404(StudyMentor, user=user)
    # mentor = StudyMentor.objects.all().filter(user=user)
    # mentor.update(Approved= True)
    messages.success(request, "Successfully Saved")

    # staff = Staff.objects.all()

    student = Student.objects.all()
    mentor = StudyMentor.objects.all()
    exam = Exams.objects.all()
    ur = request.POST.get('staffid')
    staff = Staff.objects.filter(user=ur)

    context = {
            'staff' : staff,
            'student' : student,
            'mentor' : mentor,
            'exam' : exam,
            'ur' : ur,
            }

    response = dashboard(request, context)
    return  response  #render(request, 'dashboard.html')


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            exam = Exams.objects.all()
            ur = form.cleaned_data['username']
            pd = form.cleaned_data['password']
            dbuser = Student.objects.filter(user=ur, password=pd)
            if not dbuser:
                return HttpResponse('Login failed')
            else:
                request.session['z'] = ur
                request.session.get_expiry_age()
                instance = get_object_or_404(Student, user=ur)
                return render(request, 'examopt.html', {'exam': exam, 'ur': ur, 'instance': instance})
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})


def logins(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))

            staff = Staff.objects.all()
            student = Student.objects.all()
            mentor = StudyMentor.objects.all()
            exam = Exams.objects.all()
            ur = form.cleaned_data['username']
            pd = form.cleaned_data['password']
            dbuser = Staff.objects.filter(user=ur, password=pd)

            context = {
            'staff' : staff,
            'student' : student,
            'mentor' : mentor,
            'exam' : exam,
            'ur' : ur,
            'pd' : pd,
            'dbuser' : dbuser,
            }

            if not dbuser:
                return HttpResponse('Login failed')
            else:
                request.session['z'] = ur
                request.session.get_expiry_age()
                instance = get_object_or_404(Staff, user=ur)
                response = dashboard(request, context)
                # return render(request, 'dashboard.html', context)
                return response
    else:
        form = LoginForm()
        return render(request, 'logins.html', {'form': form})


def dashboard(request, newContext={}):
    context = {}
    context.update(newContext)
    return render(request, "dashboard.html", context=context)



def exams(request):
    if request.session.has_key('z'):
        name = request.GET.get('name')
        request.session['name'] = name
        a = request.session['z']
        exam = Exams.objects.filter(exam_name=name)
        instance = get_object_or_404(Student, user=a)
        context = {
            'exam': exam,
            'ur': a,
            'instance': instance,
            'exam_name': name,
        }
        return render(request, 'exams1.html', context)


def home(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def start_exam(request):
    if request.session.has_key('z'):
        name = request.session['name']
        exam = Exams.objects.filter(exam_name=name)
        ques = Question.objects.all().filter(exam_name__in=exam)
        exam.update(attempts= F('attempts')+1)

        return render(request, '1.html', {'ques': ques})


def report(request):
    ur = request.session['z']
    exam_name = request.session['name']
    instance = get_object_or_404(Student, user=ur)
    context = {
        'ur': ur,
        'instance': instance,
        'exam_name': exam_name,
    }
    return render(request, 'REPORT.html', context)


def analysis(request):
    if request.session.has_key('z'):
        us = request.session['z']
        exam_name = request.session['name']
        instance = get_object_or_404(Student, user=us)
        context = {
            'ur': us,
            'instance': instance,
            'exam_name': exam_name,
        }
        return render(request, 'result_analysis.html', context)


def add_variable_to_context(request):
    user1 = request.session['z']
    return {
        'user1': user1,

    }


def logout(request):
    if request.session.has_key('z'):
        request.session.flush()
    return redirect('/home')



def mentor(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            student = Student.objects.all()
            ur = form.cleaned_data['username']
            pd = form.cleaned_data['password']
            dbuser = StudyMentor.objects.filter(user=ur, password=pd)
            if not dbuser:
                return HttpResponse('Incorrect user or password')
            else:
                request.session['z'] = ur
                request.session.get_expiry_age()
                instance = get_object_or_404(StudyMentor, user=ur)
                return render(request, 'mentor.html', {'student': student, 'ur': ur, 'instance': instance})
    else:
        form = LoginForm()
        return render(request, 'loginm.html', {'form': form})

