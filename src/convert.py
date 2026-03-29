from nodes.leafnode import LeafNode
from nodes.textnode import TextType, TextNode
from nodes.parentnode import ParentNode
from nodes.block import BlockType
from split import split_nodes_image, split_nodes_link
from delimeter import split_nodes_delimeter
from extract import block_to_block_type


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    htmlNodes = []
    for block in blocks:
        blockType = block_to_block_type(block)

        match blockType:
            case BlockType.CODE:
                htmlNodes.append(code_block_to_html_node(block))
            case BlockType.HEADING:
                htmlNodes.append(heading_block_to_html_node(block))
            case BlockType.QUOTE:
                htmlNodes.append(quote_block_to_html_node(block))
            case BlockType.ORDERED_LIST:
                htmlNodes.append(ordered_list_block_to_html_node(block))
            case BlockType.UNORDERED_LIST:
                htmlNodes.append(unordered_list_block_to_html_node(block))
            case BlockType.PARAGRAPH:
                htmlNodes.append(text_block_to_html_node(block))

    return ParentNode("div", htmlNodes)


# Goes through, pre planning for code blocks
# While cruising in a code block, just keep looking for the end
def markdown_to_blocks(markdown):
    new_blocks = []
    current_block = []
    in_code_fence = False
    for line in markdown.split("\n"):
        if line.startswith("```"):
            in_code_fence = not in_code_fence

        current_block.append(line)

        if not in_code_fence and line == "":
            block = "\n".join(current_block).strip()
            if block:
                new_blocks.append(block)
            current_block = []
    # flush remaining
    block = "\n".join(current_block).strip()
    if block:
        new_blocks.append(block)
    return new_blocks


def text_to_textnodes(text):
    new_nodes = [TextNode(text, TextType.TEXT)]
    new_nodes = split_nodes_delimeter(new_nodes, "**", TextType.BOLD)
    new_nodes = split_nodes_delimeter(new_nodes, "_", TextType.ITALIC)
    new_nodes = split_nodes_delimeter(new_nodes, "*", TextType.ITALIC)
    new_nodes = split_nodes_delimeter(new_nodes, "`", TextType.CODE)
    new_nodes = split_nodes_image(new_nodes)
    new_nodes = split_nodes_link(new_nodes)

    return new_nodes


def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        case _:
            raise Exception("text_node not valid TextType type")


def text_to_children(text):
    textNodes = text_to_textnodes(text)
    htmlNodes = []
    for node in textNodes:
        htmlNodes.append(text_node_to_html_node(node))

    return htmlNodes


def heading_block_to_html_node(text):
    count = 0
    for char in text:
        if char == "#":
            count += 1
        else:
            break
    stripped_text = text[count + 1 :]
    children = text_to_children(stripped_text)

    return ParentNode(f"h{count}", children)


def quote_block_to_html_node(text):
    lines = text.split("\n")

    new_lines = []
    for line in lines:
        new_lines.append(line.replace(">", "", 1).strip())
    new_text = " ".join(new_lines)
    children = text_to_children(new_text)

    return ParentNode("blockquote", children)


def ordered_list_block_to_html_node(text):
    lines = text.split("\n")

    children = []
    for line in lines:
        parts = line.split(" ", 1)
        sub_children = text_to_children(parts[1])
        children.append(ParentNode("li", sub_children))

    return ParentNode("ol", children)


def unordered_list_block_to_html_node(text):
    lines = text.split("\n")

    children = []
    for line in lines:
        parts = line.split(" ", 1)
        sub_children = text_to_children(parts[1])
        children.append(ParentNode("li", sub_children))

    return ParentNode("ul", children)


def code_block_to_html_node(text):
    first_line_end = text.index("\n")
    lang = text[3:first_line_end].strip()  # "python" from "```python
    content = text[first_line_end + 1 : -3]  # strip opening line and closing ```
    text_node = TextNode(content, TextType.TEXT)
    child_node = text_node_to_html_node(text_node)

    props = {"class": f"language-{lang}"} if lang else None
    code_node = ParentNode("code", [child_node], props)
    return ParentNode("pre", [code_node])


def text_block_to_html_node(text):
    children = text_to_children(text.replace("\n", " "))

    return ParentNode("p", children)
