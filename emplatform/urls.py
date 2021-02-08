from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url,include
from django.urls import path
from .views import ProblemUpdateView,ProblemDeleteView
from . import views

urlpatterns=[
    path('',views.index,name = 'index'),
    path('home/',views.home, name = 'home'),
    path('signup/',views.signup , name='signup'),
    path('profile/<username>', views.profile, name='profile'),
    path('problems/',views.problem,name='problem'),
    path('problem/<pk>', views.tip, name='tip'),
    path('updateproblem/', views.updateproblem,name="update"),
    path('deleteproblem/', views.deleteproblem,name="delete"),
    path('post/<int:pk>/update/',ProblemUpdateView.as_view(), name="updateForm"),
    path('post/<int:pk>/delete/',ProblemDeleteView.as_view(), name="deleteForm"),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)