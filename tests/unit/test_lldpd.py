# Copyright 2016-2021 Canonical Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from unittest.mock import MagicMock, call
from hooks import hooks


def test_install_hooks(mocker):

    mock_fetch = MagicMock()
    hookenv = MagicMock()
    mocker.patch.object(hooks, "fetch", mock_fetch)
    mocker.patch.object(hooks, "hookenv", hookenv)

    hooks.install()

    hookenv.status_set.assert_has_calls(
        [
            call("maintenance", "Installing LLDP daemon"),
            call("maintenance", "LLDP daemon installed"),
        ]
    )
    mock_fetch.apt_update.assert_called_once()
    mock_fetch.apt_install.assert_called_once_with(["lldpd"], fatal=False)
