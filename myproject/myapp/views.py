from django.shortcuts import render
from .models import User,AdminUser,SuperAdmin
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from django.middleware import csrf
from django.views.decorators.csrf import csrf_exempt
import psycopg2
# Create your views here.
@csrf_exempt
def user_create(request):
    if request.method == 'POST':
        jsondata = JSONParser().parse(request)
        username = jsondata.get('username')
        password = jsondata.get('password')
        category = jsondata.get('category')

        try:
            token = csrf.get_token(request)
            data = User(username=username,password=password,token = token,category=category)

            data.save()

            return JsonResponse({'message': 'Login successfully.',"token":token})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

@csrf_exempt
def login(request):
    if request.method == 'POST':
        jsondata = JSONParser().parse(request)
        phone = jsondata.get('username')
        password = jsondata.get('password')

        try:
            if type(phone)==int:
                if User.objects.filter(Mobno=phone).exists():
                    users = User.objects.get(Mobno=phone)
                    if phone == users.Mobno and str(users.user_category) == "3d" and password == users.password:
                        return JsonResponse({'message':"Login Successfull For 3D User",'username':users.Name,'mobno':users.Mobno,'token':users.token,'cat':users.user_category})
                    elif phone == users.Mobno and str(users.user_category) == "water" and password == users.password:
                        return JsonResponse({'message':"Login Successfull For waterbody User",'username':users.Name,'mobno':users.Mobno,'token':users.token,'cat':users.user_category})
                    elif phone == users.Mobno and str(users.user_category) == "aqua" and password == users.password:
                        return JsonResponse({'message':"Login Successfull For aqua User",'username':users.Name,'mobno':users.Mobno,'token':users.token,'cat':users.user_category})
                    else:  
                        return JsonResponse({'error':"Invalid credential for General user"})
                if AdminUser.objects.filter(Mobno=phone).exists():
                    admin = AdminUser.objects.get(Mobno=phone)
                    if phone == admin.Mobno and str(admin.user_category) == "3d" and password == admin.password:
                        return JsonResponse({'message':"Login Successfull For 3D Admin",'username':admin.Name,'mobno':admin.Mobno,'token':admin.token,'cat':admin.user_category})
                    elif phone == admin.Mobno and str(admin.user_category) == "water" and password == admin.password:
                        return JsonResponse({'message':"Login Successfull For waterbody Admin",'username':admin.Name,'mobno':admin.Mobno,'token':admin.token,'cat':admin.user_category})
                    elif phone == admin.Mobno and str(admin.user_category) == "aqua" and password == admin.password:
                        return JsonResponse({'message':"Login Successfull For aqua Admin",'username':admin.Name,'mobno':admin.Mobno,'token':admin.token,'cat':admin.user_category})
                    else:  
                        return JsonResponse({'error':"Invalid credential for Admin user"})
            if type(phone)==str:
                if User.objects.filter(Email=phone).exists():
                    users=User.objects.get(Email=phone)
                    print(users)
                    if phone == users.Email and str(users.user_category) == "3d" and password == users.password:
                        return JsonResponse({'message':"Login Successfull For 3D User",'username':users.Name,'mobno':users.Mobno,'token':users.token,'cat':users.user_category})
                    elif phone == users.Email and str(users.user_category) == "water" and password == users.password:
                        return JsonResponse({'message':"Login Successfull For waterbody User",'username':users.Name,'mobno':users.Mobno,'token':users.token,'cat':users.user_category})
                    elif phone == users.Email and str(users.user_category) == "aqua" and password == users.password:
                        return JsonResponse({'message':"Login Successfull For aqua User",'username':users.Name,'mobno':users.Mobno,'token':users.token,'cat':users.user_category})
                    else:  
                        return JsonResponse({'error':"Invalid credential for general user"})
                if SuperAdmin.objects.filter(Username=phone).exists():
                    admin = SuperAdmin.objects.get(Username=phone)
                    if phone == admin.Username and password == admin.Password:
                        return JsonResponse({'message':"Login Successfull For  SuperAdmin",'username':admin.Username,'password':admin.Password})
                    else:  
                        return JsonResponse({'error':"Invalid credential for SuperAdmin user"})
                if AdminUser.objects.filter(Email=phone).exists():
                    admin = AdminUser.objects.get(Email=phone)
                    if phone == admin.Email and str(admin.user_category) == "3d" and password == admin.password:
                        return JsonResponse({'message':"Login Successfull For 3D Admin",'username':admin.Name,'mobno':admin.Mobno,'token':admin.token,'cat':admin.user_category})
                    elif phone == admin.Email and str(admin.user_category) == "water" and password == admin.password:
                        return JsonResponse({'message':"Login Successfull For waterbody Admin",'username':admin.Name,'mobno':admin.Mobno,'token':admin.token,'cat':admin.user_category})
                    elif phone == admin.Email and str(admin.user_category) == "aqua" and password == admin.password:
                        return JsonResponse({'message':"Login Successfull For aqua Admin",'username':admin.Name,'mobno':admin.Mobno,'token':admin.token,'cat':admin.user_category})
                    else:  
                        return JsonResponse({'error':"Invalid credential for Admin user"})
                else:  
                    return JsonResponse({'error':"Invalid credential"})
        except:
            return JsonResponse("Invalid Credentials",safe=False)

@csrf_exempt
def token_verification(request):
    if request.method == 'POST':
        jsondata = JSONParser().parse(request)
        token = jsondata.get('token')

        try:
            data = User.objects.get(token=token)
            return JsonResponse({'message': 'Authenticated successfully.',"token":data.token,"mobile_no":data.Mobno,"username":data.password})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
        
@csrf_exempt
def registration(request):
    if request.method == 'POST':
        regd_instance=JSONParser().parse(request)
        firstname=regd_instance.get('firstname')
        lastname=regd_instance.get('lastname')
        Email=regd_instance.get('email')
        Mobno=regd_instance.get('mobno')
        Adhaar=regd_instance.get('adhaar')
        user_cat=regd_instance.get('user_cat')
        params = regd_instance.get('parameter')
        fullname=firstname+" "+lastname
        try:
            import json
            name = f'{fullname}'
            email = f'{Email}'
            mobno = f'{Mobno}'
            adhaar = f'{Adhaar}'
            user_category = f'{user_cat}'
            params = f'{json.dumps(params)}'
            if user_cat == 'aqua':
                param = {
                    'host':'20.244.48.88',
                    'database':'logindb',
                    'user':'bariflolabs',
                    'password':'bariflo123'
                    }
                conn = psycopg2.connect(**param)
                print("connected")
                cur = conn.cursor() 
                cur.execute('INSERT INTO public.app1_registration("Name", "Email", "Mobno", "Adhaar", "user_category", "params") VALUES (%s, %s, %s, %s, %s, %s);', (name, email, mobno, adhaar, user_category, params))
                conn.commit()
                return JsonResponse({'message': 'Registration successfully as Aqua-culture user'})
            
            if user_cat == 'water':
                param = {
                    'host':'20.235.250.157',
                    'database':'testdb',
                    'user':'bariflolabs',
                    'password':'tapas123',
                    }
                conn = psycopg2.connect(**param)
                print("connected")
                cur = conn.cursor() 
                cur.execute('INSERT INTO public.myapp_registration("Name", "Email", "Mobno", "Adhaar", "user_category", "params") VALUES (%s, %s, %s, %s, %s, %s);', (name, email, mobno, adhaar, user_category, params))
                conn.commit()
                return JsonResponse({'message': 'Registration successfully as Waterbody user'})
            else:
                return JsonResponse({'error': 'Error occured!'})
            # if user_cat == 'aqua':
        except Exception as e:
            return JsonResponse({'error': str(e)})
