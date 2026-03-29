import unittest

from extract import extract_markdown_images, extract_markdown_links, extract_title


class TestRegex(unittest.TestCase):
    def test_extract_single_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual(
            [("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_multiple_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png), and also This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual(
            [("image", "https://i.imgur.com/zjjcJKZ.png"), ("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_single_markdown_link(self):
        matches = extract_markdown_links(
            "This is link [to my blog](https://ryanroyals.cloud)"
        )
        self.assertListEqual(
            [("to my blog", "https://ryanroyals.cloud")], matches)

    def test_extract_multiple_markdown_link(self):
        matches = extract_markdown_links(
            "This is link [to my blog](https://ryanroyals.cloud) and [to claires portfolio](https://clairewebber.design)"
        )
        self.assertListEqual(
            [("to my blog", "https://ryanroyals.cloud"), ("to claires portfolio", "https://clairewebber.design")], matches)


class TestTitleExtract(unittest.TestCase):
    def test_extract_title(self):
        markdown = (
            "# heading 1\n"
            "## heading 2\n"
            "body with a # in the middle"
        )
        self.assertEqual("heading 1", extract_title(markdown))

    def test_no_title(self):
        markdown = (
            "## heading 2\n"
            "body with a # in the middle"
        )
        self.assertEqual(None, extract_title(markdown))


if __name__ == "__main__":
    unittest.main()
