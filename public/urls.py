from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from . import views

urlpatterns = [
    path('', views.index),
    path('new/note/', views.save_text, name="Add-new-note"),
    path('notes/all/', views.get_all_notes, name="Show-all-notes"),
    path('notes/delete/<int:id>', views.delete_by_id, name="Delete-by-id"),
    path('notes/edit/<int:id>', views.update_by_id, name="Edit-note"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)