from django.shortcuts import render,redirect
from django.contrib.auth import (REDIRECT_FIELD_NAME, get_user_model, login as auth_login,logout as auth_logout, update_session_auth_hash)
from .forms import ProfileUpdateForm,ProjectForm
from django.contrib.sites.shortcuts import get_current_site
from .models import Projects


def index(request):
    projects=Projects.objects.all()
    return render(request,'main/index.html',{"projects":projects})

def registration(request):
    if request.method == 'POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data('username')
            password=form.cleaned_data('password1')
            user=authenticate(username=username,password=password)
            login(request, user)
            return redirect('index')
    else:
        form=SignupForm()
    return render(request,'django_registration/registration.html',{'form':form})

def logout(request, next_page=None,
           template_name='registration/logged_out.html',
           redirect_field_name=REDIRECT_FIELD_NAME,
           current_app=None, extra_context=None):
    """
    Logs out the user and displays 'You are logged out' message.
    """
    auth_logout(request)

    if next_page is not None:
        next_page = resolve_url(next_page)

    if (redirect_field_name in request.POST or
            redirect_field_name in request.GET):
        next_page = request.POST.get(redirect_field_name,
                                     request.GET.get(redirect_field_name))
        # Security check -- don't allow redirection to a different host.
        if not is_safe_url(url=next_page, host=request.get_host()):
            next_page = request.path

    if next_page:
        # Redirect to this page until the session has been cleared.
        return HttpResponseRedirect(next_page)

    current_site = get_current_site(request)
    context = {
        'site': current_site,
        'site_name': current_site.name,
        'title':('Logged out')
    }
    if extra_context is not None:
        context.update(extra_context)

    if current_app is not None:
        request.current_app = current_app

    return render(request, 'registration/login.html', context)

def profile(request):
    current_user = request.user
    if request.method =='POST':
        profile=ProfileUpdateForm(request.POST,request.FILES,instance=current_user.profile)
        if profile.is_valid():
            message.success(request,'Your profile has been updated!')
            return redirect('profile')
    else:
        profile=ProfileUpdateForm(instance=request.user)
    context={"profile":profile,"current_user": current_user}
    return render(request, 'main/profile.html',context)

def newProject(request):
    user=request.user
    form=ProjectForm()
    if request.method=="POST":
        form=ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            project=form.save(commit=False)
            project.save()
        return redirect('index')
    else:
        form=ProjectForm()
        context={"form":form}
    return render(request,'main/project.html',context)
