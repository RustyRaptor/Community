# Kamina - The />p/ social network
# Copyright (C) 2018, The Kamina Project
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

"""
cli_commands.py: Class containing the command line commands - ipfs version
"""

from cli.ipfs.basic_commands import BasicCommands
from cli.ipfs.advanced_commands import AdvancedCommands
from kamina.process import KaminaProcess


class CliCommands:
    """Cli commands for managing the community node"""
    def __init__(self, kamina_process: KaminaProcess):
        self.basic_cmd = BasicCommands(kamina_process)
        self.adv_cmd = AdvancedCommands(kamina_process)

    def init(self, install_ipfs: bool) -> None:
        """
        Initialize community node
        :param install_ipfs: Whether to install ipfs or not
        :return: None
        """
        self.basic_cmd.setup_community_node(install_ipfs)

    def daemon(self) -> None:
        """
        Start community daemon
        :return: None
        """
        self.adv_cmd.start_community_daemon()
