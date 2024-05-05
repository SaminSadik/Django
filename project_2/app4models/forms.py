from django import forms
from app4models.models import myModel

class Model_Form(forms.ModelForm):
    class Meta: # defines the behaviour of a class & provide additional info for the model
        model = myModel
        fields = '__all__' # to have all fields included in the form
        exclude = ['id',] # excludes specified fields from the form
        # either fields or exclude should be specified, fields can be specified like exclude
        labels = {
            'full_name': 'Name',
            'email_address': 'Email',
            'cgpa': 'CGPA',
            'checkbox': 'I agree to the terms and conditions',
            'profile': 'Profile URL'
        } # to change the display name of the form fields
        help_texts = {
            'full_name': 'Enter your Full name',
            'email_address': 'Enter your valid Email address',
            'cgpa': 'Enter your current CGPA',
            'profile': 'Enter the URL of your social media profile'
        } # to add a text under the form fields
        widgets = {
            'full_name': forms.Textarea(attrs={'rows':2, 'class':'border border-success'}),
            'checkboc': forms.Textarea(attrs={'id':'required'})
        } # adds widgets to the form fields
        error_messages = {
            'email_address': {'invalid-feedback': 'must be a valid & unique email address'},
        } # modifies the message thats displayed if an error occurs
