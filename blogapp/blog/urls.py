
from django.urls import path


from. import views
#http://127.0.0.1:8000/          => homepage
#http://127.0.0.1:8000/index     => homepage
#http://127.0.0.1:8000/blogs     => blogs
#http://127.0.0.1:8000/blogs/3   => blogs-detail

urlpatterns = [
    path('send_info/', views.send_info, name='send_info'),
    path('send_person/', views.send_person, name='send_person'),
    path('send_product/', views.send_product, name='send_product'),
    path('send_homepage/', views.send_homepage, name='send_homepage'),
     path('remove_product/<int:product_id>/', views.remove_product, name='remove_product'),
 
    path("",views.login),   #URL geldiğinde karşılığında index fonksiyonunu kullanıcının tarayıcısına gönderdik
    path("index", views.index, name='index'),  #http://127.0.0.1:8000/ , http://127.0.0.1:8000/index kullanıcı iki url ile de gelse aynı method çağrılsın
    path("blogs",views.blogs,  name='blogs'),
    path('blog-details/', views.blog_details, name='blog-details'),   #degiskenin ismini tanımladık
    path('products_details/<int:product_id>/', views.products_details, name='products_details'), 
    path("login", views.login, name='login'),
    path("download",views.download,  name='download'),
  
    path("aciklama1",views.aciklama1, name="aciklama1"),
    path("aciklama2",views.aciklama2, name="aciklama2")
]

