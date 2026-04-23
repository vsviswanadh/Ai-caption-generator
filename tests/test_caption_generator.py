import unittest

from caption_generator import CaptionRequest, generate_caption


class CaptionGeneratorTests(unittest.TestCase):
    def test_generates_linkedin_professional_post_caption(self):
        caption = generate_caption(
            CaptionRequest(
                platform="linkedin",
                content_type="post",
                professionalism="professional",
                topic="building reliable AI products",
            )
        )

        self.assertIn("New post", caption)
        self.assertIn("A thoughtful perspective on building reliable AI products", caption)
        self.assertTrue(caption.endswith("What has your experience been?"))

    def test_generates_instagram_casual_reel_caption(self):
        caption = generate_caption(
            CaptionRequest(
                platform="instagram",
                content_type="reel",
                professionalism="casual",
                topic="content planning",
            )
        )

        self.assertIn("Watch this reel", caption)
        self.assertIn("Quick update on content planning", caption)
        self.assertTrue(caption.endswith("Save and share if this helped!"))


    def test_generates_facebook_balanced_post_caption(self):
        caption = generate_caption(
            CaptionRequest(
                platform="facebook",
                content_type="post",
                professionalism="balanced",
                topic="team collaboration",
            )
        )

        self.assertIn("New post", caption)
        self.assertIn("Insights on team collaboration", caption)
        self.assertTrue(caption.endswith("Let me know your thoughts in the comments."))

    def test_generates_x_balanced_reel_caption(self):
        caption = generate_caption(
            CaptionRequest(
                platform="x",
                content_type="reel",
                professionalism="balanced",
                topic="product updates",
            )
        )

        self.assertIn("Watch this reel", caption)
        self.assertIn("Insights on product updates", caption)
        self.assertTrue(caption.endswith("Thoughts?"))

    def test_rejects_empty_topic(self):
        with self.assertRaises(ValueError):
            generate_caption(
                CaptionRequest(
                    platform="linkedin",
                    content_type="post",
                    professionalism="balanced",
                    topic="   ",
                )
            )

    def test_rejects_unsupported_platform(self):
        with self.assertRaises(ValueError):
            generate_caption(
                CaptionRequest(
                    platform="youtube",
                    content_type="post",
                    professionalism="balanced",
                    topic="growth",
                )
            )


if __name__ == "__main__":
    unittest.main()
