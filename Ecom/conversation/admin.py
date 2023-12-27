from django.contrib import admin

from .models import Conversation, ConversaitonMessage


admin.site.register(Conversation)
admin.site.register(ConversaitonMessage)