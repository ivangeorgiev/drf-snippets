from django.contrib.auth.models import User
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.HyperlinkedIdentityField( read_only=True, source="owner.username", view_name="user-detail")
    highlight = serializers.HyperlinkedIdentityField(  # new
        view_name="snippet-highlight", format="html"
    )

    class Meta:
        model = Snippet
        fields = (
            "id",
            "title",
            "code",
            "linenos",
            "language",
            "style",
            "owner",
            "highlight",
        )


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Snippet.objects.all()
    )

    class Meta:
        model = User
        fields = ("id", "username", "snippets")
