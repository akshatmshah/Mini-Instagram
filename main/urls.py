from django.urls import path
from . import views

app_name = "insta"

urlpatterns = [
    path("logout.html/", views.logout_request, name="logout"),
    path("login.html/", views.login_request, name="login"),
    path("register.html/", views.register, name='register'),
    path("posts.html", views.create_post, name="create"),
    path("", views.homepage, name="homepage"),
    path('<int:username>/', views.get_user_profile, name="profile"),
    path("home.html/", views.Feed.as_view(), name="feed"),
    path('delete/<post_id>', views.delete_post, name='delete')
]
