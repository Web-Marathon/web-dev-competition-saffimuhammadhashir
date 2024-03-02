# chat/forms.py

from django import forms
from .models import ChatRoom, ChatMessage

from django import forms
from .models import ChatRoom

class ChatRoomForm(forms.ModelForm):
    class Meta:
        model = ChatRoom
        fields = ['name', 'description']


class ChatMessageForm(forms.ModelForm):
    class Meta:
        model = ChatMessage
        fields = ['content']

    def __init__(self, *args, **kwargs):
        super(ChatMessageForm, self).__init__(*args, **kwargs)
        # Customize form field attributes if needed
        self.fields['content'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Type your message here'})
