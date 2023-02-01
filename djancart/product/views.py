from django.shortcuts import render

from .models import Product, Category
from .serializers import ProductSerializer

from rest_framework.views import APIView
from rest_framework.response import Response


class LatestProductList(APIView):
	def get(self, request, format=None):
		products = Product.objects.all()[0:4]
		serializer = ProductSerializer(products, many=True)
		return Response(serializer.data)


class ProductDetail(APIView):
		# check the url first
	def get_object(self, category_slug, product_slug):
		try:
			return Product.objects.filter(category_slug=category_slug).get(slug=product_slug)
		except Product.DoesNotExist:
			raise Http404

		# then get the products
	def get(self, request, category_slug, product_slug, format=None):
		product = self.get_object(self, category_slug, product_slug)		
		serializer = ProductSerializer(product)
		return Response(serializer.data)