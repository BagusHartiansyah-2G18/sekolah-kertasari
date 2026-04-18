from django import forms
from .models import ContactMessage
import re

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded-lg px-4 py-3 focus:outline-none focus:ring-2 focus:ring-green-600'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full border border-gray-300 rounded-lg px-4 py-3 focus:outline-none focus:ring-2 focus:ring-green-600'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded-lg px-4 py-3 focus:outline-none focus:ring-2 focus:ring-green-600'
            }),
            'message': forms.Textarea(attrs={
                'class': 'w-full border border-gray-300 rounded-lg px-4 py-3 focus:outline-none focus:ring-2 focus:ring-green-600',
                'rows': 5
            }),
        }

    # Validasi nama
    def clean_name(self):
        name = self.cleaned_data.get('name')

        if len(name) < 3:
            raise forms.ValidationError("Nama terlalu pendek")

        return name

    # Validasi subject
    def clean_subject(self):
        subject = self.cleaned_data.get('subject')

        if len(subject) < 5:
            raise forms.ValidationError("Subject terlalu pendek")

        return subject

    # Validasi message
    def clean_message(self):
        message = self.cleaned_data.get('message')

        if len(message) < 10:
            raise forms.ValidationError("Pesan terlalu pendek")

        # anti link spam sederhana
        if re.search(r'http|www', message.lower()):
            raise forms.ValidationError("Tidak boleh mengandung link")

        return message