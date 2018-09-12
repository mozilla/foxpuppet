# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
"""Contains all current install notifications Firefox will display."""

from selenium.webdriver.common.by import By

from foxpuppet.windows.browser.notifications import BaseNotification


class AddOnInstallBlocked(BaseNotification):
    """Add-on install blocked notification."""

    def allow(self):
        """Allow the add-on to be installed."""
        with self.selenium.context(self.selenium.CONTEXT_CHROME):
            self.root.find_anonymous_element_by_attribute("anonid", "button").click()


class AddOnInstallConfirmation(BaseNotification):
    """Add-on install confirmation notification."""

    @property
    def addon_name(self):
        """Provide access to the add-on name.

        Returns:
            str: Add-on name.

        """
        with self.selenium.context(self.selenium.CONTEXT_CHROME):
            el = self.root.find_anonymous_element_by_attribute(
                "class", "popup-notification-description"
            )
            return el.find_element(By.CSS_SELECTOR, "b").text

    def cancel(self):
        """Cancel add-on install."""
        with self.selenium.context(self.selenium.CONTEXT_CHROME):
            self.root.find_anonymous_element_by_attribute(
                "anonid", "secondarybutton"
            ).click()

    def install(self):
        """Confirm add-on install."""
        with self.selenium.context(self.selenium.CONTEXT_CHROME):
            self.root.find_anonymous_element_by_attribute("anonid", "button").click()


class AddOnInstallComplete(BaseNotification):
    """Add-on install complete notification."""


class AddOnInstallRestart(BaseNotification):
    """Add-on install restart notification."""


class AddOnInstallFailed(BaseNotification):
    """Add-on install failed notification."""


class AddOnProgress(BaseNotification):
    """Add-on progress notification."""


NOTIFICATIONS = {
    "addon-install-blocked-notification": AddOnInstallBlocked,
    "addon-install-confirmation-notification": AddOnInstallConfirmation,
    "addon-install-complete-notification": AddOnInstallComplete,
    "addon-install-restart-notification": AddOnInstallRestart,
    "addon-install-failed-notification": AddOnInstallFailed,
    "addon-installed-notification": AddOnInstallComplete,
    "addon-progress-notification": AddOnProgress,
    "addon-webext-permissions-notification": AddOnInstallConfirmation,
}
