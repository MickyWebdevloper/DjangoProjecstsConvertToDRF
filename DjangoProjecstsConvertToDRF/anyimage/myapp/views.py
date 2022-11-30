from django.shortcuts import render, HttpResponseRedirect
# Create your views here.
from . forms import ResumeForm
from . models import Resume
from django.views import View


class IndexView(View):
    def get(self, request):
        fm = ResumeForm()
        candidates = Resume.objects.all()
        context = {
            'form': fm,
            'candidates': candidates
        }
        return render(request, 'myapp/home.html', context)

    def post(self, request):
        fm = ResumeForm(request.POST, request.FILES)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/')


class CandidateView(View):
    def get(self, request, pk):
        candidate = Resume.objects.get(pk=pk)
        context = {
            'candidate': candidate
        }
        return render(request, 'myapp/candidate.html', context)
