from django.shortcuts import render, HttpResponse, redirect
from .models import User

# Create your views here.
def index(request):
	return render(request, 'users/index.html', {"users": User.objects.all()})

def new(request):
	return render(request, 'users/new.html')

def create(request):
	first_name = request.POST['first_name']
	last_name = request.POST['last_name']
	email = request.POST['email']


	User.objects.create(first_name=first_name, last_name=last_name, email=email)

	return redirect('/users')

def show(request, id):
	return render(request, 'users/show.html', {'user': User.objects.get(id=id)})

def destroy(request, id):
	u = User.objects.get(id=id)
	u.delete()

	return redirect('/users')

def edit(request, id):
	return render(request, 'users/edit.html', {'user': User.objects.get(id=id)})

def update(request):
	u = User.objects.get(id=request.POST['id'])
	u.first_name = request.POST['first_name']
	u.last_name = request.POST['last_name']
	u.email = request.POST['email']
	u.save()

	return redirect("/users/{}".format(u.id))



