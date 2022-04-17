from curses.ascii import HT
import re
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views import generic
from rest_framework.parsers import JSONParser
from .models import Question, Choice
from django.utils import timezone
from .serializers import QuestionSerializer, ChoiceSerializer, VoteSerializer, QuestionResultPageSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
"""
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        #Return the last five published questions.
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    """
# Create your views here.
@api_view(['GET','POST'])
def question_list(request):

    if request.method=='GET':
        template_name = 'polls/question_text.html'
        question_text=Question.objects.all()
        serializer=QuestionSerializer(question_text, many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        template_name = 'polls/question_text.html'
        #data=JSONParser().parse(request)
        serializer=QuestionSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def question_detail(request,pk):
    try:
        question=Question.objects.get(pk=pk)
    except Question.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        serializer=QuestionSerializer(question)
        return Response(serializer.data)

    elif request.method=='PUT':
        serializer=QuestionSerializer(question,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method=='DELETE':
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
@api_view(['POST'])
def choices_view(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    serializer = ChoiceSerializer(data=request.data)
    if serializer.is_valid():
        choice = serializer.save(question=question)
        return Response(ChoiceSerializer(choice).data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET', 'PATCH', 'DELETE'])
def question_detail_view(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'GET':
        serializer = QuestionSerializer(question)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        raise NotImplementedError("PATCH currently not supported")
    elif request.method == 'DELETE':
        raise NotImplementedError("DELETE currently not supported")


@api_view(['PATCH'])
def vote_view(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    serializer = VoteSerializer(data=request.data)
    if serializer.is_valid():
        choice = get_object_or_404(Choice, pk=serializer.validated_data['choice_id'], question=question)
        choice.votes += 1
        choice.save()
        return Response("Voted")
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def question_result_view(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    serializer = QuestionResultPageSerializer(question)
    return Response(serializer.data)


