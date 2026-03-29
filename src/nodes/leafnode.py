from nodes.htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError
        if self.tag is None:
            return self.value
        if self.value == "":
            return f"<{self.tag}{self.props_to_html()}/>"
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def props_to_html(self):
        propsString = ""
        if self.props is None:
            return propsString
        for prop in self.props:
            propsString += f' {prop}="{self.props[prop]}"'
        return propsString

    def __eq__(self, other):
        return (
            self.tag == other.tag
            and self.value == other.value
            and self.props == other.props
        )

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
