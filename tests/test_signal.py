import pytest
from pydantic import ValidationError

from schemas.signal import Signal

miniumum_viable_signal = {
    "created_date": 0,
    "modified_date": 0,
    "reference_id": "",
    "modified_user": "",
    "source_type": "",
    "source_system": "",
    "owner": "",
    "stage": "ACTIVE",
    "id": "",
}


def create_new_signal_args():
    return dict(miniumum_viable_signal)


def test_mandatory_fields_succeds():
    _ = Signal.model_validate(miniumum_viable_signal)


def test_mandatory_fields_fails():
    with pytest.raises(ValidationError):
        args = create_new_signal_args()
        del args["id"]
        _ = Signal.model_validate(args)


def test_schema_taxonomy_valid():
    args = create_new_signal_args()
    _ = Signal.model_validate(args)


def test_schema_taxonomy_invalid():
    with pytest.raises(ValidationError):
        args = create_new_signal_args()
        args["stage"] = "chocolate"
        _ = Signal.model_validate(args)
