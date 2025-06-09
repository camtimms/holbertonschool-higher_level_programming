#!/usr/bin/python3
from typing import Iterable, SupportsIndex, Any


class VerboseList(list):
    def append(self, object: Any) -> None:
        print(f"Added [{object}] to the list.")
        return super().append(object)

    def extend(self, iterable: Iterable) -> None:
        x = list(iterable)
        print(f"Extended the list with [{len(x)}] items.")
        return super().extend(iterable)

    def remove(self, value: Any) -> None:
        print(f"Removed [{value}] from the list.")
        return super().remove(value)

    def pop(self, index: SupportsIndex = -1) -> Any:
        value = self[index]
        print(f"Popped [{value}] from the list.")
        return super().pop(index)
