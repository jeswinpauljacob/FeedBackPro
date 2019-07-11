from django.shortcuts import render
from firstapp.forms import newuserform

# Create your views here.
# def base(request):
#     return render(request,'firstapp/base.html')

def feedback(request):
    return render(request,'firstapp/feedback.html')

def reg(request):
    form=newuserform()
    if request.method=='POST':
        form =newuserform(request.POST)

        if form.is_valid():
            form.save(commit=True)
            print("value inserted")
            return index(request)
        else:
            print('error form invalid')

    return render(request,'firstapp/reg.html',{'form':form})
def index(request):
    return  render(request,'firstapp/home.html')