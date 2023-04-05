from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

from assessment.forms import StompForm, NeurologicScreeningEvaluationForm, PrePostForm, \
    PsychoemotionalScreeningEvaluationForm


# Create your views here.
@login_required(login_url='/accounts/login/')
def stomp(request):
    form = StompForm()
    # rendered_form = form.render("form_snippet.html")
    description = """
        Please indicate your basic preference for each of the following genres using the scale provided.
1-----------------2-----------------3-----------------4-----------------5-----------------6-----------------7
Dislike Dislike Dislike a Neither like Like a Like Like
    """
    context = {
        'form': form,
        'header': 'STOMP-Revised',
        'description': description,
        'therapist': request.user.username}
    return render(request, 'assessment/stomp.html', context)


@login_required(login_url='/accounts/login/')
def neurologic_screening_evaluation(request):
    form = NeurologicScreeningEvaluationForm()
    # rendered_form = form.render("form_snippet.html")
    description = """
Description for the form
        """
    context = {
        'form': form,
        'header': 'Neurologic Screening/Evaluation',
        'description': description,
        'therapist': request.user.username
    }
    return render(request, 'assessment/neurologic_screening_evaluation.html', context)


@login_required(login_url='/accounts/login/')
def pre_post_form(request):
    form = PrePostForm()
    # rendered_form = form.render("form_snippet.html")
    description = """
Description for the form
        """
    context = {'form': form, 'header': 'Pre/Post Tests', 'description': description}
    return render(request, 'assessment/pre_post_form.html', context)


# Stomp Form related views
class StompView(LoginRequiredMixin, FormView):
    template_name = 'assessment/pre_post_form.html'
    form_class = StompForm
    success_url = reverse_lazy('assessment:success')

    def form_valid(self, form):
        # Calls the custom send method
        form.send()
        return super().form_valid(form)


class StompSuccessView(LoginRequiredMixin, TemplateView):
    template_name = 'email/success.html'


# Pre Post Form related view
class PrePostView(LoginRequiredMixin, FormView):
    template_name = 'assessment/pre_post_form.html'
    form_class = PrePostForm
    success_url = reverse_lazy('assessment:success')

    def form_valid(self, form):
        # Calls the custom send method
        form.send()
        return super().form_valid(form)


class PrePostSuccessView(LoginRequiredMixin, TemplateView):
    template_name = 'email/success.html'


class PsychoemotionalScreeningEvaluationView(LoginRequiredMixin, FormView):
    template_name = 'assessment/Psychoemotional_Screening_Evaluation.html'
    form_class = PsychoemotionalScreeningEvaluationForm
    success_url = reverse_lazy('assessment:success')

    def form_valid(self, form):
        # Calls the custom send method
        form.send()
        return super().form_valid(form)
