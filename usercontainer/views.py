# from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
# from allauth.socialaccount.providers.oauth2.client import OAuth2Client
# from dj_rest_auth.registration.views import SocialLoginView
from bookingcontainer.models import Room
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from usercontainer.models import RoomManager, User
from usercontainer.serializers import RoomManagerSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []
    pagination_class = None

    def user_signup(request):
        if request.session.get('username', None) and request.session.get('type', None) == 'user':
            return Response({'status': 'User Already Logged In'})

        if request.sesion.get('email', None) and request.session.get('type', None) == 'roommanager':
            return Response({'status': 'Manager Already Logged In'})
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            if not username or not password or not email or not first_name or not last_name:
                return Response({'status': 'All fields are required'})

            if User.objects.filter(username=username).exists() or User.objects.filter(password=password).exists():
                warning_message = message.warning(request, 'Username already exists, please try again with a unique username')
                return Response({'status': warning_message})

            password_hash = make_password(password)

            user = User.objects.create_user(username=username, password=password_hash, email=email, first_name=first_name, last_name=last_name)
            user.save()
            return Response({'status': 'User Created Successfully'})
        else:
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            profile_pic=request.FILES.get('profile_pic',None)
            address = request.POST['address']
            phone_number = request.POST['phone_number']
            state = request.POST['state']
            pin_code = request.POST['pin_code']
            error = []

            if (len(username) < 5) or (len(username) > 20):
                error.append('Username must be between 5 and 20 characters')

            if (len(password) < 8) or (len(password) > 30):
                error.append('password must be between 8 and 30 characters')

            if (len(first_name) < 2) or (len(first_name) > 20):
                error.append('First name must be between 2 and 20 characters')

            if (len(last_name) < 2) or (len(last_name) > 20):
                error.append('Last name must be between 2 and 20 characters')

            if (len(address) < 5) or (len(address) > 50):
                error.append('Address must be between 5 and 50 characters')

            if (len(phone_number) < 10) or (len(phone_number) > 10):
                error.append('Phone number must be 10 digits')

            if (len(state) < 2) or (len(state) > 20):
                error.append('State must be between 2 and 20 characters')

            if (len(pin_code) < 6) or (len(pin_code) > 6):
                error.append('Pin code must be 6 digits')

            if error:
                return Response({'status': error})

            if len(error) == 0:
                password_hash = make_password(password)

            if not username or not email or not password or not first_name or not last_name or not address or not phone_number or not state or not pin_code:
                return Response({'status': 'All fields are required'})

            if User.objects.filter(username=username).exists():
                return Response({'status': 'Username already exists'})

            if User.objects.filter(email=email).exists():
                return Response({'status': 'Email already exists'})

            user = User.objects.create_user(username=username, email=email, password=password_hash, first_name=first_name, last_name=last_name, address=address, phone_number=phone_number, state=state, pin_code=pin_code)
            user.save()
            return Response({'status': 'User Registered Successfully'})


    def user_login(request):
        if request.session.get('username', None) and request.session.get('type', None) == 'user':
            return Response({'status': 'User Already Logged In'})

        if request.sesion.get('email', None) and request.session.get('type', None) == 'roommanager':
            return Response({'status': 'Manager Already Logged In'})
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            if not username or not password:
                return Response({'status': 'Username or Password cannot be empty'})

            if User.objects.filter(username=username).exists():
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    request.session['username'] = username
                    request.session['type'] = 'user'
                    return Response({'status': 'User Logged In Successfully'})
                else:
                    return Response({'status': 'Invalid Password'})

        return Response({'status': 'User container page'})


    def logout(request):
        if request.session.get('username', None) and request.session.get('type', None) == 'user':
            del request.session['username']
            del request.session['type']
            return Response({'status': 'User Logged Out Successfully'})

        else:
            return Response({'status': 'User Not Logged In'})


class RoomManagerViewSet(viewsets.ModelViewSet):
    queryset = RoomManager.objects.all()
    serializer_class = RoomManagerSerializer
    permission_classes = []
    pagination_class = None

    def manager_signup(request):
        if request.session.get('user', None) and request.session.get('type', None) == 'user':
            return Response({'status': 'User Already Logged In'})

        if request.sesion.get('email', None) and request.session.get('type', None) == 'roommanager':
            return Response({'status': 'Manager Already Logged In'})
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']

            if not email or not password or not first_name or not last_name:
                return Response({'status': 'All fields are required'})

            if RoomManager.objects.filter(email=email).exists() or User.objects.filter(password=password).exists():
                warning_message = message.warning(request, 'email already exists, please try again with a unique username')
                return Response({'status': warning_message})

            password_hash = make_password(password)

            roommanager = RoomManager(email=email, password=password_hash, first_name=first_name, last_name=last_name)
            roommanager.save()
            return Response({'status': 'User Created Successfully'})
        else:
            email = request.POST['email']
            password = request.POST['password']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            address = request.POST['address']
            phone_number = request.POST['phone_number']
            state = request.POST['state']
            gender = request.POST['gender']

            error = []

            if (len(password) < 8) or (len(password) > 30):
                error.append('password must be between 8 and 30 characters')

            if (len(first_name) < 2) or (len(first_name) > 20):
                error.append('First name must be between 2 and 20 characters')

            if (len(last_name) < 2) or (len(last_name) > 20):
                error.append('Last name must be between 2 and 20 characters')

            if (len(address) < 5) or (len(address) > 50):
                error.append('Address must be between 5 and 50 characters')

            if (len(phone_number) < 10) or (len(phone_number) > 10):
                error.append('Phone number must be 10 digits')

            if (len(state) < 2) or (len(state) > 20):
                error.append('State must be between 2 and 20 characters')


            if error:
                return Response({'status': error})

            if len(error) == 0:
                password_hash = make_password(password)

            if not email or not password or not first_name or not last_name or not address or not phone_number or not state:
                return Response({'status': 'All fields are required'})

            if RoomManager.objects.filter(email=email).exists():
                return Response({'status': 'Email already exists'})

            password_hash = make_password(password)

            roommanager = RoomManager(email=email, password=password_hash, first_name=first_name, last_name=last_name, address=address, phone_number=phone_number, state=state)

            roommanager.save()
            return Response({'status': 'Manager Registered Successfully'})

    def manager_login(request):
        if request.session.get('user', None) and request.session.get('type', None) == 'user':
            return Response({'status': 'User Already Logged In'})

        if request.sesion.get('email', None) and request.session.get('type', None) == 'roommanager':
            return Response({'status': 'Manager Already Logged In'})
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']

            if not email or not password:
                return Response({'status': 'Email or Password cannot be empty'})

            if RoomManager.objects.filter(email=email).exists():
                roommanager = authenticate(email=email, password=password)
                if roommanager is not None:
                    login(request, roommanager)
                    request.session['email'] = email
                    request.session['type'] = 'roommanager'
                    return Response({'status': 'Manager Logged In Successfully'})
                else:
                    return Response({'status': 'Invalid Password'})

        return Response({'status': 'Manager container page'})


    def logout(request):
        if request.session.get('email', None) and request.session.get('type', None) == 'roommanager':
            del request.session['email']
            del request.session['type']
            return Response({'status': 'Manager Logged Out Successfully'})

        else:
            return Response({'status': 'Manager Not Logged In'})


    @action(detail=False, methods=['POST'],  permission_classes=[IsAdminUser])
    def add_room(self, request, pk=None):
        if request.session.get('email', None) and request.session.get('type', None) == 'roommanager':
            manager = RoomManager.objects.get(email=request.session['email'])
            room = Room.objects.create(
                name=request.data['name'],
                description=request.data['description'],
                price=request.data['price'],
                room_manager=manager
            )
            return Response({'status': 'Room Added Successfully'})
        else:
            return Response({'status': 'Manager Not Logged In'})
#  Can still update the manager autorization
