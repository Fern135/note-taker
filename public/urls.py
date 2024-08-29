from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from . import views

urlpatterns = [
    path('', views.index),
    path('new/note/', views.save_text),
    path('notes/all/', views.get_all_notes)

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)