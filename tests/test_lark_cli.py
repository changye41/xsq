import pytest

from feishu_message_archive.lark_cli import _extract_open_id


@pytest.mark.parametrize(
    ("payload", "expected"),
    [
        ({"open_id": "ou_abc"}, "ou_abc"),
        ({"user": {"open_id": "ou_u"}}, "ou_u"),
        ({"data": {"open_id": "ou_d"}}, "ou_d"),
    ],
)
def test_extract_open_id(payload: dict, expected: str) -> None:
    assert _extract_open_id(payload) == expected


def test_extract_open_id_missing() -> None:
    assert _extract_open_id({}) is None
