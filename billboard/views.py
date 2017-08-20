from django.utils import timezone
from django.shortcuts import render
from .models import Entry
from .forms import newEntry


def index(request):
    list = Entry.objects.order_by("-published")[:2]
    form = newEntry(request.POST)
    if request.method == 'POST':
        new_form = form.save(commit=False)
        new_form.published = timezone.now()
        new_form.save()
        form = newEntry()
    return render(request, "billboard/index.html", {"all_entries": list, "new_form":form})
