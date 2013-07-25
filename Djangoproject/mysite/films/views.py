# Create your views here.
from django.http import HttpResponse
from films.models import Films
from django.template import Context, loader


def index(request):
	film_list = Films.objects.all()
	t = loader.get_template('films/index.html')
	c = Context({'film_list': film_list})
	return HttpResponse(t.render(c))
