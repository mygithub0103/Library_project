from django.shortcuts import render, redirect
from .models import Research

def research_list(request):
    research_list = Research.objects.all()
    return render(request, 'research_list.html', {'research_list': research_list})

def add_research(request):
    if request.method == 'POST':
        titler = request.POST['titler']
        authorr = request.POST['authorr']
        Research.objects.create(titler=titler, authorr=authorr)
        return redirect('research_list')
    return render(request, 'add_research.html')

 

def research_list(request):
    query = request.GET.get('q')
    if query:
        research_list = Research.objects.filter(titler__icontains=query)
    else:
        research_list = Research.objects.all()
    return render(request, 'research_list.html', {'research_list': research_list})
