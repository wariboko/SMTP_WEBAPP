
'''
class ContactForm(forms.Form):
    sender = forms.EmailField(label='Sender', widget=forms.EmailInput(attrs={'class': 'form-control form-control-sm'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control form-control-sm'}))
    host = forms.CharField(label='Host', widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}))
    port = forms.IntegerField()
    subject = forms.CharField(label='Subject', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}))
    recipients = forms.CharField(label='Recipients', widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}))
    message = forms.CharField(label='Message',  widget=forms.Textarea(attrs={'class': 'form-control'}))
    '''