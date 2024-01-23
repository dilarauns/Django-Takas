from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponseRedirect
from .models import Person, Product
import os
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.
        
kategori_list=["Elektronik","Okuma Kitabı","Ders Kitabı","Diğer"]
city_list=["Adana","Adıyaman","Afyonkarahisar","Ağrı","Aksaray","Amasya","Ankara","Antalya","Ardahan","Artvin","Aydın","Balıkesir","Bartın","Batman","Bayburt","Bilecik","Bingöl","Bitlis","Bolu","Burdur","Bursa","Çanakkale","Çankırı","Çorum","Denizli","Diyarbakır","Düzce","Edirne","Elazığ","Erzincan","Erzurum","Eskişehir","Gaziantep","Giresun","Gümüşhane","Hakkâri","Hatay","Iğdır","Isparta","İstanbul","İzmir","Kahramanmaraş","Karabük","Karaman","Kars","Kastamonu","Kayseri","Kilis","Kırıkkale","Kırklareli","Kırşehir","Kocaeli","Konya","Kütahya","Malatya","Manisa","Mardin","Mersin","Muğla","Muş","Nevşehir","Niğde","Ordu","Osmaniye","Rize","Sakarya","Samsun","Şanlıurfa","Siirt","Sinop","Sivas","Şırnak","Tekirdağ","Tokat","Trabzon","Tunceli","Uşak","Van","Yalova","Yozgat","Zonguldak"]
university_list = ["Bursa Teknik Üniversitesi","Bursa Uludağ Üniversitesi","Boğaziçi Üniversitesi","İstanbul Teknik Üniversitesi","İstanbul Üniversitesi","Sabancı Üniversitesi","Koç Üniversitesi","Hacettepe Üniversitesi","Ankara Üniversitesi","Gazi Üniversitesi","Orta Doğu Teknik Üniversitesi"]
def index(request):
    person = Person.objects.all()
    user_products = Product.objects.all()
    for product in user_products:
        product.gorsel = os.path.basename(str(product.gorsel))
    print(user_products)
    return render(request, "blog/index.html", {"user_products": user_products, "person_list": person})  # Uygulamamız render metodu aracılığıyla index.html'ye ulaşabilir. Başka bir uygulama altında da index.hmtl olsa blog'dan önce o çıkabilir çünkü bütün uygulamalarda arıyor. Bunun ayrımını yapmak için ilgili uygulamanın ismini ekleriz


def blogs(request):
    return render(request, "blog/blogs.html")


def login(request):  # bu bizi uye girisi sayfasina yonlendiriyor
    return render(request, "blog/login.html")

def blog_details(request): 
    person = Person.objects.all()
    user_products = Product.objects.all()
    for product in user_products:
        product.gorsel = os.path.basename(str(product.gorsel))
    print(user_products)
    return render(request, "blog/blog-details.html", {"user_products": user_products, "person_list": person})



def download(request):  
    return render(request, "blog/download.html")
def aciklama1(request):
    return render(request,"blog/aciklama1.html")

def aciklama2(request):
    return render(request,"blog/aciklama2.html")

def send_info(request):
    if request.method == "POST":
        firstname = request.POST.get("register-firstname")
        lastname = request.POST.get("register-lastname")
        email = request.POST.get("register-email")
        username = request.POST.get("register-username")
        password = request.POST.get("register-password")
        repassword = request.POST.get("register-repassword")
       
        submit = request.POST.get("submit")
      

    if (
            firstname is not None
            and lastname is not None
            and email is not None
            and username is not None
            and password is not None
            and repassword is not None
            and password == repassword
        ):
            hashed_password = make_password(password)
            newdata = Person(
                firstname=firstname,
                lastname=lastname,
                email=email,
                username=username,
                password=hashed_password,
                repassword=hashed_password
            )
            newdata.save()
            return render(request, "blog/login.html")
    else:
            return render(request, "blog/blogs.html")


def send_person(request):
     if request.method == "POST":
        username = request.POST.get("login-username")
        password = request.POST.get("login-password")
        submit = request.POST.get("login-submit")

        if username is not None and password is not None:
            # Kullanıcı adı ve parola ile eşleşen bir kullanıcı var mı kontrol et
            user_exists = Person.objects.filter(username=username).exists()

            if user_exists:
                # Kullanıcı varsa, şifreleri karşılaştır
                user = Person.objects.get(username=username)
                if check_password(password, user.password):
                    # Şifreler eşleşirse, kullanıcıyı yönlendir

                    return redirect("index")
                    
                else:
                    # Şifreler eşleşmezse, hata mesajını göster veya başka bir işlem yap
                    return render(request, "blog/login.html")
            else:
                # Kullanıcı yoksa, hata mesajını göster veya başka bir işlem yap
                return render(request, "blog/login.html")
        else:
            # Gerekli alanlar eksikse, hata mesajını göster veya başka bir işlem yap
            return render(request, "blog/login.html")
        
        
def send_product(request):
    print(request.POST)
    if request.method == "POST":
        urun_adi = request.POST.get("urun_adi")
        urun_kategori = request.POST.get("urunkategori")
        urun_aciklamasi = request.POST.get("urun_aciklamasi")
        urun_durum = request.POST.get("urun_durum")
        urun_mekani = request.POST.get("urun_mekani")
        sehir = request.POST.get("sehir")
        universite = request.POST.get("universite")
        gorsel = request.FILES.get("gorsel")
        karsi_takas = request.POST.get("karsi_takas")
        # Kullanıcı oturum açmışsa, request.user üzerinden kullanıcıya ulaşabilirsiniz
    
    
    new_product = Product(
                urun_adi=urun_adi,
                urun_kategori=kategori_list[int(urun_kategori)-1],
                urun_aciklamasi=urun_aciklamasi,
                urun_durum=urun_durum,
                urun_mekani=urun_mekani,
                sehir=city_list[int(sehir)-1],
                universite=university_list[int(universite)-1],
                gorsel=gorsel,
                karsi_takas=karsi_takas
            )
    new_product.save()      
    return redirect("blog-details")       

def send_homepage(request):
    return redirect("blog-details")
def remove_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return redirect('blog-details') 

def products_details(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.gorsel = os.path.basename(str(product.gorsel))
    return render(request, 'blog/products_details.html', {"product":product}) 