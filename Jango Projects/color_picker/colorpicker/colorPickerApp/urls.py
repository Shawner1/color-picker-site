from django.urls import path

from colorPickerApp.views import ColorPickerView

urlpatterns = [
    # paintapp/
    path('', ColorPickerView.as_view(), name='paint'),
]