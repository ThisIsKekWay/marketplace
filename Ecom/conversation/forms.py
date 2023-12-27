from django import forms

from .models import Conversation, ConversaitonMessage


class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model = ConversaitonMessage
        fields = ['content',]

        labels = {
            'content': 'Сообщение',
        }

        widgets = {
            'content': forms.Textarea(attrs={'class': 'w-full py-4 px-6 rounded-xl border', 'rows': 4}),
        }
