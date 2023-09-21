from typing import Any, Callable

SignalCallback = Callable[[Any, Any], None]


__all__ = [
    "post_save",
    "post_init",
    "post_delete",
    "pre_save",
    "pre_save_post_validation",
    "pre_init",
]

class pre_init:
    @staticmethod
    def connect(callback: SignalCallback, sender: object) -> None: ...

class pre_save:
    @staticmethod
    def connect(callback: SignalCallback, sender: object) -> None: ...


class pre_save_post_validation:
    @staticmethod
    def connect(callback: SignalCallback, sender: object) -> None: ...


class post_init:
    @staticmethod
    def connect(callback: SignalCallback, sender: object) -> None: ...


class post_save:
    @staticmethod
    def connect(callback: SignalCallback, sender: object) -> None: ...


class post_delete:
    @staticmethod
    def connect(callback: SignalCallback, sender: object) -> None: ...


