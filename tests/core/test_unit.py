import pytest
from geokube.core.unit import Unit
import cf_units as cf


def test_unit_1():
    u = Unit("not_existing")
    assert u.is_unknown
    assert str(u) == "not_existing"
    assert u._unit == cf.Unit(None)

    u = Unit("m")
    assert str(u) == "m"
    assert not u.is_time_reference()

    u = Unit("hours since 1970-01-01 00:00:00", "gregorian")
    assert u.is_time_reference()