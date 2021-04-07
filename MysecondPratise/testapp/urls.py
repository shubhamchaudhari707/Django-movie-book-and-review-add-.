from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('details/<int:id>/', views.view_details, name='details'),
    # path('demo/', views.demo_details, name='demo'),

    path('admin/', views.admin_panel, name='admin'),
    path('movies/', views.movies_adminpanel, name='movies'),
    path('category/', views.category_info, name='category'),
    path('language/', views.language_info, name='language'),

    path('delete/<int:id>/', views.DeleteMovie, name='delete'),
    path('deletecategory/<int:id>/', views.deleteCategory, name='deletecategory'),
    path('deletelanguage/<int:id>/', views.deleteLanguages, name='deletelanguage'),

    path('updatemovies/<int:id>/', views.update_data_movie, name='updatemovies'),
    path('updatecategory/<int:id>/', views.update_data_category, name='updatecategory'),
    path('updatelanguage/<int:id>/', views.update_data_languages, name='updatelanguage'),

    path('bookmovie/<int:id>/',views.moviebook, name='bookmovie'),
    path('mybooking/',views.mybooking, name='mybooking'),
    path('totalbookings/<int:movie_id>/', views.totalbookings, name='totalbookings'),

    path('reviews_add/<int:movie_id>/', views.reviews_add, name='reviews_add'),

    path('userinformation/', views.userinformation ,name='userinformation')

]
