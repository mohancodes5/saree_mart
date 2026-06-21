from django import template
from django.conf import settings

from allauth.socialaccount.models import SocialApp

register = template.Library()


@register.simple_tag
def has_social_provider(provider_name):
    """Return True when the specified social provider is configured for this site."""
    try:
        return SocialApp.objects.filter(provider=provider_name, sites__id=settings.SITE_ID).exists()
    except Exception:
        return False
