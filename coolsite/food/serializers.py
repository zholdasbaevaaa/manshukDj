import io
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from .models import Food
# class FoodModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content


class FoodSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Food
        fields = "__all__"

# class FoodSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=255)
#     content = serializers.CharField()

#
# class FoodSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=255)
#     content = serializers.CharField()
#     time_create = serializers.DateTimeField()
#     time_update = serializers.DateTimeField()
#     is_published = serializers.BooleanField(default=True)
#     cat_id = serializers.IntegerField()
#
#     def create(self, validated_data):
#         return Food.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get("title", instance.title)
#         instance.content = validated_data.get("content", instance.content)
#         instance.time_update = validated_data.get("time_update", instance.time_update)
#         instance.is_published = validated_data.get("is_published", instance.is_published)
#         instance.cat_id = validated_data.get("cat_id", instance.cat_id)
#         instance.save()
#         return instance
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method DELETE not allowed"})
#         #
#         return Response({"post": "delete post " + str(pk)})

# def encode():
#     model = FoodModel('Хинкали', 'Content: Хинкали')
#     model_sr = FoodSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json, type(json), sep='\n')
#
#
# def decode():
#     stream = io.BytesIO(b'{"title":"Хинкали","content":"Content:Хинкали"}')
#     data = JSONParser().parse(stream)
#     serializer = FoodSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)