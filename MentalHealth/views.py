from django.shortcuts import render,redirect, get_object_or_404
from .models import CustomUser,Event,Resource,Like,Appointment
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileForm,EventForm,ResourceForm,ResourceFilterForm,AppointmentForm
from datetime import datetime

 
def index(request):
    return render(request,"index.html")
def about(request):
        return render(request,"about.html")
def service(request):
        return render(request,"service.html")

from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm, LoginForm


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration_success')
           
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration.html', {'form': form})
def registration_success(request):
    return render(request, 'registration_success.html')

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_superuser:
                    login(request, user)
                    #print(username,password)
                    return redirect('/admindashboard')  # Redirect to your desired page after login
                else:
                    login(request, user)
                    return redirect('/userdashboard') 
            else:
                error_message = "Invalid username or password"
                messages.error(request, error_message)  # Display error message
                #return render(request, 'login.html', {'form': form})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
def user_dashboard_view(request):
    # Logic for user dashboard view
    return render(request, 'user_dashboard.html')
def admin_dashboard_view(request):
    # Logic for admin dashboard view
    return render(request, 'admin_dashboard.html')

def custom_logout(request):
    logout(request)
    return redirect('/login')


@login_required
def my_account(request):
    user = request.user
    custom_user = CustomUser.objects.get(username=user.username)  # Retrieve the CustomUser object
    return render(request, 'my_account.html', {'custom_user': custom_user})


#admin profile
@login_required
def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user  # Assign the current user to the profile
            profile.save()
            return redirect('view_profile')  # Redirect to the profile view
    else:
        form = ProfileForm()
    return render(request, 'create_profile.html', {'form': form})

@login_required
def view_profile(request):
    profile = request.user.profile
    return render(request, 'profile.html', {'profile': profile})

@login_required
def edit_profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('view_profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'edit_profile.html', {'form': form})

#Events

def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.created_by = request.user.profile
            event.save()
            return redirect('event_success')  # Redirect to event detail page after creation

    else:
        form = EventForm()
    return render(request, 'create_event.html', {'form': form})
def event_success(request):
    return render(request, 'event_success.html')

def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})

def upcoming_events(request):
    current_time = datetime.now()
    upcoming_events = Event.objects.filter(date_time__gte=current_time)
    return render(request, 'upcoming_events.html', {'upcoming_events': upcoming_events})





#resourse
#@login_required
def upload_resource(request):
    if request.method == 'POST':
        form = ResourceForm(request.POST)
        if form.is_valid():
            resource = form.save(commit=False)
            resource.uploader = request.user.profile
            resource.save()
            return redirect('event_success')  # Redirect to event detail page after creation

    else:
        form = ResourceForm()
    return render(request, 'upload_resourse.html', {'form': form})
'''def resourse_success(request):
    return render(request, 'resourse_sucess.html')'''

#@login_required
def resource_list(request):
    resources = Resource.objects.all()
    return render(request, 'resourse_list.html', {'resources': resources})

#@login_required
def like_resource(request, resource_id):
    resource = Resource.objects.get(pk=resource_id)
    like, created = Like.objects.get_or_create(user=request.user, resource=resource)
    if not created:
        like.delete()
    return redirect('resource_list')

def resource_search(request):
    if request.method == 'POST':
        form = ResourceFilterForm(request.POST)
        if form.is_valid():
            category = form.cleaned_data['category']
            resources = Resource.objects.filter(category=category)
            return render(request, 'search_results.html', {'resources': resources})
    else:
        form = ResourceFilterForm()
    return render(request, 'search_form.html', {'form': form})


def resourse_detail(request):
    resourses = Resource.objects.filter(uploader=request.user.profile)
    return render(request, 'resourse_details.html', {'resourses': resourses})

def delete_resourse(request, resourse_id):
    resourse = get_object_or_404(Resource, id=resourse_id)
    if request.method == 'POST':
        resourse.delete()
        return redirect('resourse_detail')

#event delete or edit

def event_detail(request):
    events = Event.objects.filter(created_by=request.user.profile)
    return render(request, 'event_details.html', {'events': events})

def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        event.delete()
        return redirect('event_detail')


#simple quiz


QUESTIONS = [
    {
        'question': 'When dealing with change, how do you typically feel?',
        'answers': ['Positive', 'Neutral', 'Negative'],
    },
    {
        'question': 'How would you rate your mood generally?',
        'answers': ['Positive', 'Neutral', 'Negative'],
    },
    {
        'question': 'How do you typically approach new opportunities?',
        'answers': ['Positive', 'Neutral', 'Negative'],
    },
    {
        'question': 'Do you feel motivated to engage in activities you enjoy?',
        'answers': ['Positive', 'Neutral', 'Negative'],
    },
    {
        'question': 'How comfortable are you discussing your feelings with others?',
        'answers': ['Positive', 'Neutral', 'Negative'],
    },
]

RESPONSES = {
    
    'Positive': 'Your overall mental health seems to be positive. Keep up the good work! Here are some additional tips to maintain your positive mood:\n\n- Practice gratitude daily.\n- Engage in regular physical activity.\n- Spend time with loved ones and friends.\n- Try mindfulness or meditation techniques.\n- Pursue hobbies and activities you enjoy.',
    
    'Neutral': 'Your overall mental health is neutral. Consider seeking support if needed. Here are some tips to improve your mood:\n\n- Establish a consistent sleep schedule.\n- Practice deep breathing exercises to reduce stress.\n- Take breaks and engage in relaxation activities throughout the day.\n- Connect with supportive friends or family members.\n- Seek professional help if you feel overwhelmed or persistently low.',
    
    'Negative': 'Your overall mental health might need attention. It\'s important to talk to someone for support. Here are some steps to help improve your mood:\n\n- Reach out to a trusted friend, family member, or mental health professional for support.\n- Engage in regular physical activity to boost endorphins.\n- Practice relaxation techniques such as deep breathing or progressive muscle relaxation.\n- Limit exposure to negative news or social media.\n- Consider therapy or counseling to explore underlying issues and develop coping strategies.'


    
   ''' 'Positive': 'Your overall mental health seems to be positive. Keep up the good work!',
    'Neutral': 'Your overall mental health is neutral. Consider seeking support if needed.',
    'Negative': 'Your overall mental health might need attention. It\'s important to talk to someone for support.','''
}

def quiz(request):
    if request.method == 'POST':
        answers = [request.POST.get(f'question_{i}') for i in range(1, 6)]
        result = get_result(answers)
        return render(request, 'result.html', {'message': result})
    return render(request, 'quiz.html', {'questions': QUESTIONS})

def get_result(answers):
    # Calculate the overall result based on the most frequent response
    result = max(set(answers), key=answers.count)
    return RESPONSES[result]


#booking appointment

def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm()
    return render(request, 'book_appointment.html', {'form': form})

def appointment_list(request):
    appointments = Appointment.objects.filter(user=request.user)
    return render(request, 'appointment_list.html', {'appointments': appointments})




def appointment_detail(request):
    appointments =Appointment.objects.all() 
    return render(request, 'appointment_detail.html', {'appointments': appointments})

def accept_appointment(request, appointment_id):
    appointment =Appointment.objects.get(pk=appointment_id)
    appointment.status = 'Accepted'
    appointment.save()
    return redirect('appointment_detail')

def reject_appointment(request, appointment_id):
    appointment =Appointment.objects.get(pk=appointment_id)
    appointment.status = 'Rejected'
    appointment.save()
    return redirect('appointment_detail')

def cancel_booking(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    if request.method == 'POST':
        appointment.delete()
        return redirect('appointment_list')


def doc_list(request):
    profiles= Profile.objects.all()
    return render(request, 'docprofile.html', {'profiles': profiles})