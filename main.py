"""CLI entrypoint for caption generation."""

from __future__ import annotations

import argparse

from caption_generator import CaptionRequest, generate_caption


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate captions for posts/reels")
    parser.add_argument("--platform", required=True, choices=["instagram", "linkedin", "facebook", "x"])
    parser.add_argument("--type", required=True, dest="content_type", choices=["post", "reel"])
    parser.add_argument("--professionalism", required=True, choices=["casual", "balanced", "professional"])
    parser.add_argument("--topic", required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    request = CaptionRequest(
        platform=args.platform,
        content_type=args.content_type,
        professionalism=args.professionalism,
        topic=args.topic,
    )
    print(generate_caption(request))


if __name__ == "__main__":
    main()
