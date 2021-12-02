from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentReg
from .models import User
# Create your views here.

#POST function and shows all item
def add_show(request):
	# stud = ''
	if request.method == 'POST':
		new = StudentReg(request.POST)
		if new.is_valid():
			fnm = new.cleaned_data['fname']
			lnm = new.cleaned_data['lname']
			stdnm = new.cleaned_data['std']
			reg = User(fname=fnm, lname=lnm, std=stdnm)
			reg.save()
			new = StudentReg() #for blank form
	else:
		new = StudentReg()
	stud = User.objects.all()
	return render(request, 'enroll/addandshow.html', {'form': new, 'stu':stud})


#Update function
def update_data(request, id):
	if request.method=='POST':
		pi = User.objects.get(pk=id)
		new = StudentReg(request.POST, instance=pi)
		if new.is_valid():
			new.save()
	else:
		pi = User.objects.get(pk=id)
		new = StudentReg(request.POST, instance=pi)
		
	return render(request, 'enroll/updatestudent.html', {'form':new})


#Delete function
def delete_data(request,id):
	if request.method == 'POST':
		pi = User.objects.get(pk = id)
		pi.delete()
		return HttpResponseRedirect('/')
