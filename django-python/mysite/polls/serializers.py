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
    def create(self, validated_data):
        return Question.objects.create(**validated_data)

class QuestionListPageSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    question_text = serializers.CharField(max_length=200)
    pub_date = serializers.DateTimeField()
    was_published_recently = serializers.BooleanField(read_only=True) # Serializer is smart enough to understand that was_published_recently is a method on Question

    def create(self, validated_data):
        return Question.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class QuestionDetailPageSerializer(QuestionListPageSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)

class VoteSerializer(serializers.Serializer):
    choice_id = serializers.IntegerField()

class ChoiceSerializerWithVotes(ChoiceSerializer):
    votes = serializers.IntegerField(read_only=True)

class QuestionResultPageSerializer(QuestionListPageSerializer):
    choices = ChoiceSerializerWithVotes(many=True, read_only=True)

