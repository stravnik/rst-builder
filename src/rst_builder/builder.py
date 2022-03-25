import typing as t


if t.TYPE_CHECKING:
    from .maker import RSTMaker


RSTBuilderT = t.TypeVar("RSTBuilderT", bound="RSTBuilder")


class RSTBuilder():
    def __init__(self, maker: "RSTMaker") -> None:
        self._maker = maker
        self._string = ""

    def add_indents(self, __count: int) -> RSTBuilderT:
        self._string += "\n" * __count

        return self

    def add_text(self, text: str) -> RSTBuilderT:
        self._string += text

        return self

    def add_header1(self, text: str) -> RSTBuilderT:
        self._string += self._maker.create_header1(text)

        return self

    def add_header2(self, text: str) -> RSTBuilderT:
        self._string += self._maker.create_header2(text)

        return self

    def add_header3(self, text: str) -> RSTBuilderT:
        self._string += self._maker.create_header3(text)

        return self

    def add_header4(self, text: str) -> RSTBuilderT:
        self._string += self._maker.create_header4(text)

        return self

    def add_header5(self, text: str) -> RSTBuilderT:
        self._string += self._maker.create_header5(text)

        return self

    def add_create_contents(
        self,
        name: t.Optional[str] = None,
        depth_level: t.Optional[int] = None,
    ):
        self._string += self._maker.create_contents(
            name,
            depth_level=depth_level,
        )

        return self

    def get_result(self) -> str:
        return self._string

