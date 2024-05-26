from django.urls import path, include
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index, name='home'),
    path('active-users', views.active_users, name='active-users'),
    path('about', views.about, name='about'),
    path('sign-in', views.sign_in, name='sign-in'),
    path('sign-up', views.sign_up, name='sign-up'),
    path('profile', views.profile, name='profile'),
    path('logout', views.logout_user, name='logout'),
    path(
        "redoc/",
        TemplateView.as_view(
            template_name="pet_shop/redoc.html", extra_context={"schema_url": "openapi-schema"}
        ),
        name="redoc",
    ),
]
