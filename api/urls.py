# from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from .views import (
   	# for-items
    ItemList,
    ItemUpdateAPI,
	ItemDestroyAPI,
	ItemDetailView,
	ItemCreateAPI,
	# for-item/s
	# for-categorys
	CategoryList,
    CategoryUpdateAPI,
	CategoryDestroyAPI,
	CategoryDetailView,
	CategoryCreateAPI,
	# for-categorys

	# for-categorys
	MenuList,
    MenuUpdateAPI,
	MenuDestroyAPI,
	MenuDetailView,
	MenuCreateAPI,
	# for-categorys

	# for-Resturant-Brach
	RestaurantList,
    RestaurantUpdateAPI,
	RestaurantDestroyAPI,
	RestaurantDetailView,
	RestaurantCreateAPI,
	# for-Resturant-Brach



)


urlpatterns = [
    url(r'^items/$', ItemList.as_view(), name='items'),
    url(r'^item-create$', ItemCreateAPI.as_view(), name='item-create'),
    url(r'^item/(?P<id>\d+)/$', ItemDetailView.as_view(), name='item-details'),
    url(r'^item/(?P<id>[\w-]+)/edit/$',ItemUpdateAPI.as_view(), name='item-edit'),
    url(r'^item/(?P<id>[\w-]+)/delete$',ItemDestroyAPI.as_view(), name='item-detroy'),

    url(r'^categorys/$', CategoryList.as_view(), name='categorys'),
    url(r'^category-create$', CategoryCreateAPI.as_view(), name='category-create'),
    url(r'^category/(?P<id>\d+)/$', CategoryDetailView.as_view(), name='category-details'),
    url(r'^category/(?P<id>[\w-]+)/edit/$',CategoryUpdateAPI.as_view(), name='category-edit'),
    url(r'^category/(?P<id>[\w-]+)/delete$',CategoryDestroyAPI.as_view(), name='category-detroy'),

	url(r'^menus/$', MenuList.as_view(), name='menus'),
    url(r'^menu-create$', MenuCreateAPI.as_view(), name='menu-create'),
    url(r'^menu/(?P<id>\d+)/$', MenuDetailView.as_view(), name='menu-details'),
    url(r'^menu/(?P<id>[\w-]+)/edit/$',MenuUpdateAPI.as_view(), name='menu-edit'),
    url(r'^menu/(?P<id>[\w-]+)/delete$',MenuDestroyAPI.as_view(), name='menu-detroy'),


    url(r'^restaurants/$', RestaurantList.as_view(), name='restaurants'),
    url(r'^restaurant-create$', RestaurantCreateAPI.as_view(), name='restaurant-create'),
    url(r'^restaurant/(?P<id>\d+)/$', RestaurantDetailView.as_view(), name='restaurant-details'),
    url(r'^restaurant/(?P<id>[\w-]+)/edit/$',RestaurantUpdateAPI.as_view(), name='restaurant-edit'),
    url(r'^restaurant/(?P<id>[\w-]+)/delete$',RestaurantDestroyAPI.as_view(), name='restaurant-detroy'),


]
