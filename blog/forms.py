from django import forms

class MessageForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        required=False,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Name not required"
        })
    )

    email = forms.CharField(
        required=False,
         widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "Mail not required"
        })
    )

    body = forms.CharField(
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "placeholder": "Write your message :)"
        })
    )


class CommentForm(forms.Form):
    comment = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control comment",
            "placeholder": "Leave your comment!"
        })
    )