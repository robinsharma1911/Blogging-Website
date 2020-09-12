from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.LoginUser,name='login'),
    path('profile/',views.profile,name='profile'),
    path('signup/',views.signup,name='signup'),
    path('logout/',views.LogoutUser,name='logout'),
    path('base/',views.base,name='base'),
    path('add_blog/',views.add_blog,name='add_blog'),
    path('edit/',views.edit,name='edit'),
    path('about/',views.about,name='about'),

    #to carry username for show another user profile from database....
    path('anotheruser/<blog_uname>',views.anotheruser,name='anotheruser'),

    #Urls related to delete posts and profile_pic and bio's...
    path('delete_post/<post_id>',views.delete_post,name='delete_post'),
    path('delete_bio/<pic_bio>',views.delete_bio,name='delete_bio')
]
if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)