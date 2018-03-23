from django.urls import path

from movies import views



urlpatterns = [
    path('movies/', views.hello_world)
   #path('articles/<int:year>/', views.year_archive),
    #path('articles/<int:year>/<int:month>/', views.month_archive),
    #path('articles/<int:year>/<int:month>/<slug:slug>/', views.article_detail),
]