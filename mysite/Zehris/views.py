from django.http import HttpResponse, HttpResponseRedirect
from Zehris.forms import EmployeeForm
from django.template import RequestContext, loader
from django.shortcuts import render_to_response
from Zehris.models import Employee

def index(request):
    context = {}
    if request.method == "POST":
        search_query = request.POST.get('fname','')
        search_pass = request.POST.get('password','')
        emp_objs = Employee.objects.filter(fname__icontains = search_query, pwd__icontains = search_pass)
        context["emp_obj"] = emp_objs
        if(emp_objs):
            return render_to_response('Zehris/welcome.html',
                                  context,
                                  context_instance=RequestContext(request))
        else:
            return render_to_response('Zehris/index.html',
                              context,
                              context_instance=RequestContext(request))
    else:
        return render_to_response('Zehris/index.html',
                              context,
                              context_instance=RequestContext(request))

def login(request):
    if request.method == "POST":
        save_data = request.POST.get('postcode','')
        if(save_data):
            form = EmployeeForm(request.POST)
            if form.is_valid():
                form.save()
                return render_to_response('Zehris/success.html',
                              context={"saved": True},
                              context_instance=RequestContext(request))
    return render_to_response('Zehris/login.html',
                              context ={},
                              context_instance=RequestContext(request))

def applys(request):
    context = {}
    f_name = request.POST.get('fname','')
    l_name = request.POST.get('lname','')
    emp_objs = Employee.objects.filter(fname__icontains = f_name, lname__icontains=l_name)
    context["emp_obj"] = emp_objs
    return render_to_response('Zehris/applys.html',
                              context,
                              context_instance=RequestContext(request))

def welcome(request):
    context = {}
    f_name = request.POST.get('fname','')
    l_name = request.POST.get('lname','')
    Apply_button = request.POST.get('Apply','')
    if(Apply_button):
        leave_type = request.POST.get('leave_type','earn_l')
        ern_days = int(request.POST.get('ern_days',0))
        sick_days = int(request.POST.get('sick_days',0))
        days = int(request.POST.get('days',0))
        app_days=0
        if (days != 0):
            if (leave_type == "earn_l"):
                app_days = ern_days - days
                t = Employee.objects.get(fname=f_name)
                t.earn_apply_leave = t.earn_apply_leave + days
                t.earn_leave = app_days 
                t.save()
            else:
                app_days = sick_days - days
                t = Employee.objects.get(fname=f_name)
                t.sic_apply_leave = t.sic_apply_leave + days
                t.sick_leave = app_days 
                t.save()
        else:
            return applys(request)
    emp_objs = Employee.objects.filter(fname__icontains = f_name, lname__icontains=l_name)
    context["saved"] = True
    context["emp_obj"] = emp_objs
    return render_to_response('Zehris/welcome.html',
                              context,
                              context_instance=RequestContext(request))

def logout(request):
    return render_to_response('Zehris/logout.html',
                              context={},
                              context_instance=RequestContext(request))

def success(request):
    return render_to_response('Zehris/success.html',
                              context={},
                              context_instance=RequestContext(request))
