from django.shortcuts import render, redirect
from .forms import ProfileForm,ProjectForm, WorkExperienceForm, EducationForm, CertificationForm
from .models import Profile,Project, WorkExperience, Education, Certification
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
@login_required
def view_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    return render(request, 'view_profile.html', {'profile': profile})

@login_required
def edit_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('view_profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'edit_profile.html', {'form': form})

def customize_portfolio(request):
    if request.method == 'POST':
        project_form = ProjectForm(request.POST, request.FILES)
        work_form = WorkExperienceForm(request.POST)
        education_form = EducationForm(request.POST)
        certification_form = CertificationForm(request.POST)

        if project_form.is_valid():
            project = project_form.save(commit=False)
            project.user = request.user
            project.save()

        if work_form.is_valid():
            work = work_form.save(commit=False)
            work.user = request.user
            work.save()

        if education_form.is_valid():
            education = education_form.save(commit=False)
            education.user = request.user
            education.save()

        if certification_form.is_valid():
            certification = certification_form.save(commit=False)
            certification.user = request.user
            certification.save()

        # Check if all forms are valid
        if not project_form.is_valid():
            print(project_form.errors)
        if not work_form.is_valid():
            print(work_form.errors)
        if not education_form.is_valid():
            print(education_form.errors)
        if not certification_form.is_valid():
            print(certification_form.errors)

        # Redirect after processing the forms
        return redirect('view_profile')

    else:
        project_form = ProjectForm()
        work_form = WorkExperienceForm()
        education_form = EducationForm()
        certification_form = CertificationForm()

    return render(request, 'customize_portfolio.html', {
        'project_form': project_form,
        'work_form': work_form,
        'education_form': education_form,
        'certification_form': certification_form,
    })

def project_showcase(request):
    projects = Project.objects.filter(user=request.user)
    paginator = Paginator(projects, 6)  # Show 6 projects per page

    page_number = request.GET.get('page')
    projects = paginator.get_page(page_number)

    return render(request, 'project_showcase.html', {'projects': projects})

def show_index(request):
    return render(request,"index.html")

def work_experience_view(request):
    work_experiences = WorkExperience.objects.filter(user=request.user)  # Get only user's work experiences
    return render(request, 'work_experience_details.html', {'work_experiences': work_experiences})

# View to display education details
def education_view(request):
    education_details = Education.objects.filter(user=request.user)  # Get only user's education details
    return render(request, 'education_details.html', {'education_details': education_details})

# View to display certification details
def certification_view(request):
    certifications = Certification.objects.filter(user=request.user)  # Get only user's certifications
    return render(request, 'certification_details.html', {'certifications': certifications})