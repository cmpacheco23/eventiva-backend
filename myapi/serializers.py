from rest_framework import serializers

class PollSerializer(serializers.ModelSerializer):
  class Meta:
    model = Poll 
    fields = ['option1', 'option2', 'option3', 'option4', 'option5', 'option6']
    