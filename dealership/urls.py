from django.urls import path
from .views import indexPageView
from .views import aboutPageView
from .views import contactPageView
from .views import createPageView
from .views import deletePageView
from .views import updatePageView
from .views import showSingleEntryPageView 


urlpatterns = [
    path('', indexPageView, name = 'index'),
    path('about/', aboutPageView, name = 'about'),
    path('contact/', contactPageView, name = 'contact'),
    path('create/', createPageView, name = 'create'),
    path('update/', updatePageView, name = 'update'),
    path('singleEntry/', showSingleEntryPageView, name = 'singleEntry'),
    path('delete/', deletePageView, name = 'delete'),
]