"""Test Home Assistant parking sensor."""

import pytest

from teslajsonpy.ha.lock import DoorLock


def test_is_locked():
    """Test is_locked()."""

    _lock = DoorLock()

    assert not _lock.is_locked


def test_changed_by():
    """Test changed_by()."""

    _lock = DoorLock()

    assert _lock.changed_by is None


def test_assumed_state():
    """Test assumed_state()."""

    _lock = DoorLock()

    assert not _lock.assumed_state


def test_available():
    """Test available()."""

    _lock = DoorLock()

    assert _lock.available


def test_device_class():
    """Test device_class()."""

    _lock = DoorLock()

    assert _lock.device_class is None


def test_device_state_attributes():
    """Test device_state_attributes()."""

    _lock = DoorLock()

    assert _lock.device_state_attributes is None


def test_entity_picture():
    """Test entity_picture()."""

    _lock = DoorLock()

    assert _lock.entity_picture is None


def test_name():
    """Test name()."""

    _lock = DoorLock()

    assert _lock.name is None


def test_should_poll():
    """Test should_poll()."""

    _lock = DoorLock()

    assert _lock.should_poll


def test_unique_id():
    """Test unique_id()."""

    _lock = DoorLock()

    assert _lock.unique_id is None


def test_force_update():
    """Test force_update()."""

    _lock = DoorLock()

    assert not _lock.force_update


def test_icon():
    """Test icon()."""

    _lock = DoorLock()

    assert _lock.icon is None


def test_entity_registry_enabled_default():
    """Test entity_registry_enabled_default()."""

    _lock = DoorLock()

    assert _lock.entity_registry_enabled_default


@pytest.mark.asyncio
async def test_update():
    """Test update()."""

    _lock = DoorLock()

    with pytest.raises(NotImplementedError):
        await _lock.update()
