from django.shortcuts import render
from .models import User,AdminUser,SuperAdmin
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from django.middleware import csrf
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
import psycopg2
from django.middleware.csrf import get_token
import datetime
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

        # try:
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
        # except:
        #     return JsonResponse("Invalid Credentials",safe=False)

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
        params = regd_instance.get('params')
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
                    'host':'4.188.244.11',
                    'database':'aquadb',
                    'user':'bariflolabs',
                    'password':'bariflo2024'
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
        
@api_view(['POST'])
@csrf_exempt        
def admincreate(request):
    if request.method == 'POST':
        userimg=request.data['userimg']
        print(userimg)
        firstname=request.data['firstname']
        lastname=request.data['lastname']
        email=request.data['email']
        mobno=request.data['mobno']
        password=request.data['password']
        usertype=request.data['user_cat']
        fullname=firstname+" "+lastname
        a = AdminUser.objects.filter(Mobno=mobno)
        b = User.objects.filter(Mobno=mobno)
        # try:
        if b.exists():
            return JsonResponse({"message":"Mobile no already used as General User"})
        if not a.exists():
            token = get_token(request)
            datas = AdminUser(Name=fullname,Email=email,Mobno=mobno,password=password,user_category=usertype,token=token)
            datas.save()
            # def admin_img(instance,filename):
            #     current_dt = datetime.datetime.now()
            #     date_str = current_dt.strftime("%d-%m-%Y")
            #     return '/'.join(['Admin_user_profile',str((instance.Name)+" "+date_str),filename])
            param = {
                    'host':'4.188.244.11',
                    'database':'aquadb',
                    'user':'bariflolabs',
                    'password':'bariflo2024'
                    }
            conn = psycopg2.connect(**param)
            print("connected")
            cur = conn.cursor() 
            cur.execute('INSERT INTO public.app1_adminuser("Name", "Email", "Mobno", "password", "token", "user_category", "user_img") VALUES (%s, %s, %s, %s, %s, %s, %s);', (f'{fullname}', f'{email}', f'{mobno}', f'{password}', f'{token}', f'{usertype}', f'{userimg}'))
            conn.commit()
            return JsonResponse({"message":"Admin user created"})
        else:
            return JsonResponse({"message":"Mobile no. already exists"})
            # else:
            #     return JsonResponse({"message":"Mobile no. already exists"})
        # except Exception as e:
        #     return JsonResponse({"error":str(e)})

@csrf_exempt        
def admin_delete(request):
    if request.method == 'POST':
        admininstance = JSONParser().parse(request)
        mobno=admininstance.get('mobno')
        param = {
                    'host':'4.188.244.11',
                    'database':'aquadb',
                    'user':'bariflolabs',
                    'password':'bariflo2024'
                    }
        conn = psycopg2.connect(**param)
        print("connected")
        cur = conn.cursor() 
        cur.execute(f'DELETE FROM public.app1_adminuser WHERE "Mobno"={mobno};')
        conn.commit()
        a = AdminUser.objects.get(Mobno=mobno)
        a.delete()
        return JsonResponse({"message":"Admin deleted"})
    
@csrf_exempt        
def admin_view(request):
    if request.method == 'GET':
        a = AdminUser.objects.all()
        data = [(i.Name,i.Email,i.Mobno,i.user_category,i.password) for i in a]
        return JsonResponse({"datas":data})

@csrf_exempt
def ocr(request):
    if request.method == 'GET':
        import easyocr
        reader = easyocr.Reader(['en'])
        result = reader.readtext('images/capture.png')
        y = result[0][0][0][1]
        count = 0
        for i in result:
            a = i[0][0][1]
            if a == y:
                count+=1
        lst = []
        lst1 = []
        count1 = 0
        # while True:
        import time
        for i in result:
            # print(i)
            lst1.append(i[1])
            time.sleep(1)
            # if count1==count:
            #     lst.append(lst1)
            #     count1+=1
            # else:
            #     # print("lst1")
            #     pass
        print(lst1)
                
        # return JsonResponse({"datas":lst})
                
