from django.urls import URLPattern, path
from . import views

URLPattern=[
    path("",views.entry),
    path("index",views.index,name="index"),
    path("showposting",views.showPosting,name="showposting"),
    path("like",views.like,name="like"),
    path("collect",views.collect,name="collect"),
    path("comment",views.addComment,name="comment"),
    path("register",views.register,name='register'),
    path("login",views.log_view,name="login"),
    path("logout",views.logout_view,name="logout"),
    path("myself",views.Showmyself,name='myself')
]