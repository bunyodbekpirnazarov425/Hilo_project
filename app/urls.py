from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='home'),
    # path('about/', about, name='about'),
    # path('contact/', contact, name='contact'),
    # path('products/', products, name='products'),
    # path('product/<int:product_id>', product_detail, name='product_detail'),
    # path('cart/', cart, name='cart'),
    # path('checkout/', checkout, name='checkout'),
    # path('search/', search, name='search'),
    # path('blog/', blog, name='blog'),
    # path('blog/<int:blog_id>', blog_detail, name='blog_detail'),
    # path('newsletters/', newsletters, name='newsletters'),
    # path('faq/', faq, name='faq'),
    # path('terms/', terms, name='terms'),
    # path('privacy/', privacy, name='privacy'),
    # path('sitemap/', sitemap, name='sitemap'),
    # path('404/', page_not_found,
]