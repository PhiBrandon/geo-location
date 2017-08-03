from django.shortcuts import render
from django.views.generic import View
from .utils import yelp_search

# Create your views here.
class SearchView(View):
	def get(self, request, *args, **kwargs):
		items = []
		q = request.GET.get('q')
		loc = request.GET.get('loc')
		if not loc:
			location = request.session.get('CITY', 'Newport Beach')
		else:
			location = loc
		if q:
			items = yelp_search(keyword=q, location=location, request=request)
			businesses = items['businesses']
			print(businesses[0])
		return render(request, 'search/home.html', {'results': items['businesses']})