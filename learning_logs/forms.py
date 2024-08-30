from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text' : ''}


class EntryForm(forms.ModelForm):

    class Meta:

        model = Entry
        fields = ['text']
        labels = {'text' : 'Entry'}
        widgets = {'text' : forms.Textarea(attrs={'cols' :80,'class': 'border border-gray-300 rounded-lg p-2 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'})}