from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from . models import Product

def validate_title(value):
    qs = Product.objects.filter(title__iexact=value)
    if qs.exist():
        raise serializers.ValidationError(f"{value} is already a product name")
    return value

def validate_title_no_Hello(value):
    if "Hello" in value.lower():
        raise serializers.ValidationError(f"{value} is not allow ")
    return value

unique_product_title = UniqueValidator(queryset=Product.objects.all(), loookup='iexact')