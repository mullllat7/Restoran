from rest_framework import serializers

from app.resto.models import Resto, Menu, Food, RestoImage, FoodImage, MenuImage


#------------------------------------Resto------------------------------
#------------------------------------Resto------------------------------


class RestoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Resto
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return representation


class RestoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resto
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        total_rating = [i.ratings for i in instance.ratings.all()]
        if len(total_rating) > 0:
            representation['total_rating'] = sum(total_rating) / len(total_rating)
        return representation


class RestoImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = RestoImage
        fields = ('image',)

    def _get_image_url(self, obj):
        if obj.image:
            url = obj.image.url
            request = self.context.get('request')
            if request is not None:
                url = request.build_absolute_uri(url)
        else:
            url = ''
            return url

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['image'] = self._get_image_url(instance)
        return representation
#------------------------------------Resto------------------------------
#------------------------------------Resto------------------------------


# -----------------------------MENU----------------------------------------
# -----------------------------MENU----------------------------------------

class MenuSerializer(serializers.ModelSerializer):

    class Meta:
        model = Menu
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = MenuImageSerializer(MenuImage.objects.filter(menu=instance.menu, ), many=True,
                                                       context=self.context).data
        return representation


class MenuImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = MenuImage
        fields = ('image',)

    def _get_image_url(self, obj):
        if obj.image:
            url = obj.image.url
            request = self.context.get('request')
            if request is not None:
                url = request.build_absolute_uri(url)
        else:
            url = ''
        return url

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['image'] = self._get_image_url(instance)
        return representation


class MenuDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = MenuImageSerializer(MenuImage.objects.filter(menu=instance.menu, ), many=True,
                                                      context=self.context).data
        return representation

# -----------------------------MENU----------------------------------------
# -----------------------------MENU----------------------------------------


# ------------------------------FOOD--------------------------------------------
# ------------------------------FOOD--------------------------------------------
class FoodSerializer(serializers.ModelSerializer):

    class Meta:
        model = Food
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = FoodImageSerializer(FoodImage.objects.filter(food=instance.id, ), many=True,
                                                       context=self.context).data
        return representation


class FoodImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = FoodImage
        fields = ('image',)

    def _get_image_url(self, obj):
        if obj.image:
            url = obj.image.url
            request = self.context.get('request')
            if request is not None:
                url = request.build_absolute_uri(url)
        else:
            url = ''
        return url

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['image'] = self._get_image_url(instance)
        return representation


class FoodDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = FoodImageSerializer(FoodImage.objects.filter(food=instance.id, ), many=True,
                                                         context=self.context).data
        return representation

# ------------------------------FOOD--------------------------------------------
# ------------------------------FOOD--------------------------------------------


