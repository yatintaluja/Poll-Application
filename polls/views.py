from django.shortcuts import render, get_object_or_404, render_to_response

from django.http import HttpResponseRedirect

from django.core.urlresolvers import reverse

from django.views import generic

from polls.models import Choice, Poll

from django.utils import timezone

from django.contrib import auth

from django.core.context_processors import csrf

from forms import MyRegistrationForm

# Create your views here.

class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_poll_list'

	def get_queryset(self):
		return Poll.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
	model = Poll
	template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
	model = Poll
	template_name = 'polls/results.html'

def vote(request, poll_id):
	p = get_object_or_404(Poll, pk=poll_id)
	try:
		selected_choice = p.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'polls/detail.html', {
			'poll' : p,
			'error_message': "You didn't select a choice.",
			})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

def login(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('polls/login.html', c)

def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)

	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/polls/loggedin')
	else:
		return HttpResponseRedirect('/polls/invalid')

def loggedin(request):
	return render_to_response('polls/loggedin.html',
							 							{'full_name': request.user.username})


def invalid_login(request):
	return render_to_response('polls/invalid_login.html')

def logout(request):
	auth.logout(request)
	return render_to_response('polls/logout.html')


def register_user(request):
	if request.method == 'POST':
		form = MyRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/polls/register_success')

	args = {}
	args.update(csrf(request))

	args['form'] = MyRegistrationForm()
	print args
	return render_to_response('polls/register.html', args)

def register_success(request):
	return render_to_response('polls/register_success.html')