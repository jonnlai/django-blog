from django.shortcuts import render
from .models import About

# Create your views here.

def about(request):
    queryset = About.objects.all().order_by('-updated_on').first()
    template_name = "about/about.html"

    return render(
        request,
        template_name,
        {"about": about}
    )

