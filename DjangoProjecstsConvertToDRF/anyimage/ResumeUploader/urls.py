from django.conf import settings
from django.conf.urls.static import static
# make by me upper.
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='home'),
    path('<int:pk>', views.CandidateView.as_view(), name='candidate')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
