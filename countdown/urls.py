from django.urls import path
from .views import CountdownListView, CountdownDetailView, CountdownCreateView

urlpatterns = [
	path('', CountdownListView.as_view(), name='countdown_list'),
	path('<int:pk>/', CountdownDetailView.as_view(), name='countdown_detail'),
	path('create/', CountdownCreateView.as_view(), name='countdown_create')
]
# This might be needed, depending on your Django version
app_name = "countdown"