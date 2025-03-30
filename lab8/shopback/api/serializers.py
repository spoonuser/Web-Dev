from .models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
    class ProductSerializer(serializers.ModelSerializer):
        class Meta:
            model = Product
            fields = '__all__'
