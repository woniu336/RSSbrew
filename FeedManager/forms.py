from django import forms
from .models import Filter, Article, ProcessedFeed, OriginalFeed
from django.contrib import admin
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
import re

class FilterForm(forms.ModelForm):
    class Meta:
        model = Filter
        fields = '__all__'
        widgets = {
            'value': forms.Textarea(attrs={'cols': 20, 'rows': 1}),
        }

class ReadOnlyArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        widgets = {
            'content': forms.HiddenInput(),
        }

class ProcessedFeedAdminForm(forms.ModelForm):
    class Meta:
        model = ProcessedFeed
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ProcessedFeedAdminForm, self).__init__(*args, **kwargs)
#        toggle_digest_initial = self.initial.get('toggle_digest', self.instance.toggle_digest if self.instance else False)
#        if not toggle_digest_initial:
#            self.fields['digest_frequency'].widget = forms.HiddenInput()
#            self.fields['digest_time'].widget = forms.HiddenInput()
#            self.fields['additional_prompt_for_digest'].widget = forms.HiddenInput()
#            self.fields['send_full_article'].widget = forms.HiddenInput()

class OriginalFeedAdminForm(forms.ModelForm):
    class Meta:
        model = OriginalFeed
        fields = '__all__'

    def clean_url(self):
        urls = self.cleaned_data['url']
        # First replace any combination of spaces and commas with a single comma
        urls = re.sub(r'\s*,\s*', ',', urls)
        # Then split by either newlines or commas
        url_list = [url.strip() for url in re.split(r'[\n,]', urls)]
        # Filter out empty strings
        url_list = [url for url in url_list if url]
        
        # Validate each URL
        for url in url_list:
            try:
                URLValidator()(url)
            except ValidationError:
                raise ValidationError(f'Invalid URL format: {url}')
        
        return urls
