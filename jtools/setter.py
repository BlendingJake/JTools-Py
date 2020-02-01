__all__ = ["Setter"]


class Setter:
    def __init__(self, field: str, convert_ints: bool = True):
        self.field = field
        self.convert_ints = convert_ints
        self.parts = self._process_field(field)

    def _process_field(self, field: str):
        parts = []
        for p in field.split("."):
            if self.convert_ints:
                try:
                    i = int(p)
                    parts.append(i)
                except ValueError:
                    parts.append(p)
            else:
                parts.append(p)

        return parts

    def set(self, item, value):
        current = item

        if len(self.parts) >= 2:
            for p in self.parts[:-1]:
                current = item[p]

        current[self.parts[-1]] = value
