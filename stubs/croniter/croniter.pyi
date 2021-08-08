import datetime
from typing import Any, Dict, Iterator, List, Text, Tuple, Type, TypeVar, Union

_RetType = Union[Type[float], Type[datetime.datetime]]
_SelfT = TypeVar("_SelfT", bound=croniter)

class CroniterError(ValueError): ...
class CroniterBadCronError(CroniterError): ...
class CroniterBadDateError(CroniterError): ...
class CroniterNotAlphaError(CroniterError): ...

class croniter(Iterator[Any]):
    MONTHS_IN_YEAR: int
    RANGES: Tuple[Tuple[int, int], ...]
    DAYS: Tuple[int, ...]
    ALPHACONV: Tuple[Dict[str, Any], ...]
    LOWMAP: Tuple[Dict[int, Any], ...]
    bad_length: str
    tzinfo: datetime.tzinfo | None
    cur: float
    expanded: List[List[str]]
    start_time: float
    dst_start_time: float
    nth_weekday_of_month: Dict[str, Any]
    def __init__(
        self, expr_format: Text, start_time: float | datetime.datetime | None = ..., ret_type: _RetType | None = ...
    ) -> None: ...
    # Most return value depend on ret_type, which can be passed in both as a method argument and as
    # a constructor argument.
    def get_next(self, ret_type: _RetType | None = ...) -> Any: ...
    def get_prev(self, ret_type: _RetType | None = ...) -> Any: ...
    def get_current(self, ret_type: _RetType | None = ...) -> Any: ...
    def __iter__(self: _SelfT) -> _SelfT: ...
    def __next__(self, ret_type: _RetType | None = ...) -> Any: ...
    def next(self, ret_type: _RetType | None = ...) -> Any: ...
    def all_next(self, ret_type: _RetType | None = ...) -> Iterator[Any]: ...
    def all_prev(self, ret_type: _RetType | None = ...) -> Iterator[Any]: ...
    def iter(self, ret_type: _RetType | None = ...) -> Iterator[Any]: ...
    def is_leap(self, year: int) -> bool: ...
    @classmethod
    def expand(cls, expr_format: Text) -> Tuple[List[List[str]], Dict[str, Any]]: ...
    @classmethod
    def is_valid(cls, expression: Text) -> bool: ...
