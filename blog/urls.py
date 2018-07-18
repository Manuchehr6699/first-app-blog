from . import views
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),


    url(r'^register/$', views.register, name='register'),

    #login/logout urls
    #url(r'^login/$', views.user_login, name='login'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^logout-then-login/$', auth_views.logout_then_login, name='logout_then_login'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),

    #change password urls
    url(r'^password-change/$', auth_views.password_change, name='password_change'),
    url(r'^password-change/done/$', auth_views.password_change_done, name='password_change_done'),

    # restore password urls
    url(r'^password-reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password-reset/done/$', views.password_reset_done, name='password_reset_done'),
    url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^password-reset/complete/$', auth_views.password_reset_complete, name='password_reset_complete'),

    #prof
    url(r'^edit/$', views.edit, name='edit'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


