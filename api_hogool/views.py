from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http.response import JsonResponse
from django.contrib import auth
from django.http import *
from rest_framework.decorators import *
from rest_framework.permissions import *
from .models import *
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.authentication import *
from django.db.models import Q
import datetime
# Create your views here.
from .serializers import *


@api_view(['POST'])
@permission_classes([AllowAny])
def create_new_user(request):
    fullName=request.data['fullName']
    email=request.data['email']
    userName=request.data['userName']
    password=request.data['password']
    accountType=request.data['accountType']

    user = authenticate(username=userName, password=password)
    if user:
        return Response("user is already exist")
    else:
        user = User.objects.create_user(username=userName, password=password, email=email)
    if user:
        user.save()
    else:
        return Response("there is problem with create user")
    user = authenticate(username=userName, password=password)
    if user:
        Token.objects.create(user=user)
    else:
        return Response("there is problem with create token")

    userInfo=UserInfo(user_id=user,full_name=fullName,account_type=accountType,account_avalability=True)
    if userInfo:
        userInfo.save()
        if accountType=="farmer":
            farmerInfo=FarmerInfo(
                farmer_id=user,
                phone="null",
                description="null",
                experince=0,
                profile_photo="null",
                location="الخرطوم",
                avalability_for_job=False
            )
            if farmerInfo:
                farmerInfo.save()
            else:
                return Response("wrong with farmer")
        else:
            investorInfo=InvestorInfo(
                investor_id=user,
            phone ="null",
            description = "null",
            profile_photo = "null",
            location = "الخرطوم"
            )
            if investorInfo:
                investorInfo.save()
            else:
                return Response("worng with investor")
        return Response("Welcome"+fullName)
    else:
        return Response("some thing is wrong")



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserType(request):
    currentUser = request.user.id
    data = UserInfo.objects.get(user_id=currentUser)
    return Response(data.account_type)

@api_view(['GET','PUT'])
@permission_classes([IsAuthenticated])
def completeProfile(request):
    currentUser = request.user.id
    accountType=get_type(currentUser)
    info =None
    if request.method=='GET':
        if accountType=="farmer":
            farmerInfo=FarmerInfo.objects.get(farmer_id=currentUser)
            ser=Farmer_infoSerializer(farmerInfo)
            return Response(ser.data)
        else:
            investor=InvestorInfo.objects.get(investor_id=currentUser)
            ser=Investor_infoSerializer(investor)
            return Response(ser.data)
    else:
        if accountType=="farmer":
            farmerInfo = FarmerInfo.objects.get(farmer_id=currentUser)
            dataFarmer ={
              "farmer_id":currentUser,
              "phone":request.data['phone'],
              "description":request.data['description'],
              "experince":request.data['experince'],
              "profile_photo":request.data['profile_photo'],
              "location":request.data['location'],
              "avalability_for_job":request.data['avalability_for_job']
            }
            ser = Farmer_infoSerializer(farmerInfo,data=dataFarmer)
            if ser.is_valid():
                ser.save()
                return Response(ser.data)
        else:
            investor = InvestorInfo.objects.get(investor_id=currentUser)
            dataInvestor={
                "investor_id": currentUser,
                "phone":request.data['phone'],
                "description": request.data['description'],
                "profile_photo": request.data['profile_photo'],
                "location": request.data['location']
            }
            ser = Investor_infoSerializer(investor,data=dataInvestor)
            if ser.is_valid():
                ser.save()
                return Response(ser.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addNew(request):
    title = request.data['title']
    pic = request.data['pic']
    contnet = request.data['contnet']
    avalability = request.data['avalability']

    new= News(
    title=request.data['title'],
    pic = request.data['pic'],
    contnet = request.data['contnet'],
    avalability = request.data['avalability']
    )
    if new:
        new.save()
    return Response("Done")

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getNews(request,id):
    if id==0:
        news = News.objects.filter(avalability=True)
        ser = News_Serializer(news, many=True)
        return Response(ser.data)
    else:
        news = News.objects.get(pk=id)
        ser = News_Serializer(news)
        return Response(ser.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createLand(request):
    currentUser = request.user
    type = get_type(currentUser)
    if type=="land owner":
        my_land = land(
            land_oner=currentUser,
            space=request.data['space'],
            duration=request.data['duration'],
            description=request.data['description'],
            price_rent=request.data['price_rent'],
            Location=request.data['Location'],
            irrigation_typemodels=request.data['irrigation_typemodels'],
            avalability=False,
        )
        if my_land:
            my_land.save()
            return Response("Done")
    else:
        return Response("you don't land owner")


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addCrop(request):
    crop=Crops(
        crop=request.data['crop']
    )
    if crop:
        crop.save()
        return Response("Done")

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def showAllCrop(request):
    allcrop=Crops.objects.all()
    ser=Crop_Serializer(allcrop,many=True)
    return Response(ser.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def showLand(request,id):
    if id==0:
        lands=land.objects.filter(avalability=True)
        ser=Land_Serializer(lands,many=True)
        return Response(ser.data)
    else:
        lands = land.objects.get(pk=id)
        ser = Land_Serializer(lands)
        return Response(ser.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def showUserLand(request):
    currentUser = request.user.id
    type=get_type(currentUser)
    if type=="land owner":
        lands = land.objects.filter(land_oner=currentUser)
        ser = Land_Serializer(lands, many=True)
        return Response(ser.data)
    else:
        return Response("you don't land owner")

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def changeNewState(request,id):
    new=News.objects.get(pk=id)
    avalability =request.data['avalability']
    data={
     "title" :new.title,
     "pic":new.pic,
     "contnet": new.contnet,
      "avalability":avalability
     }
    ser=News_Serializer(new,data=data)
    if ser.is_valid():
        ser.save()
        return Response(ser.data)

    else:
        return Response("some thing is wrong")

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def changeLandState(request,id):
    theLand = land.objects.get(pk=id)
    user = User.objects.get(id=id)
    usrInfo = UserInfo.objects.get(user_id=theLand.land_oner.pk)
    avalability = None
    if usrInfo.account_avalability:
        avalability = request.data['avalability']
    else:
        avalability=False
    data={
    "land_oner":theLand.land_oner.pk,
    "space" : theLand.space,
    "duration":theLand.duration,
    "description":theLand.description,
    "price_rent" : theLand.price_rent,
    "Location" :theLand.Location,
    "irrigation_typemodels" : theLand.irrigation_typemodels,
    "avalability" : avalability
    }
    ser = Land_Serializer(theLand, data=data)
    if ser.is_valid():
        ser.save()
        return Response(ser.data)
    else:

        return Response(ser.errors)



@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def activateUser(request,id):
    user=User.objects.get(id=id)
    usrInfo=UserInfo.objects.get(user_id=user.id)
    avalability = request.data['avalability']
    data={
    "user_id" :usrInfo.user_id.pk,
    "full_name" :usrInfo.full_name,
    "account_type" :usrInfo.account_type,
    "account_avalability" :avalability
    }
    ser =UserInfo_Serializer(usrInfo,data=data)
    if ser.is_valid():
        ser.save()
        return Response("done")
    else:
        return Response(ser.errors)





def get_type(user):
    data = UserInfo.objects.get(user_id=user)
    return data.account_type

