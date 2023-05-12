class Html:
    def __init__(self, subelement=None):
        self.subelement = subelement

    def __str__(self):
        if self.subelement:
            return f"<html>{str(self.subelement)}</html>"
        else:
            return "<html></html>"


class Body:
    def __init__(self, text=None, subelement=None):
        self.text = text
        self.subelement = subelement

    def __str__(self):
        if self.text and self.subelement:
            return f"<body>{self.text}{str(self.subelement)}</body>"
        elif self.text:
            return f"<body>{self.text}</body>"
        elif self.subelement:
            return f"<body>{str(self.subelement)}</body>"
        else:
            return "<body></body>"


class P:
    def __init__(self, text=None):
        self.text = text

    def __str__(self):
        if self.text:
            return f"<p>{self.text}</p>"
        else:
            return "<p></p>"
para = P(text="this is some body text")
doc_body = Body(text="This is the body", subelement=para)
doc = Html(subelement=doc_body)
print(doc)