from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'testapp/index.html')
def movieinfo(request):
    head_msg="Latest movie information.."
    msg1="Kantara is Kanada movie."
    msg2="KAntara gatting hate soon.."
    msg3="Resalnam movie are good than boollwood movie"
    my_dict={"head_msg":head_msg,"msg1":msg1,"msg2":msg2,"msg3":msg3}
    return render(request,"testapp/profile.html",context=my_dict)
def politicsinfo(request):
    head_msg = "Politics information portal..."
    msg1 = "Rahul gandhi doing india serve."
    msg2 = "Modi will be visit in UK ."
    msg3 = "Mr. Aknath Shinde is CM of MH.."
    my_dict = {"head_msg": head_msg, "msg1": msg1, "msg2": msg2, "msg3": msg3}
    return render(request, "testapp/profile.html", context=my_dict)
def sportinfo(request):
    head_msg = "Latest Sport information.."
    msg1 = "Virat will be next caption of indian team."
    msg2 = "There is no no good news from sport."
    msg3 = "Tomorrow india pakistan match."
    my_dict = {"head_msg": head_msg, "msg1": msg1, "msg2": msg2, "msg3": msg3}
    return render(request, "testapp/profile.html", context=my_dict)