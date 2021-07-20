from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import (REDIRECT_FIELD_NAME, get_user_model, login as auth_login,logout as auth_logout, update_session_auth_hash)
from .forms import ProfileUpdateForm,ProjectForm,ReviewForm,ProfileForm
from django.contrib.sites.shortcuts import get_current_site
from .models import Projects,Profile,Review
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProjectSerializer
from django.contrib.auth.decorators import login_required
from rest_framework import status
from .permissions import IsAdminOrReadOnly
from django.http import HttpResponseRedirect


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

@login_required(login_url='/accounts/login/')
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
        'p':('Logged out')
    }
    if extra_context is not None:
        context.update(extra_context)

    if current_app is not None:
        request.current_app = current_app

    return render(request, 'main/logout.html', context)


@login_required(login_url='/accounts/login/')
def profile(request,id):
    profile_data = Profile.objects.get(id=id)
    current_user = request.user
    if request.method =='POST':
        profile=ProfileUpdateForm(request.POST,request.FILES,instance=current_user.profile)
        if profile.is_valid():
            message.success(request,'Your profile has been updated!')
            return redirect('profile')
    else:
        profile=ProfileUpdateForm(instance=request.user)
    context={"profile":profile,"current_user": current_user,"profile_data":profile_data}
    return render(request, 'main/profile.html',context)

@login_required(login_url='/accounts/login/')
def newProject(request):
    current_user=request.user
    user_profile=Profile.objects.filter(user=current_user)
    
    if request.method=="POST":
        form=ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            new_post=form.save(commit=False)
            new_post.user=request.user
            new_post.save()
        
            return redirect('index')
    else:
        form=ProjectForm()
    return render(request,'main/project.html', {'form':form})

@login_required(login_url='/accounts/login/')
def search_results(request):
    if 'Project' in request.GET and request.GET["Project"]:
        search_term=request.GET.get('Project')
        searched_results=Projects.search(search_term)
        message=f"{search_term}"
        
        return render(request,"main/search.html",{"message":message,"results": searched_results})
    else:
        message="You haven't searched for any term"
        return render(request,"main/search.html",{"message":message})
    
@login_required(login_url='/accounts/login/')
def reviews(request,id):
    project=Projects.objects.get(id=id)
    reviews=Review.objects.filter(project_id=id)
    user = request.user
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.project_id = project
            review.user=user
            review.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = ReviewForm()
    print(reviews)
    return render(request,"main/reviews.html",{"form":form,"reviews":reviews,"project":project}) 

@login_required(login_url='/accounts/login/')
def updateprofile(request):
    current_user = request.user
    profile=Profile.objects.all()
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile) 

        if form.is_valid() and profile_form.is_valid():
            user_form = form.save()
            custom_form = profile_form.save(False)
            custom_form.user = user_form
            custom_form.save()
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=request.user)

    return render(request, 'main/updateprofile.html',{"form": form} )

class ProjectsList(APIView):
    def get(self, request,format=None):
        all_projects = Projects.objects.all()
        serializers=ProjectSerializer(all_projects,many=True)
        return Response(serializers.data)
    
    def post (self, request,format=None):
        serializers=ProjectSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_project(self,pk):
        try:
            return Projects.objects.get(pk=pk)
        except Projects.DoesNotExist:
            return Http404
        
    def get(self,request,pk,format=None):
        project=self.get_project(pk)
        serializers=ProjectSerializer(project)
        return Response(serializers.data)