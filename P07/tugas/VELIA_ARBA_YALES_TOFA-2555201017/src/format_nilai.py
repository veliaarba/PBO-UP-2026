from __future__ import annotations

from functools import singledispatch


@singledispatch
def format_nilai(nilai: object) -> str:
    return str(nilai)


@format_nilai.register(int)
def _(nilai: int) -> str:
    return f"Rp {nilai:,}".replace(",", ".")


@format_nilai.register(float)
def _(nilai: float) -> str:
    return f"{nilai * 100:.2f}%"


@format_nilai.register(list)
def _(nilai: list[object]) -> str:
    return "[" + ", ".join(format_nilai(item) for item in nilai) + "]"

