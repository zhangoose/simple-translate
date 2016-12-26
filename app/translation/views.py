from rest_framework import viewsets, mixins

from app.translation.serializers import TranslationSerializer
from app.translation.models import Translation


class TranslationViewSet(mixins.RetrieveModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        viewsets.GenericViewSet):
    """
    Viewset for Translations.

    request type | allowed?
    -----------------------
    CREATE       | YES
    LIST         | YES
    RETRIEVE     | YES
    DESTROY      | YES
    UPDATE       | NO
    """
    serializer_class = TranslationSerializer
    queryset = Translation.objects.all().order_by("-timestamp")
