from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from schema_graph.views import Schema

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("main.urls")),
    path("profile/",include("MyUser.urls")),
    path("schema/", Schema.as_view()),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
