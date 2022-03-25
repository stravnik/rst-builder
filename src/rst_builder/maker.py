import typing as t


class RSTMaker():
    def create_header1(self, text: str) -> str:
        return f"{text}\n" + "#"*len(text)

    def create_header2(self, text: str) -> str:
        return f"{text}\n" + "="*len(text)

    def create_header3(self, text: str) -> str:
        return f"{text}\n" + "-"*len(text)

    def create_header4(self, text: str) -> str:
        return f"{text}\n" + "^"*len(text)

    def create_header5(self, text: str) -> str:
        return f"{text}\n" + "\""*len(text)

    def create_contents(
        self,
        name: t.Optional[str] = None,
        depth_level: t.Optional[int] = None,
    ) -> str:
        result = ".. contents::"

        if name is not None:
            result += name

        if depth_level is not None:
            result += f"\n\t:depth: {depth_level}"

        return result
