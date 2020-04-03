#  SPDX-License-Identifier: Apache-2.0
"""Tesla vehicle GUI settings model."""

from typing import Text


class GuiSettingsModel:
    """Tesla vehicle GUI settings model.

    The model is represented by the GUI settings API results.
    See also: https://tesla-api.timdorr.com/vehicle/state/guisettings
    """

    def __init__(self):
        """Initialize the GUI settings model."""

        self.__gui_24_hour_time = None
        self.__gui_charge_rate_units = None
        self.__gui_distance_units = None
        self.__gui_range_display = None
        self.__gui_temperature_units = None
        self.__show_range_units = None
        self.__timestamp = None

    @property
    def gui_24_hour_time(self) -> bool:
        """Return the gui_24_hour_time."""
        return self.__gui_24_hour_time

    @property
    def gui_charge_rate_units(self) -> Text:
        """Return the gui_charge_rate_units."""
        return self.__gui_charge_rate_units

    @property
    def gui_distance_units(self) -> Text:
        """Return the gui_distance_units."""
        return self.__gui_distance_units

    @property
    def gui_range_display(self) -> Text:
        """Return the gui_range_display."""
        return self.__gui_range_display

    @property
    def gui_temperature_units(self) -> Text:
        """Return the gui_temperature_units."""
        return self.__gui_temperature_units

    @property
    def show_range_units(self) -> bool:
        """Return the show_range_units."""
        return self.__show_range_units

    @property
    def timestamp(self) -> int:
        """Return the timestamp."""
        return self.__timestamp
