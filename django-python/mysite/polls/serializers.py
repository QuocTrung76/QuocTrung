from rest_framework import serializers
from .models import Question, Choice

"""
Serializer
"""


# class QuestionSerializers(serializers.Serializer):
#     question_text = serializers.CharField(max_length=200)
#     pub_date = serializers.DateTimeField()

#     def create(self,validate_data):
#         return Question.objects.create(validate_data)

#     def update(self, instance, validate_data):
#         instance.question_text=validate_data.get('question_text', instance.question_text)
#         instance.pub_date=validate_data.get('pub_date', instance.pub_date)
#         instance.save()
#         return instance


"""
ModelSerializer
"""
class ChoiceSerializer(serializers.Serializer):
    choice_text=serializers.CharField(max_length=200)

    def create(self, validated_data):
        return Choice.objects.create(**validated_data)
class QuestionSerializer(serializers.Serializer):
    question_text=serializers.CharField(max_length=200)
    pub_date=serializers.DateTimeField()
    choices=ChoiceSerializer(many=True, read_only=True)
    def craete(self, validate_data):
        return Question.objects.create(**validated_data)

