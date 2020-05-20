from django.shortcuts import render,redirect
from .models import SignUp,UserFile,Solution
from . import checksum
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import random
# Create your views here.

mercent_key = "UUuC1klf9gvGqGNQ"
def index(request):
    if request.method=="POST":

        email = request.POST['email']
        password = request.POST['pass']
        user = SignUp.objects.all().filter(email=email,password=password)
        if SignUp.objects.filter(email=email,password=password):
            return render(request,"ProSol_Plus/userpage.html",{'user':user,'email':email})
        else:
            return render(request,'ProSol_Plus/index.html')
    else:
        return render(request, 'ProSol_Plus/index.html')


def register(request):

    if request.method=="POST":
        name= request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        password = request.POST['pass']


        if SignUp.objects.filter(email=email):
            return render(request,'ProSol_Plus/register.html')
        else:
            SignUp(name=name,email=email,password=password,mobile=mobile).save()

            return render(request, 'ProSol_Plus/index.html')

    return render(request,'ProSol_Plus/register.html')

def userpage(request,email,id):

    if request.method=="POST":
        user= SignUp.objects.filter(email=email)
        idkey = SignUp.objects.get(id=id)
        print(idkey)
        if user:
            UserFile.objects.filter(namefile=idkey).delete()
            savefile= UserFile(namefile=idkey,file=request.FILES.get('myfile'))
            savefile.save()
            return render(request,'ProSol_Plus/success.html',{'alert':'success','email':email,'msg':"FILE SUCCESSFULLY UPLOADED",'user':user})
        else:
            return render(request,'ProSol_Plus/success.html',{'alert':'warning','email':email,'msg':"FILE NOT UPLOADED",'user':user})
    else:
        return render(request,'ProSol_Plus/userpage.html')


def solution(request,email,id):


    idkey = UserFile.objects.get(namefile=SignUp.objects.get(id=id))
    user = Solution.objects.filter(namefile=idkey)

    return render(request,'ProSol_Plus/solution.html',{'email':email,'user':user})

def payment(request,email,id):
    idkey = UserFile.objects.get(namefile=SignUp.objects.get(id=id))
    user = Solution.objects.filter(namefile=idkey)
    amt = user.get().amount
    order = random.randint(10000000,9999999999)
    params = {
        "MID": "eaeKAe89564366759087",
        "ORDER_ID": str(order),
        "CUST_ID": str(email)+str(id),
        "TXN_AMOUNT": str(amt),
        "CHANNEL_ID": "WEB",
        "INDUSTRY_TYPE_ID": "Retail",
        "WEBSITE": "WEBSTAGING",
        "CALLBACK_URL" : "http://127.0.0.1:8000/paymenthandle/"+email+"/"+id+"/"
    }
    params['CHECKSUMHASH'] = checksum.generate_checksum(params,mercent_key)
    return render(request,'ProSol_Plus/payment.html',{"user":params})

@csrf_exempt
def paymenthandle(request,email,id):

    idkey = UserFile.objects.get(namefile=SignUp.objects.get(id=id))
    user = Solution.objects.filter(namefile=idkey)

    form = request.POST
    response_dict ={}
    for i in form.keys():
        response_dict[i]= form[i]
        if i=="CHECKSUMHASH":
            Checksum = form[i]
    verify = checksum.verify_checksum(response_dict,mercent_key,Checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            return render(request, 'ProSol_Plus/paymenthandle.html', {'email': email, 'user': user})
        else:
            return render(request, 'ProSol_Plus/paymentfail.html',{'response':response_dict,'email':email})

