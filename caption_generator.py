"""Simple caption generator for posts and reels."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class CaptionRequest:
    platform: str
    content_type: str
    professionalism: str
    topic: str


_ALLOWED_PLATFORMS = {"instagram", "linkedin", "facebook", "x"}
_ALLOWED_CONTENT_TYPES = {"post", "reel"}
_ALLOWED_PROFESSIONALISM = {"casual", "balanced", "professional"}


def _normalize(value: str) -> str:
    return value.strip().lower()


def _validate(request: CaptionRequest) -> CaptionRequest:
    platform = _normalize(request.platform)
    content_type = _normalize(request.content_type)
    professionalism = _normalize(request.professionalism)
    topic = request.topic.strip()

    if platform not in _ALLOWED_PLATFORMS:
        raise ValueError(f"Unsupported platform: {request.platform}")
    if content_type not in _ALLOWED_CONTENT_TYPES:
        raise ValueError(f"Unsupported content type: {request.content_type}")
    if professionalism not in _ALLOWED_PROFESSIONALISM:
        raise ValueError(f"Unsupported professionalism level: {request.professionalism}")
    if not topic:
        raise ValueError("Topic cannot be empty")

    return CaptionRequest(platform, content_type, professionalism, topic)


def generate_caption(request: CaptionRequest) -> str:
    """Generate a caption based on platform, content type, and professionalism."""

    request = _validate(request)

    if request.content_type == "reel":
        opener = "Watch this reel"
    else:
        opener = "New post"

    if request.professionalism == "professional":
        tone = "A thoughtful perspective on"
    elif request.professionalism == "balanced":
        tone = "Insights on"
    else:
        tone = "Quick update on"

    if request.platform == "linkedin":
        closing = "What has your experience been?"
    elif request.platform == "instagram":
        closing = "Save and share if this helped!"
    elif request.platform == "facebook":
        closing = "Let me know your thoughts in the comments."
    else:  # x
        closing = "Thoughts?"

    return f"{opener}: {tone} {request.topic}. {closing}"
