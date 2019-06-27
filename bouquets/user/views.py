from django.shortcuts import render
from .forms import UserRegisterForm, ProfileForm, FeedbackForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.views.generic import CreateView, ListView
from .models import Feedbacks
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
# Create your views here.

class FeedbackListView(ListView):
    model = Feedbacks
    template_name = 'user/feedback_view.html'  # <app>/<model>_<viewtype>.html
    queryset = Feedbacks.objects.all()
    context_object_name = 'feedback_list'

    def get_queryset(self):
        return Feedbacks.objects.all()


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserRegisterForm(data=request.POST)
        profile_form = ProfileForm(data=request.POST)
        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            #user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user                
            profile.save()
            # Update our variable to tell the template registration was successful.
            registered = True
            messages.success(request, f'Your Account has been created! You are now able to Log In !')
            return HttpResponseRedirect('login')
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserRegisterForm()
        profile_form = ProfileForm()
    # Render the template depending on the context.
    return render(request,'user/register.html',{'user_form': user_form, 'profile_form': profile_form, 'registered': registered},)
    
class FeedbackCreateView(CreateView):
        model = Feedbacks              
        template_name = 'user/feedback.html'
        form_class = FeedbackForm #it is a variable so don't use quotes.
        # success_url = '../'
        success_url = reverse_lazy('home:index')

        def form_valid(self, form):
            form.instance.user = self.request.user
            return super(FeedbackCreateView, self).form_valid(form)

