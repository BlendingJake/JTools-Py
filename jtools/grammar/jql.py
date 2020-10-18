from typing import Union, List, Optional


class JQLQueryPart:
    pass


class JQLField(JQLQueryPart):
    def __init__(self):
        self.field = None

    def __repr__(self):
        return f"<Field '{self.field}'>"

    def set_field(self, field: Union[str, int]):
        self.field = field


class JQLSpecial(JQLQueryPart):
    def __init__(self):
        self.special = None
        self.arguments = []

    def __repr__(self):
        return f"<Special '{self.special}' args={self.arguments}>"

    def set_special(self, special: str):
        self.special = special

    def add(self, argument):
        self.arguments.append(argument)


class JQLQuery:
    def __init__(self):
        self.parent = None
        self.parts: List[JQLQueryPart] = []

    def __repr__(self):
        return f"<Query parts={self.parts}>"

    def add(self, part: JQLQueryPart):
        self.parts.append(part)


class JQLRawInput:
    def __init__(self):
        self.text = None

    def set_text(self, text: str):
        self.text = text


class JQLMultiQuery:
    def __init__(self):
        self.queries: List[Union[JQLQuery, JQLRawInput]] = []

    def add(self, query):
        self.queries.append(query)


class JQLValue:
    def __init__(self):
        self.parent = None
        self.value = None

    def __repr__(self):
        return f"<Value: value={repr(self.value)}>"

    def add(self, value):
        self.value = value


class JQLList(JQLValue):
    def __init__(self):
        super().__init__()
        self.value = []

    def __repr__(self):
        return f"<List values={self.value}>"

    def add(self, value):
        self.value.append(value)


class JQLSet(JQLValue):
    def __init__(self):
        super().__init__()
        self.value = set()

    def __repr__(self):
        return f"<Set values={self.value}>"

    def add(self, value):
        self.value.add(value)


class JQLDict(JQLValue):
    MISSING = object()

    def __init__(self):
        super().__init__()
        self.value = {}
        self.key = self.MISSING

    def __repr__(self):
        return f"<Dict values={self.value}>"

    def add(self, value):
        if self.key is self.MISSING:
            self.key = value
        else:
            self.value[self.key] = value
            self.key = self.MISSING


class JQLExpression:
    def __init__(self):
        self.operator: Optional[str] = None
        self.first: Union[JQLExpression, JQLQuery, JQLValue, None] = None
        self.second: Union[JQLExpression, JQLQuery, JQLValue, None] = None

    def __repr__(self):
        if self.first is not None and self.second is not None:
            return f"<Expr: {repr(self.first)} {self.operator} {repr(self.second)}>"
        else:
            return repr(self.first)

    def set_operator(self, op: str):
        self.operator = op

    def add(self, value):
        if self.first is None:
            self.first = value
        else:
            self.second = value


class JQLArgument:
    def __init__(self):
        self.value: Union[JQLValue, JQLExpression, None] = None

    def __repr__(self):
        return f"<Argument: {repr(self.value)}>"

    def add(self, value):
        self.value = value

    def set_value(self, value: JQLValue):
        self.value = value


class JQLKeywordArgument(JQLArgument):
    def __init__(self):
        super().__init__()
        self.name: Optional[str] = None

    def __repr__(self):
        return f"<Keyword Argument: {self.name}={repr(self.value)}>"

    def set_name(self, name: str):
        self.name = name
