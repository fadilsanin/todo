from django.shortcuts import render
from. models import place,Team

# Create your views here.
def demo(request):
    obj=place.objects.all()
    abc = Team.objects.all()
    return render(request,"index.html",{'result':obj,'res':abc})



