from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .yasg import urlpatterns as doc_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('app.account.urls')),
    path('restoran/', include('app.resto.urls')),
    path('order/', include('app.order.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += doc_urls