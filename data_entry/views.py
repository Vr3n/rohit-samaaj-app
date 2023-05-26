from django.views.generic import TemplateView

# Create your views here.


class DataEntryFormView(TemplateView):
    """
    View for Data Entry Form.
    Consist all the forms required to save a new member.

    """

    template_name = "data_entry/index.html"
