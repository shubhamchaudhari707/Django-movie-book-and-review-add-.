from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib import messages
import datetime
from .models import Movies
from .models import MyCategory
from .models import MyLanguges
from .models import BookMovie
from .models import Myuser
from .models import ReviewMovie

from django.contrib.auth.decorators import login_required, user_passes_test


# Create your views here.
@login_required(login_url='/')
def home(request):
    movies = Movies.objects.all().order_by('-id')
    return render(request, 'testapp/home.html', {"movies": movies})


def signup(request):
    if request.method == 'POST':
        nm = request.POST['name']
        us = request.POST['username']
        em = request.POST['email']
        pw1 = request.POST['password1']
        pw2 = request.POST['password2']

        if pw1 == pw2:
            if Myuser.objects.filter(username=us).exists():
                messages.info(request, 'username already taken !!')
                return redirect('signup')
            elif Myuser.objects.filter(email=em).exists():
                messages.info(request, 'email already taken !!')
                return redirect('signup')
            else:
                user = Myuser.objects.create_user(first_name=nm, username=us, email=em, password=pw1)
                user.save()

                messages.info(request, 'Signup Created Successfully !!')
                return redirect('login')

        else:
            messages.info(request, 'Password is not matching !!')
            return redirect('signup')

    else:
        return render(request, 'testapp/signup.html')


def login(request):
    if request.method == 'POST':
        us = request.POST['username']
        pw1 = request.POST['password1']

        user = auth.authenticate(username=us, password=pw1)

        if user is None:
            messages.info(request, 'invailid credentials ')
            return redirect('login')
        else:
            auth.login(request, user)
            if user.is_superuser:
                return redirect('admin')
            else:
                return redirect('home')
    else:
        return render(request, 'testapp/login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')


def view_details(request, id):
    movie = Movies.objects.get(pk=id)
    return render(request, 'testapp/view.html', {'movie': movie})


# def demo_details(request):
#     movie = Movies.objects.all()
#     categories = MyCategory.objects.all()
#     languages = MyLanguges.objects.all()
#
#     if request.method == 'POST':
#         title = request.POST['title']
#         description = request.POST['description']
#         image = request.FILES['image']
#         category = request.POST['category']
#         languages = request.POST['languages']
#         cast = request.POST['cast']
#         year_of_production = request.POST['year_of_production']
#         slug = request.POST['slug']
#
#         reg = Movies.objects.create(title=title, description=description, image=image, category_id=category,
#                                     language_id=languages, cast=cast,
#                                     year_of_production=year_of_production,
#                                     slug=slug)
#         reg.save()
#         return redirect('home')
#     else:
#         return render(request, 'testapp/demo.html',
#                       {'movies': movie, 'categories': categories, 'languages': languages})

def check_admin(user):
    return user.is_superuser


@login_required(login_url='/')
@user_passes_test(check_admin, login_url='/')
def admin_panel(request):
    movie = Movies.objects.all()
    categories = MyCategory.objects.all()
    languages = MyLanguges.objects.all()

    return render(request, 'testapp/admin.html', {'movie': movie, 'categories': categories, 'languages': languages})


def movies_adminpanel(request):
    # movie = Movies.objects.all()
    categories = MyCategory.objects.all()
    languages = MyLanguges.objects.all()

    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        image = request.FILES['image']
        price = request.POST['price']
        category = request.POST['category']
        languages = request.POST['languages']
        cast = request.POST['cast']
        year_of_production = request.POST['year_of_production']
        slug = request.POST['slug']

        reg = Movies.objects.create(title=title, description=description, image=image, category_id=category,
                                    language_id=languages, cast=cast,
                                    year_of_production=year_of_production,
                                    slug=slug, price=price)
        reg.save()
        return redirect('home')
    else:
        return render(request, 'testapp/movies.html',
                      {'categories': categories, 'languages': languages})


def category_info(request):
    if request.method == 'POST':
        category = request.POST['category']
        reg = MyCategory(category=category)
        reg.save()
        return redirect('admin')
    else:
        return render(request, 'testapp/category.html')


def language_info(request):
    if request.method == 'POST':
        language = request.POST['languages']
        reg = MyLanguges(language=language)
        reg.save()
        return redirect('admin')
    else:
        return render(request, 'testapp/language.html')


def DeleteMovie(request, id):
    if request.method == 'POST':
        mo = Movies.objects.get(pk=id)
        mo.delete()
        return redirect('admin')


def deleteCategory(request, id):
    if request.method == 'POST':
        ca = MyCategory.objects.get(pk=id)

        ca.delete()
        return redirect('admin')


def deleteLanguages(request, id):
    if request.method == 'POST':
        la = MyLanguges.objects.get(pk=id)

        la.delete()
        return redirect('admin')


def update_data_movie(request, id):
    mo = Movies.objects.get(pk=id)
    ca = MyCategory.objects.all()
    la = MyLanguges.objects.all()
    if request.method == 'POST':
        mo.title = request.POST['title']
        mo.description = request.POST['description']
        # mo.image = request.FILES['image']
        mo.category_id = request.POST['category']
        mo.language_id = request.POST['languages']
        mo.cast = request.POST['cast']
        mo.year_of_production = request.POST['year_of_production']
        mo.slug = request.POST['slug']
        mo.price = request.POST['price']

        mo.save()
        return redirect('home')
    else:
        return render(request, 'testapp/movies.html', {'movies': mo, 'categories': ca, 'languages': la})


def update_data_category(request, id):
    pi = MyCategory.objects.get(pk=id)
    if request.method == 'POST':
        pi.category = request.POST['category']
        pi.save()
        return redirect('admin')
    else:
        return render(request, 'testapp/category.html', {'data': pi})


def update_data_languages(request, id):
    pi = MyLanguges.objects.get(pk=id, )
    if request.method == 'POST':
        pi.language = request.POST['languages']
        pi.save()
        return redirect('admin')
    else:
        return render(request, 'testapp/language.html', {'data': pi})


def moviebook(request, id):
    print('movie : ', id)
    print('user : ', request.user)
    date = request.POST['booking_date']
    valid_date = datetime.datetime.strptime(date, '%Y-%m-%d')
    try:
        already_book = BookMovie.objects.get(movie_id=id, user=request.user, booking_date=date)
        print('found : ', already_book)
        print('You already book this movie')
        messages.info(request, ' You already book this movie Only one Movie Book For Today ..')

    except BookMovie.DoesNotExist:
        print('not found')
        today = datetime.datetime.today()
        print(today)
        if today < valid_date:
            print(valid_date)
            print(today < valid_date)
            book_movie_obj = BookMovie(movie_id=id, user=request.user, booking_date=valid_date)
            print(date)

            login_user = request.user
            print('wallet amount user = ', login_user.wallet_amount)

            print('movie amount = ', book_movie_obj.movie.price)

            if book_movie_obj.movie.price <= login_user.wallet_amount:
                print('enough  balance')
                book_movie_obj.save()
                login_user.wallet_amount = login_user.wallet_amount - book_movie_obj.movie.price
                login_user.save()

            else:
                print('Not Insufficient balance ')
                messages.info(request, ' Not Insufficient balance !!')
            print('save success')

        else:
            print('not valid date')
            messages.info(request, ' not valid date !!')

    return redirect('mybooking')


def mybooking(request):
    booking_movies_obj = BookMovie.objects.filter(user=request.user)

    return render(request, 'testapp/mybooking.html', {'bookings': booking_movies_obj})


def totalbookings(request, movie_id):
    booking_movies_obj = BookMovie.objects.filter(movie_id=movie_id)
    return render(request, 'testapp/totalbookings.html', {'bookings': booking_movies_obj})


def reviews_add(request, movie_id):
    user = request.user
    print(movie_id)
    print(user)
    if request.method == 'POST':
        rating = request.POST['rating']
        reviews = request.POST['reviews']
        reg = ReviewMovie(rating=rating, reviews=reviews, user=request.user, movie_id=movie_id)
        reg.save()
        login_user = request.user
        login_user.wallet_amount = login_user.wallet_amount + 10
        login_user.save()
    return redirect('details', id=movie_id)


def userinformation(request):
    customer = Myuser.objects.exclude(id=request.user.id)
    return render(request, 'testapp/users.html', {'customers': customer})
