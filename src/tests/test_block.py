import unittest

from nodes.block import BlockType
from extract import block_to_block_type


class TestBlockToBlockType(unittest.TestCase):
    def test_headings(self):
        blocks = [
            "# Heading 1",
            "## Heading 2",
            "### Heading 3",
            "#### Heading 4",
            "#####  Heading 5",
            "###### Heading 6",
        ]
        expected = [
            BlockType.HEADING,
            BlockType.HEADING,
            BlockType.HEADING,
            BlockType.HEADING,
            BlockType.HEADING,
            BlockType.HEADING
        ]
        result = []
        for block in blocks:
            result.append(block_to_block_type(block))

        self.assertEqual(result, expected)

    def test_heading_out_of_scope(self):
        self.assertEqual(block_to_block_type("####### Heading 7"), BlockType.PARAGRAPH)

    def test_code(self):
        block = (
            "```\n"
            'print("hello_world")\n'
            "```"
        )
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_quote(self):
        block = (
            "> Hello\n"
            "> This is a quote\n"
            ">Note that I dont have a space"
        )
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

    def test_unordered_list(self):
        block = (
            "- this is a good list\n"
            "- and we all have our spaces\n"
            "- we love markdown lists"
        )
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        block = (
            "1. this is a ordered list\n"
            "2. and we all have our numbers\n"
            "3. we love markdown lists"
        )
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

    def test_paragraph(self):
        block = (
            "I'm just a boring paragraph\n"
            "No tricks, no pizzazz"
        )
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
