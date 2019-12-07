from django.shortcuts 					import render,redirect
from . models 							import *
from . serializers 						import *
from rest_framework 					import generics

from django.contrib.auth.models 		import User

from django.contrib.auth                import authenticate
from rest_framework.authtoken.models    import Token
from rest_framework.authentication      import TokenAuthentication
from rest_framework.decorators          import api_view, permission_classes
from rest_framework.permissions         import AllowAny, IsAuthenticated
from rest_framework.response            import Response
from rest_framework.status              import (HTTP_400_BAD_REQUEST,HTTP_404_NOT_FOUND,HTTP_200_OK)

#---------------User Login------------------------------------------------------
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key, "user_id":user.id},
                    status=HTTP_200_OK)

#--------------User Registration-------------------------------------------------
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def Register(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = User()
    user.username = username
    user.set_password(password)
    user.save()
    return Response({'User Created Successfully': True},
                    status=HTTP_200_OK)

# HTML Template Views ------------------------------------------------------------
def schoolCollegeView(request):
	context = {
		"schools" : Schools.objects.all(),
		"colleges" : Colleges.objects.all(),
	}
	return render(request, 'schoolCollegelist.html',context)

# School List API -----------------------------------------------------------------

class SchoolList(generics.ListCreateAPIView):
    queryset = Schools.objects.all()
    serializer_class = SchoolSerializer

class SchoolDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Schools.objects.all()
    serializer_class = SchoolSerializer

# college List API-----------------------------------------------------------------

class CollegeList(generics.ListCreateAPIView):
    queryset = Colleges.objects.all()
    serializer_class = CollegeSerializer

class CollegeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Colleges.objects.all()
    serializer_class = CollegeSerializer