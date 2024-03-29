from django.contrib import admin
from django.urls import path, include
from product import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('account/', include('account.urls')),
    path('product/', include('product.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
