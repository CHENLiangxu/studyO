from django.shortcuts import render
# Create your views here.
def my_view(request):
    output = {}
    output['x'] = {}
    output['x']['time'] = "2014"
    output['x']['where'] = "paris"
    output['x']['name'] = "x"
    return render(request, 'index.html', {'school_list': output})
  