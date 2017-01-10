from django.shortcuts import render
from django.views import generic
# from .models import Restaurant
from django.http import HttpResponseRedirect, HttpResponse

def index(request):
    return HttpResponse('You\'re looking at question')

#class IndexView(generic.ListView):
#    template_name = 'inspection/index.html'
#    context_object_name = 'recommended_restaurants'
#    
#    def get_queryset(self):        
#         # Filter for Thai food
#        recommendations = Restaurant.objects.filter(cuisine = 'Thai')
#        
#        # Filter for grade
#        recommendations = recommendations.filter(inspectionresults__grade__in = ['A', 'B'])
#
#        # Order by score        
#        recommendations = recommendations.order_by('inspectionresults__score')
#        
#        # Select first ten
#        recommendations = recommendations[: 10]
#        
#        return recommendations
#
#def detail(request, inspection_id):
#    inspection = Restaurant.objects.filter(pk = inspection_id)
#    return render(request, 'inspection/inspection.html', {'inspection': inspection})