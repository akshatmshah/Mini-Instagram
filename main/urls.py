from django.urls import path
from . import views

app_name = "insta"

urlpatterns = [
    # path('', views.IndexView.as_view(), name='index'),
    path("logout.html/", views.logout_request, name="logout"),
    path("login.html/", views.login_request, name="login"),
    path("register.html/", views.register, name='register'),
    # path("create_post.html", views.create_post, name="create"),
    path("", views.homepage, name="homepage"),
    path('<int:username>/', views.get_user_profile, name="profile"),
    # path("home.html/", views.feed, name="feed")
]
