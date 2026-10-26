#!/usr/bin/env python

# Copyright 2019 Phreaknik
# SPDX-License-Identifier: AGPL-3.0-or-later
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


import os
import sys
import time
import toml
import nicehash
import mwgrinpool


def __updateNicehashOrders():
    nicehash.updateOrders()

def __withdrawFromPool(config):
    payout = mwgrinpool.Pool_Payout()
    payout.username = config['USERNAME']
    payout.password = config['PASSWORD']
    payout.wallet_pass = config['PASSWORD']
    payout.run_local_wallet()


if __name__ == "__main__":
    ## Load user config
    config = toml.load("config.toml")
    LOOP_DELAY_MINUTES = 60 * config['hashmanager']['LOOP_DELAY_MINUTES']

    ## Print banner
    print("################################################################################")
    print("##                                Hash Manager                                ##")
    print("################################################################################")


    while(1):
        ## Open new Nicehash orders
        # Any BTC funds sitting in Nicehash should be committed to hash orders.

        ## Update existing Nicehash orders
        # Existing orders should be updated to track lowest possible price
        try:
            print("Updating existing Nicehash orders...")
            __updateNicehashOrders()
        except Exception as e:
            print("Error: {}".format(str(e)))

        ## Withdraw from mining pool
        try:
            __withdrawFromPool(config['mwgrinpool'])
        except Exception as e:
            print("Error: {}".format(str(e)))

        ## Deposit GRIN to exchange

        ## Exchange funds for BTC

        ## Withdraw BTC to Nicehash

        ## Sleep
        time.sleep(LOOP_DELAY_MINUTES)
