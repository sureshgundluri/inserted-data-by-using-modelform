from  django import forms
from app.models import *

class Topicforms(forms.Form):
    topic_name=forms.CharField(max_length=30)

class Modelform_topic(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'

class Modelform_webpage(forms.ModelForm):
    class Meta:
        model=Webpage
        fields='__all__'

class Modelform_access(forms.ModelForm):
    class Meta:
        model=AccessRecords
        fields='__all__'