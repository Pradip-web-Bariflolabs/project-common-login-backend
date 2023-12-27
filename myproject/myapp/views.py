from django.shortcuts import render
from .models import User
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
        username = jsondata.get('username')
        password = jsondata.get('password')

        try:
            data = User.objects.get(username=username,password=password)
            return JsonResponse({'message': 'Login successfully.',"token":data.token,"cat":data.user_category})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

@csrf_exempt
def token_verification(request):
    if request.method == 'POST':
        jsondata = JSONParser().parse(request)
        token = jsondata.get('token')
        # password = jsondata.get('password')

        try:
            data = User.objects.get(token=token)
            return JsonResponse({'message': 'Authenticated successfully.',"token":data.token,"mobile_no":data.mobile_no,"username":data.username})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
        
@csrf_exempt
def registration(request):
    if request.method == 'POST':
        regd_instance=JSONParser().parse(request)
        firstname=regd_instance.get('firstname')
        lastname=regd_instance.get('lastname')
        email=regd_instance.get('email')
        mobno=regd_instance.get('mobno')
        adhaar=regd_instance.get('adhaar')
        accountname=regd_instance.get('accountname')
        devicedetails=regd_instance.get('devicedetails')
        user_cat=regd_instance.get('user_cat')
        fullname=firstname+" "+lastname
        try:
            if user_cat == 'aqua':
                params = {
                    'host':'20.244.48.88',
                    'database':'iotdb',
                    'user':'bariflolabs',
                    'password':'bariflo123'
                    }
                
                conn = psycopg2.connect(**params)
                cur = conn.cursor() 
                cur.execute(f'INSERT INTO public.app1_registration("Name", "Email", "Mobno", "Adhaar", "account_name", "device_details", "user_category") VALUES (%s,%s,%s,%s,%s,%s,%s);',(fullname,email,mobno,adhaar,accountname,f'{devicedetails}',user_cat))
                conn.commit()
                return JsonResponse({'message': 'Registration successfully as Aqua-culture user'})
        except Exception as e:
            return JsonResponse({'error': str(e)})
