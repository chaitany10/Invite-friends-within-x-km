from django.shortcuts import render
from .models import Entry
from django.http import Http404
from .distance import calc_dist
def home(request):
    return render(request, 'entries/form.html')

def calculate(request):
    if request.method == 'POST':
        lat = float(request.POST.get('Latitude', None))
        lon = float(request.POST.get('Longitude', None))
        km = float(request.POST.get('km', None))
        print(lat,lon,km)
        all_entries = Entry.objects.all()
        sel_entries = []
        user = []
        for entry in all_entries:
            if(calc_dist(lat,lon,entry.latitude,entry.longitude)<=km):
                sel_entries.append([entry.user_id,entry.name])

        print(sel_entries)
        context = {'sel_entries':sel_entries,'user':user}

        return render(request, 'entries/dist.html', context)


def index(request):
    all_entries = Entry.objects.all()
    context = {'all_entries' :all_entries}
    return render(request,'entries/index.html',context)

def detail(request,userid):
    try:
        entry = Entry.objects.get(user_id=userid)
    except Entry.DoesNotExist:
        raise Http404("Entry not found")
    return render(request, 'entries/detail.html', {'entry':entry})


