from django import template
from django.contrib.contenttypes.models import ContentType
from django.db.models import Sum
from ..models import Donation


register = template.Library()

class BaseDonationNode(template.Node):
    def __init__(self, object_expr, var):
        self.object_expr, self.var = object_expr, var

    def render(self, context):
        obj = self.object_expr.resolve(context)
        content_type = ContentType.objects.get_for_model(obj)
        object_id = obj.id
        queryset = Donation.objects.filter(
                content_type=content_type,
                object_id=object_id)
        context[self.var] = self.process_queryset(queryset)
        return ''

    def process_queryset(self, queryset):
        raise NotImplementedError

class LatestDonationNode(BaseDonationNode):
    def process_queryset(self, queryset):
        return list(queryset)

class DonationSumNode(BaseDonationNode):
    def process_queryset(self, queryset):
        return queryset.aggregate(Sum('amount'))['amount__sum']

@register.tag(name="donation_list_for")
def get_donation_list(parser, token):
    """To Retrieve donation list of an object
    Syntax::
        {% donation_list_for [object] as [var]
    Example::
        {% donation_list_for project as donate_list %}
    """
    bits = token.contents.split()
    if len(bits) != 4:
        raise TemplateSyntaxError, "donation_list_for takes 3 args"
    if bits[2] != 'as':
        raise TemplateSyntaxError, "2nd arg must be `as`"
    obj = parser.compile_filter(bits[1])
    return LatestDonationNode(obj, bits[3])

@register.tag(name="donation_sum_for")
def donation_sum(parser, token):
    """To Retrieve donation list of an object
    Syntax::
        {% donation_sum_for [object] as [var]
    Example::
        {% donation_sum_for project as donate_sum %}
    """
    bits = token.contents.split()
    if len(bits) != 4:
        raise TemplateSyntaxError, "donation_list_for takes 3 args"
    if bits[2] != 'as':
        raise TemplateSyntaxError, "2nd arg must be `as`"
    obj = parser.compile_filter(bits[1])
    return DonationSumNode(obj, bits[3])
