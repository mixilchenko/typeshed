import sys
from _typeshed import IterableOrSupportsIntGetItem, Self
from collections.abc import Callable, Iterator
from typing import Any, Generic, SupportsComplex, SupportsFloat, SupportsInt, TypeVar, overload
from typing_extensions import Literal, SupportsIndex, TypeAlias

if sys.version_info >= (3, 9):
    from types import GenericAlias

_T = TypeVar("_T")
_S = TypeVar("_S")
_N = TypeVar("_N", int, float, SupportsFloat, SupportsInt, SupportsIndex, SupportsComplex)
_T_co = TypeVar("_T_co", covariant=True)
_T1 = TypeVar("_T1")
_T2 = TypeVar("_T2")
_T3 = TypeVar("_T3")
_T4 = TypeVar("_T4")
_T5 = TypeVar("_T5")
_T6 = TypeVar("_T6")

_Step: TypeAlias = SupportsFloat | SupportsInt | SupportsIndex | SupportsComplex

_Predicate: TypeAlias = Callable[[_T], object]

# Technically count can take anything that implements a number protocol and has an add method
# but we can't enforce the add method
class count(Iterator[_N], Generic[_N]):
    @overload
    def __new__(cls) -> count[int]: ...
    @overload
    def __new__(cls, start: _N, step: _Step = ...) -> count[_N]: ...
    @overload
    def __new__(cls, *, step: _N) -> count[_N]: ...
    def __next__(self) -> _N: ...
    def __iter__(self: Self) -> Self: ...

class cycle(Iterator[_T], Generic[_T]):
    def __init__(self, __iterable: IterableOrSupportsIntGetItem[_T]) -> None: ...
    def __next__(self) -> _T: ...
    def __iter__(self: Self) -> Self: ...

class repeat(Iterator[_T], Generic[_T]):
    @overload
    def __init__(self, object: _T) -> None: ...
    @overload
    def __init__(self, object: _T, times: int) -> None: ...
    def __next__(self) -> _T: ...
    def __iter__(self: Self) -> Self: ...
    def __length_hint__(self) -> int: ...

class accumulate(Iterator[_T], Generic[_T]):
    if sys.version_info >= (3, 8):
        @overload
        def __init__(self, iterable: IterableOrSupportsIntGetItem[_T], func: None = ..., *, initial: _T | None = ...) -> None: ...
        @overload
        def __init__(
            self, iterable: IterableOrSupportsIntGetItem[_S], func: Callable[[_T, _S], _T], *, initial: _T | None = ...
        ) -> None: ...
    else:
        def __init__(self, iterable: IterableOrSupportsIntGetItem[_T], func: Callable[[_T, _T], _T] | None = ...) -> None: ...

    def __iter__(self: Self) -> Self: ...
    def __next__(self) -> _T: ...

class chain(Iterator[_T], Generic[_T]):
    def __init__(self, *iterables: IterableOrSupportsIntGetItem[_T]) -> None: ...
    def __next__(self) -> _T: ...
    def __iter__(self: Self) -> Self: ...
    @classmethod
    # We use type[Any] and not type[_S] to not lose the type inference from __iterable
    def from_iterable(
        cls: type[Any], __iterable: IterableOrSupportsIntGetItem[IterableOrSupportsIntGetItem[_S]]
    ) -> chain[_S]: ...
    if sys.version_info >= (3, 9):
        def __class_getitem__(cls, __item: Any) -> GenericAlias: ...

class compress(Iterator[_T], Generic[_T]):
    def __init__(self, data: IterableOrSupportsIntGetItem[_T], selectors: IterableOrSupportsIntGetItem[Any]) -> None: ...
    def __iter__(self: Self) -> Self: ...
    def __next__(self) -> _T: ...

class dropwhile(Iterator[_T], Generic[_T]):
    def __init__(self, __predicate: _Predicate[_T], __iterable: IterableOrSupportsIntGetItem[_T]) -> None: ...
    def __iter__(self: Self) -> Self: ...
    def __next__(self) -> _T: ...

class filterfalse(Iterator[_T], Generic[_T]):
    def __init__(self, __predicate: _Predicate[_T] | None, __iterable: IterableOrSupportsIntGetItem[_T]) -> None: ...
    def __iter__(self: Self) -> Self: ...
    def __next__(self) -> _T: ...

class groupby(Iterator[tuple[_T, Iterator[_S]]], Generic[_T, _S]):
    @overload
    def __new__(cls, iterable: IterableOrSupportsIntGetItem[_T1], key: None = ...) -> groupby[_T1, _T1]: ...
    @overload
    def __new__(cls, iterable: IterableOrSupportsIntGetItem[_T1], key: Callable[[_T1], _T2]) -> groupby[_T2, _T1]: ...
    def __iter__(self: Self) -> Self: ...
    def __next__(self) -> tuple[_T, Iterator[_S]]: ...

class islice(Iterator[_T], Generic[_T]):
    @overload
    def __init__(self, __iterable: IterableOrSupportsIntGetItem[_T], __stop: int | None) -> None: ...
    @overload
    def __init__(
        self, __iterable: IterableOrSupportsIntGetItem[_T], __start: int | None, __stop: int | None, __step: int | None = ...
    ) -> None: ...
    def __iter__(self: Self) -> Self: ...
    def __next__(self) -> _T: ...

class starmap(Iterator[_T], Generic[_T]):
    def __init__(
        self, __function: Callable[..., _T], __iterable: IterableOrSupportsIntGetItem[IterableOrSupportsIntGetItem[Any]]
    ) -> None: ...
    def __iter__(self: Self) -> Self: ...
    def __next__(self) -> _T: ...

class takewhile(Iterator[_T], Generic[_T]):
    def __init__(self, __predicate: _Predicate[_T], __iterable: IterableOrSupportsIntGetItem[_T]) -> None: ...
    def __iter__(self: Self) -> Self: ...
    def __next__(self) -> _T: ...

def tee(__iterable: IterableOrSupportsIntGetItem[_T], __n: int = ...) -> tuple[Iterator[_T], ...]: ...

class zip_longest(Iterator[_T_co], Generic[_T_co]):
    # one iterable (fillvalue doesn't matter)
    @overload
    def __new__(cls, __iter1: IterableOrSupportsIntGetItem[_T1], *, fillvalue: object = ...) -> zip_longest[tuple[_T1]]: ...
    # two iterables
    @overload
    # In the overloads without fillvalue, all of the tuple members could theoretically be None,
    # but we return Any instead to avoid false positives for code where we know one of the iterables
    # is longer.
    def __new__(
        cls, __iter1: IterableOrSupportsIntGetItem[_T1], __iter2: IterableOrSupportsIntGetItem[_T2]
    ) -> zip_longest[tuple[_T1 | Any, _T2 | Any]]: ...
    @overload
    def __new__(
        cls, __iter1: IterableOrSupportsIntGetItem[_T1], __iter2: IterableOrSupportsIntGetItem[_T2], *, fillvalue: _T
    ) -> zip_longest[tuple[_T1 | _T, _T2 | _T]]: ...
    # three iterables
    @overload
    def __new__(
        cls,
        __iter1: IterableOrSupportsIntGetItem[_T1],
        __iter2: IterableOrSupportsIntGetItem[_T2],
        __iter3: IterableOrSupportsIntGetItem[_T3],
    ) -> zip_longest[tuple[_T1 | Any, _T2 | Any, _T3 | Any]]: ...
    @overload
    def __new__(
        cls,
        __iter1: IterableOrSupportsIntGetItem[_T1],
        __iter2: IterableOrSupportsIntGetItem[_T2],
        __iter3: IterableOrSupportsIntGetItem[_T3],
        *,
        fillvalue: _T,
    ) -> zip_longest[tuple[_T1 | _T, _T2 | _T, _T3 | _T]]: ...
    # four iterables
    @overload
    def __new__(
        cls,
        __iter1: IterableOrSupportsIntGetItem[_T1],
        __iter2: IterableOrSupportsIntGetItem[_T2],
        __iter3: IterableOrSupportsIntGetItem[_T3],
        __iter4: IterableOrSupportsIntGetItem[_T4],
    ) -> zip_longest[tuple[_T1 | Any, _T2 | Any, _T3 | Any, _T4 | Any]]: ...
    @overload
    def __new__(
        cls,
        __iter1: IterableOrSupportsIntGetItem[_T1],
        __iter2: IterableOrSupportsIntGetItem[_T2],
        __iter3: IterableOrSupportsIntGetItem[_T3],
        __iter4: IterableOrSupportsIntGetItem[_T4],
        *,
        fillvalue: _T,
    ) -> zip_longest[tuple[_T1 | _T, _T2 | _T, _T3 | _T, _T4 | _T]]: ...
    # five iterables
    @overload
    def __new__(
        cls,
        __iter1: IterableOrSupportsIntGetItem[_T1],
        __iter2: IterableOrSupportsIntGetItem[_T2],
        __iter3: IterableOrSupportsIntGetItem[_T3],
        __iter4: IterableOrSupportsIntGetItem[_T4],
        __iter5: IterableOrSupportsIntGetItem[_T5],
    ) -> zip_longest[tuple[_T1 | Any, _T2 | Any, _T3 | Any, _T4 | Any, _T5 | Any]]: ...
    @overload
    def __new__(
        cls,
        __iter1: IterableOrSupportsIntGetItem[_T1],
        __iter2: IterableOrSupportsIntGetItem[_T2],
        __iter3: IterableOrSupportsIntGetItem[_T3],
        __iter4: IterableOrSupportsIntGetItem[_T4],
        __iter5: IterableOrSupportsIntGetItem[_T5],
        *,
        fillvalue: _T,
    ) -> zip_longest[tuple[_T1 | _T, _T2 | _T, _T3 | _T, _T4 | _T, _T5 | _T]]: ...
    # six or more iterables
    @overload
    def __new__(
        cls,
        __iter1: IterableOrSupportsIntGetItem[_T],
        __iter2: IterableOrSupportsIntGetItem[_T],
        __iter3: IterableOrSupportsIntGetItem[_T],
        __iter4: IterableOrSupportsIntGetItem[_T],
        __iter5: IterableOrSupportsIntGetItem[_T],
        __iter6: IterableOrSupportsIntGetItem[_T],
        *iterables: IterableOrSupportsIntGetItem[_T],
    ) -> zip_longest[tuple[_T | Any, ...]]: ...
    @overload
    def __new__(
        cls,
        __iter1: IterableOrSupportsIntGetItem[_T],
        __iter2: IterableOrSupportsIntGetItem[_T],
        __iter3: IterableOrSupportsIntGetItem[_T],
        __iter4: IterableOrSupportsIntGetItem[_T],
        __iter5: IterableOrSupportsIntGetItem[_T],
        __iter6: IterableOrSupportsIntGetItem[_T],
        *iterables: IterableOrSupportsIntGetItem[_T],
        fillvalue: _T,
    ) -> zip_longest[tuple[_T, ...]]: ...
    def __iter__(self: Self) -> Self: ...
    def __next__(self) -> _T_co: ...

class product(Iterator[_T_co], Generic[_T_co]):
    @overload
    def __new__(cls, __iter1: IterableOrSupportsIntGetItem[_T1]) -> product[tuple[_T1]]: ...
    @overload
    def __new__(
        cls, __iter1: IterableOrSupportsIntGetItem[_T1], __iter2: IterableOrSupportsIntGetItem[_T2]
    ) -> product[tuple[_T1, _T2]]: ...
    @overload
    def __new__(
        cls,
        __iter1: IterableOrSupportsIntGetItem[_T1],
        __iter2: IterableOrSupportsIntGetItem[_T2],
        __iter3: IterableOrSupportsIntGetItem[_T3],
    ) -> product[tuple[_T1, _T2, _T3]]: ...
    @overload
    def __new__(
        cls,
        __iter1: IterableOrSupportsIntGetItem[_T1],
        __iter2: IterableOrSupportsIntGetItem[_T2],
        __iter3: IterableOrSupportsIntGetItem[_T3],
        __iter4: IterableOrSupportsIntGetItem[_T4],
    ) -> product[tuple[_T1, _T2, _T3, _T4]]: ...
    @overload
    def __new__(
        cls,
        __iter1: IterableOrSupportsIntGetItem[_T1],
        __iter2: IterableOrSupportsIntGetItem[_T2],
        __iter3: IterableOrSupportsIntGetItem[_T3],
        __iter4: IterableOrSupportsIntGetItem[_T4],
        __iter5: IterableOrSupportsIntGetItem[_T5],
    ) -> product[tuple[_T1, _T2, _T3, _T4, _T5]]: ...
    @overload
    def __new__(
        cls,
        __iter1: IterableOrSupportsIntGetItem[_T1],
        __iter2: IterableOrSupportsIntGetItem[_T2],
        __iter3: IterableOrSupportsIntGetItem[_T3],
        __iter4: IterableOrSupportsIntGetItem[_T4],
        __iter5: IterableOrSupportsIntGetItem[_T5],
        __iter6: IterableOrSupportsIntGetItem[_T6],
    ) -> product[tuple[_T1, _T2, _T3, _T4, _T5, _T6]]: ...
    @overload
    def __new__(
        cls,
        __iter1: IterableOrSupportsIntGetItem[Any],
        __iter2: IterableOrSupportsIntGetItem[Any],
        __iter3: IterableOrSupportsIntGetItem[Any],
        __iter4: IterableOrSupportsIntGetItem[Any],
        __iter5: IterableOrSupportsIntGetItem[Any],
        __iter6: IterableOrSupportsIntGetItem[Any],
        __iter7: IterableOrSupportsIntGetItem[Any],
        *iterables: IterableOrSupportsIntGetItem[Any],
    ) -> product[tuple[Any, ...]]: ...
    @overload
    def __new__(cls, *iterables: IterableOrSupportsIntGetItem[_T1], repeat: int) -> product[tuple[_T1, ...]]: ...
    @overload
    def __new__(cls, *iterables: IterableOrSupportsIntGetItem[Any], repeat: int = ...) -> product[tuple[Any, ...]]: ...
    def __iter__(self: Self) -> Self: ...
    def __next__(self) -> _T_co: ...

class permutations(Iterator[tuple[_T, ...]], Generic[_T]):
    def __init__(self, iterable: IterableOrSupportsIntGetItem[_T], r: int | None = ...) -> None: ...
    def __iter__(self: Self) -> Self: ...
    def __next__(self) -> tuple[_T, ...]: ...

class combinations(Iterator[_T_co], Generic[_T_co]):
    @overload
    def __new__(cls, iterable: IterableOrSupportsIntGetItem[_T], r: Literal[2]) -> combinations[tuple[_T, _T]]: ...
    @overload
    def __new__(cls, iterable: IterableOrSupportsIntGetItem[_T], r: Literal[3]) -> combinations[tuple[_T, _T, _T]]: ...
    @overload
    def __new__(cls, iterable: IterableOrSupportsIntGetItem[_T], r: Literal[4]) -> combinations[tuple[_T, _T, _T, _T]]: ...
    @overload
    def __new__(cls, iterable: IterableOrSupportsIntGetItem[_T], r: Literal[5]) -> combinations[tuple[_T, _T, _T, _T, _T]]: ...
    @overload
    def __new__(cls, iterable: IterableOrSupportsIntGetItem[_T], r: int) -> combinations[tuple[_T, ...]]: ...
    def __iter__(self: Self) -> Self: ...
    def __next__(self) -> _T_co: ...

class combinations_with_replacement(Iterator[tuple[_T, ...]], Generic[_T]):
    def __init__(self, iterable: IterableOrSupportsIntGetItem[_T], r: int) -> None: ...
    def __iter__(self: Self) -> Self: ...
    def __next__(self) -> tuple[_T, ...]: ...

if sys.version_info >= (3, 10):
    class pairwise(Iterator[_T_co], Generic[_T_co]):
        def __new__(cls, __iterable: IterableOrSupportsIntGetItem[_T]) -> pairwise[tuple[_T, _T]]: ...
        def __iter__(self: Self) -> Self: ...
        def __next__(self) -> _T_co: ...
