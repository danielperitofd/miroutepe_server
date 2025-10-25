
from django.contrib import admin
from django.urls import path, include

from django.conf.urls import handler404
from django.shortcuts import render
from django.http import Http404

# Definindo uma view personalizada para o erro 404
def custom_404(request, exception):
    # Pegando a URL da página que causou o erro
    page_name = request.path.split('/')[-1]  # Pega o último segmento da URL
    return render(request, 'em_construcao.html', {'page_name': page_name}, status=404)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  #
]

# Associe a view ao erro 404
handler404 = custom_404


