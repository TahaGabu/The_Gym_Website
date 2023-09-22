from django.contrib import messages
from gymApp.models import bookSlots
from gymApp.models import gymPlans
from gymApp.models import trainer
from gymApp.serializers import gymSerializer
from rest_framework import serializers
from django.shortcuts import render
from rest_framework.views import APIView
from gymApp.models import gym
from rest_framework.response import Response
from rest_framework import status
from django.template import loader
from django.http import HttpResponse
from gymApp.models import gymAdmin



# Create your views here.
def home(request):
    return render(request,"index.html")

def services(request):
    return render(request,"services.html")


def bookingSlots(request):
    if request.method == "POST":
        date = request.POST.get("date")
        member_id = request.POST.get("member")
        member_instance = gym.objects.get(id=member_id)
        trainer_id = request.POST.get("trainer")
        trainer_instance = trainer.objects.get(id=trainer_id)
        subscription_id = request.POST.get("subscription")
        subscription_instance = gymPlans.objects.get(id=subscription_id)

        print(member_id)
        print(trainer_id)

        print(subscription_id)

        myValues = bookSlots(date=date,member = member_instance,trainer=trainer_instance,plans=subscription_instance)
        myValues.save()                              
    return render(request,"bookedSlots.html")


def listOfBookedSlots(request):
    listOfSlots= bookSlots.objects.all().values('id','date',
                                                'member__fname','member__lname',
                                                'trainer__fname','trainer__lname',
                                                'plans__name','plans__amount','plans__duration')
    data ={
        "slots":listOfSlots
    }
    return render(request,"slotList.html",data)


def deletingSlots(request):
        if request.method=="POST":
            id = int(request.POST.get('id'))
            gym_instance = bookSlots.objects.get(id=id)
            gym_instance.delete()
            return render(request,"deletedSlots.html",{"Message":"Deleted Successfully!"})
        else:
            return render(request, {"Message":"ID Not Found"})


class slotUpdation(APIView):
    def get(self, request, id):
        mySlots=bookSlots.objects.filter(id=id).first()
        member = gym.objects.all().values()
        listOfPlans = gymPlans.objects.all().values()
        trainers = trainer.objects.all().values()
        data={
            "slot":mySlots,
            "members":member,
            "plans":listOfPlans,
            "trainers":trainers
        }
        return render(request,"slotUpdation.html",data)





def updatingSlot(request):
        if request.method =="POST":

            gym_id = int(request.POST.get("id"))
            gym_instance = bookSlots.objects.get(id=gym_id)

            # Update the fields of the gym_instance with the values from the form data
            gym_instance.date = request.POST.get("date")

            member_id = request.POST.get("members")
            member_instance =gym.objects.get(id=member_id)
            gym_instance.member = member_instance

            trainer_id = request.POST.get("trainers")
            trainer_instance =trainer.objects.get(id=trainer_id)
            gym_instance.trainer = trainer_instance

            subscription_id = request.POST.get("plans")
            subscription_instance =gymPlans.objects.get(id=subscription_id)
            gym_instance.plans = subscription_instance
            gym_instance.save()
            return render(request, "slotUpdated.html",{"Message":"Updated Successfully!"})
        else:
            return render(request,"index.html",{'error': "gym object not updated"})


def registration(request):
    listOfPlans = gymPlans.objects.all().values()
    data ={
        "plans":listOfPlans
    }
    return render(request,"registration.html",data)


def bookSlotsPage(request):
    members= gym.objects.all().values()
    trainers= trainer.objects.all().values()
    listOfPlans = gymPlans.objects.all().values()
    data={
        "members":members,
        "trainers":trainers,
        "plans":listOfPlans
    }
    return render(request,"bookSlots.html",data)

def passingAdmin(request):
    return render(request,"passing.html")

def passingTrainer(request):
    return render(request,"passingTrainers.html")


def adminPage(request):
    return render(request,"login.html")


def trainerRegistration(request):
    if request.method == "POST":
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        dob = request.POST.get("dob")
        age = request.POST.get("age")
        height  = request.POST.get("height")
        weight  = request.POST.get("weight")
        address = request.POST.get("address")
        number = request.POST.get("number")

        myValues = trainer(fname=fname, lname= lname,dob=dob,age=age,height=height,weight=weight,address =address,number=number)
        myValues.save()
    return render(request,"signup.html")


def trainers(request):
    listOfTrainers = trainer.objects.all().values()
    data = {
        "trainers":listOfTrainers
    }
    return render(request,"trainers.html",data)


def addedPlans(request):
    return render (request,"plansAdded.html")


def gymAdminPlans(request):
    listOfPlans = gymPlans.objects.all().values()
    data = {
        "plans":listOfPlans
    }
    return render(request,"gymAdminPlans.html",data)






class gymMyAdmin(APIView):
    def post(self,request):
        if request.method == "POST":
            # id = int(request.POST.get("id"))
            username= request.POST.get("username")
            password = request.POST.get("password")

            # gym_admin=gymAdmin.objects.filter(username=username,password=password).exists()
            gym_admin=gymAdmin.objects.filter(username=username,password=password,active=True).exists()
            gym_trainer=gymAdmin.objects.filter(username=username,password=password,active=False).exists()
            
            if gym_admin:
                print("It's working....")
                return render(request,"passing.html")
            elif gym_trainer:
                return render(request,"passingTrainers.html")
            else:
                messages.error(request, 'Invalid username or password. Please try again.')

            error_message =messages.get_messages(request)
            data={"error_message":error_message}

            return render(request,"index.html",)
                
                
            # except gymAdmin.DoesNotExist:
                
            
            # print(id)
            # gym_instance=gymAdmin.objects.filter(id=id).exists()
            # if gym_instance is True:
            #     print(gym_instance)
            #     return render(request,"members.html")
            # else:
            #     print(gym_instance)
            #     return render(request,"index.html")


def addPlan(request):
    return render(request,"addPlan.html")

def viewPlans(request):
    listOfPlans = gymPlans.objects.all().values()
    data = {
        "plans":listOfPlans
    }
    return render(request,"viewPlans.html",data)



def updatingPlans(request):
        if request.method =="POST":
                
            gym_id = int(request.POST.get("id"))
            gym_instance = gymPlans.objects.get(id=gym_id)

            # Update the fields of the gym_instance with the values from the form data
            gym_instance.name = request.POST.get("name")
            gym_instance.amount = request.POST.get("amount")
            gym_instance.duration = request.POST.get("duration")
            gym_instance.save()
            return render(request, "plansUpdated.html",{"Message":"Updated Successfully!"})
        else:
            return render(request,"index.html",{'error': "gym object not updated"})
    


def trainerReg(request):
    return render(request,"trainerReg.html")


def contact(request):
    return render(request,"contact.html")




def blog(request):
    return render(request,"blog.html")
            
def deleted(request):
    return render(request,"deleted.html")


def updated(request):
    return render(request,"updated.html")


def signup(request):
    if request.method == "POST":
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        dob = request.POST.get("dob")
        address = request.POST.get("address")
        number = request.POST.get("number")
        subscription_id = request.POST.get("subscription")
        subscription_instance = gymPlans.objects.get(id=subscription_id)

        print(subscription_id)

        myValues = gym(fname=fname, lname= lname,dob=dob,address =address,number=number,subscription=subscription_instance)
        myValues.save()                              
    return render(request,"signup.html")

# def postingData(request):
#     return render(request,"signup.html")

#data retrieval
def retrieval(request):
    listOfMembers= gym.objects.all().values('id', 'fname', 'lname', 'dob', 'address', 'number', 'subscription__name', 'subscription__amount', 'subscription__duration')
    # for i in listOfMembers:
    #     print(i)

    data={
        "Hello":listOfMembers
    }
    return render(request,"members.html",data)


def deletingTrainer(request):
        if request.method=="POST":
            id = int(request.POST.get('id'))
            gym_instance = trainer.objects.get(id=id)
            gym_instance.delete()
            return render(request,"deletedTrainer.html",{"Message":"Deleted Successfully!"})
        else:
            return render(request, {"Message":"ID Not Found"})
        

def deletingPlans(request):
        if request.method=="POST":
            id = int(request.POST.get('id'))
            gym_instance = gymPlans.objects.get(id=id)
            gym_instance.delete()
            return render(request,"deletedPlans.html",{"Message":"Deleted Successfully!"})
        else:
            return render(request, {"Message":"ID Not Found"})



def addGymPlans(request):
    if request.method == "POST":
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        duration = request.POST.get("duration")
        myValues = gymPlans(name=name,amount=amount,duration=duration)
        myValues.save()
    return render(request,"plansAdded.html")




class updationPlans(APIView):
    def get(self, request, id):
        member = gymPlans.objects.filter(id=id).first()
        data={
            "member":member
        }
        return render(request,"plansUpdation.html",data)


def deletingEntry(request):
        if request.method=="POST":
            id = int(request.POST.get('id'))
            gym_instance = gym.objects.get(id=id)
            gym_instance.delete()
            return render(request,"deleted.html",{"Message":"Deleted Successfully!"})
        else:
            return render(request, {"Message":"ID Not Found"})



class updation(APIView):
    def get(self, request, id):
        member = gym.objects.filter(id=id).first()
        listOfPlans = gymPlans.objects.all().values()
        data={
            "member":member,
            "plans":listOfPlans
        }
        return render(request,"updation.html",data)



class updationTrainer(APIView):
    def get(self, request, id):
        member = trainer.objects.filter(id=id).first()
        data={
            "member":member
        }
        return render(request,"trainerUpdation.html",data)




def updatingEntry(request):
        if request.method =="POST":
                # gym_id = int(request.POST.get("id"))
                # gym_instance = gym.objects.filter(id=gym_id).update(fname=request.POST.get("fname"),
                #                                                     lname=request.POST.get("lname"),
                #                                                     dob=request.POST.get("dob"),
                #                                                     address=request.POST.get("address"),
                #                                                     number=request.POST.get("number")
                #                                                                            )
                # gymObject = gym(gym_instance)
                # gymObject.save()

            gym_id = int(request.POST.get("id"))
            gym_instance = gym.objects.get(id=gym_id)

            # Update the fields of the gym_instance with the values from the form data
            gym_instance.fname = request.POST.get("fname")
            gym_instance.lname = request.POST.get("lname")
            gym_instance.dob = request.POST.get("dob")
            gym_instance.address = request.POST.get("address")
            gym_instance.number = request.POST.get("number")
            subscription_id = request.POST.get("subscription")
            subscription_instance =gymPlans.objects.get(id=subscription_id)
            gym_instance.subscription = subscription_instance
            gym_instance.save()
            return render(request, "updated.html",{"Message":"Updated Successfully!"})
        else:
            return render(request,"index.html",{'error': "gym object not updated"})
    
    
def updatingTrainer(request):
        if request.method =="POST":
                
            gym_id = int(request.POST.get("id"))
            gym_instance = trainer.objects.get(id=gym_id)

            # Update the fields of the gym_instance with the values from the form data
            gym_instance.fname = request.POST.get("fname")
            gym_instance.lname = request.POST.get("lname")
            gym_instance.dob = request.POST.get("dob")
            gym_instance.age = request.POST.get("age")
            gym_instance.height = request.POST.get("height")
            gym_instance.weight = request.POST.get("weight")
            gym_instance.address = request.POST.get("address")
            gym_instance.number = request.POST.get("number")
            gym_instance.save()
            return render(request, "trainerUpdated.html",{"Message":"Updated Successfully!"})
        else:
            return render(request,"index.html",{'error': "gym object not updated"})






#APIViews 

class gymMembership(APIView):
    def get(self,request):
        member = gym.objects.all()
        serializer = gymSerializer(member, many=True)
        return Response({"Message":serializer.data},status.HTTP_400_BAD_REQUEST)

    def post(self,request):
        serializer = gymSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)


    # def delete(request,pk):
    #      gym_instance  = gym.objects.get(id=pk)
    #      gym_instance.delete()
    #      return Response(status.HTTP_200_OK)

class Delete(APIView):
    def post(self, request):
        gym_instance = gym.objects.get(id=int(request.data.get('id')))
        gym_instance.delete()
        return Response(data={'status': 1,
                              'msg': 'success'},status=status.HTTP_200_OK)

class Deleteagain(APIView):
    def post(self, request, pk):
        gym_instance = gym.objects.get(id=int(pk))
        gym_instance.delete()
        return Response(data={'status': 1,
                              'msg': 'success'},status=status.HTTP_200_OK)        

# class UpdateData(APIView):
#     def post(self, request):
#         serializer = gymSerializer(data=request.data)

#         if serializer.is_valid():
#             user = gym.objects.filter(id = int(request.data.get("id")))

class UpdateData(APIView):
    def post(self, request):
        # Check if 'id' is present in the request data
        if 'id' in request.data:
            gym_id = int(request.data.get("id"))
            
            try:
                # Retrieve the corresponding Gym instance
                gym_instance = gym.objects.get(id=gym_id)
                
                # Serialize and update the Gym instance with request data
                serializer = gymSerializer(gym_instance, data=request.data)
                
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            except gym.DoesNotExist:
                return Response({'error': 'Gym with id {} not found'.format(gym_id)}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'Missing "id" field in request data'}, status=status.HTTP_400_BAD_REQUEST)

            
        