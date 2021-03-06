from django.shortcuts import render,redirect
from FarMeKart.forms import UsregFo,ChpwdForm,UpdPfle,Vegfr,UpdVgtab,Userp,Usperm
from django.contrib.auth.decorators import login_required
from farmer import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User,AbstractUser
from FarMeKart.models import Vegpro,User
import sys

# Create your views here.

def home(re):
	i = Vegpro.objects.filter(a_id=re.user.id)
	s = Vegpro.objects.all()
	k = {}
	for m in s:
		g = User.objects.get(id=m.a_id)
		k[m.id] = m.item_type,m.item_name,m.quantity,m.price,m.impf,m.is_stock,m.create_date,g.username
	f = k.values()
	return render(re,'html/cart1.html',{'it':i,'d':f})
	
# def home(re):
# 	return render(re,"html/home.html")
def contact(re):
	return render(re,"html/contact.html")

def about(re):
	return render(re,"html/about.html")

def registration(request):
	if request.method=="POST":
		k = UsregFo(request.POST)
		if k.is_valid():
			e = k.save(commit=False)
			sb = "Testing Email For FarMeKart"
			mg = "Hi Welcome{}. You have successfully registered for FarMeKart portal.".format(e.username)
			sd = settings.EMAIL_HOST_USER
			snt = send_mail(sb,mg,sd,[e.email])
			if snt == 1:
				e.save()
				return redirect('/lg')
			else:
				return redirect('/')
	k=UsregFo()
	return render(request,'html/register.html',{'h':k})

@login_required
def cgf(re):
	if re.method=="POST":
		c=ChpwdForm(user=re.user,data=re.POST)
		if c.is_valid():
			c.save()
			return redirect('lg/')
	c=ChpwdForm(user=re.user)
	return render(re,'html/changepassword.html',{'t':c})

@login_required
def profile(req):
	return render(req,'html/profile.html')

@login_required
def updprofile(request):
	if request.method == "POST":
		t = UpdPfle(request.POST,instance=request.user)
		if t.is_valid():
			t.save()
			return redirect('/pro')
	t = UpdPfle(instance=request.user)
	return render(request,'html/updateprofile.html',{'z':t})


@login_required
def dashboard(re):
	return render(re,'html/dashboard.html')

@login_required
def farmerdashboard(request):
	return render(request,'html/farmerdashboard.html')


@login_required
def vegf(request):
	t = Vegpro.objects.filter(a_id=request.user.id)
	if request.method == "POST":
		s = Vegfr(request.POST,request.FILES)
		if s.is_valid():
			r = s.save(commit=False)
			r.a_id = request.user.id
			r.save()
			return redirect('/dt')
	s=Vegfr()
	return render(request,'html/data.html',{'a':s,'e':t})




@login_required
def infodelete(req,et):
	data=Vegpro.objects.get(id=et)
	print(data.id)
	if req.method == "POST":
		print(data.id)
		data.delete()
		return redirect('/dt')
	return render(req,'html/userdelete.html',{'sd':data})

def itemupdate(request,y):
	dc = Vegpro.objects.get(id=y)
	if request.method == "POST":
		m = UpdVgtab(request.POST,request.FILES,instance=dc)
		if m.is_valid():
			m.save()
			return redirect('/dt')
	m = UpdVgtab(instance=dc)
	return render(request,'html/updateuser.html',{'e':m})





@login_required
def cart(re):
	i = Vegpro.objects.filter(a_id=re.user.id)
	s = Vegpro.objects.all()
	k = {}
	for m in s:
		g = User.objects.get(id=m.a_id)
		k[m.id] = m.item_type,m.item_name,m.quantity,m.price,m.impf,m.is_stock,m.create_date,g.username
	f = k.values()
	return render(re,'html/cart.html',{'it':i,'d':f})



def usr(re):
	s=Userp()
	return render(re,'html/user.html',{'a':s})
def requestform(rq):
	e2=User.objects.get(id=rq.user.id)
	if rq.method=='POST':
		print(e2)
		e2.age=rq.POST['age']
		e2.gender=rq.POST['gender']
		e2.impf=rq.POST['fil']
		e2.address=rq.POST['ad']
		e2.mobile_number=rq.POST['pn']
		e2.save()
		return redirect('/lg')
	k2= Usperm(instance=e2)
	return render(rq,'html/requestp.html',{'y':k2})
def adminpermissions(request):
	ty=User.objects.all()
	return render(request,'html/adminpermissions.html',{'q':ty})
def updatepermissions(request,k):
	r=User.objects.get(id=k)
	if request.method == "POST":
		k=Usperm(request.POST,instance=r)
		if k.is_valid():
			k.save()
			return redirect('/gper')
	k2= Usperm(instance=r)
	return render(request,'html/updatepermissions.html',{'y':k2})
def userdelete(request,id):
	c=User.objects.get(id=id)
	c.delete()
	c.save()
	return redirect('/gper')
		
		
	




