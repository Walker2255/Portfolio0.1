from django.urls import path
from .views import BlogPageView
from .views import HomePageView
from .views import AboutPageView
from .views import WorksPageView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('blog/', BlogPageView.as_view(), name='blog'),
    path('works/', WorksPageView.as_view(), name='works'),
    path('about/', AboutPageView.as_view(), name='about'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
