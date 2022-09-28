from django.urls import path
from views import jokes, joke, add_laugh

urlpatterns = [
    path('jokes', jokes),
    path('jokes/<int:id>', joke),
    path('jokes/<int:id>', add_laugh)
]
