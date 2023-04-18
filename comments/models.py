from django.db import models
from common.models import CommonModel


class Comment(CommonModel):
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="comment",
    )
    feed = models.ForeignKey(
        "feeds.Feed",
        on_delete=models.CASCADE,
        related_name="comment",
    )
    description = models.TextField(
        max_length=255,
    )

    def __str__(self) -> str:
        return f"{self.description}"

    @property
    def commentlikeCount(self):
        return self.commentlike.count()
