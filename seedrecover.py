#!/usr/bin/env python3

# seedrecover.py -- Bitcoin mnemonic sentence recovery tool
# Copyright (C) 2014-2017 Christopher Gurnee
#
# This program is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version
# 2 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see http://www.gnu.org/licenses/

# If you find this program helpful, please consider a small
# donation to the developer at the following Bitcoin address:
#
#           bc1q2rfdnec5jmm2eczdgxlymugquqvftmw2kvvruv
#
#                      Thank You!

# PYTHON_ARGCOMPLETE_OK - enables optional bash tab completion

import compatibility_check

from btcrecover import btcrseed
import sys, multiprocessing

if __name__ == "__main__":
    print()
    print("Starting", btcrseed.full_version())

    btcrseed.register_autodetecting_wallets()
    mnemonic_sentence, path_coin = btcrseed.main(sys.argv[1:])

    if mnemonic_sentence:
        if not btcrseed.tk_root:  # if the GUI is not being used
            print()
            print(
                "If this tool helped you to recover funds, please consider donating 1% of what you recovered, in your crypto of choice to:")
            print("BTC: bc1q2rfdnec5jmm2eczdgxlymugquqvftmw2kvvruv ")
            print("BCH: qpz0xfeqpxnlwnevxpvx39nwp5qsedsfpgwn73ce6j ")
            print("LTC: ltc1qy3w2j4rs33l07vscsyedw7vcc642868e6nqnjr ")
            print("ETH: 0xd0D94C2D870d55F487bbE2904EDfEA06fc9a1a6f ")
            print("BNB: 0xd0D94C2D870d55F487bbE2904EDfEA06fc9a1a6f ")
            
            # Selective Donation Addressess depending on path being recovered... (To avoid spamming the dialogue with shitcoins...)
            # TODO: Implement this better with a dictionary mapping in seperate PY file with BTCRecover specific donation addys... (Seperate from YY Channel)
            if path_coin == 28:
                print("VTC: vtc1qxauv20r2ux2vttrjmm9eylshl508q04uju936n ")

            if path_coin == 22:
                print("MONA: mona1q504vpcuyrrgr87l4cjnal74a4qazes2g9qy8mv ")

            if path_coin == 5:
                print("DASH: Xx2umk6tx25uCWp6XeaD5f7CyARkbemsZG ")

            if path_coin == 121:
                print("ZEN: znUihTHfwm5UJS1ywo911mdNEzd9WY9vBP7 ")

            if path_coin == 3:
                print("DOGE: DMQ6uuLAtNoe5y6DCpxk2Hy83nYSPDwb5T ")

            print()
            print("Find me on Twitter @ https://twitter.com/_sameerofficial")
            print()
            print(
                "You may also consider donating to Gurnec, who created and maintained this tool until late 2017 @ bc1q2rfdnec5jmm2eczdgxlymugquqvftmw2kvvruv")
            print()
            print("Seed found:", mnemonic_sentence)  # never dies from printing Unicode

        # print this if there's any chance of Unicode-related display issues
        if any(ord(c) > 126 for c in mnemonic_sentence):
            print("HTML Encoded Seed:", mnemonic_sentence.encode("ascii", "xmlcharrefreplace").decode())

        if btcrseed.tk_root:      # if the GUI is being used
            btcrseed.show_mnemonic_gui(mnemonic_sentence, path_coin)

        retval = 0

    elif mnemonic_sentence is None:
        retval = 1  # An error occurred or Ctrl-C was pressed inside btcrseed.main()

    else:
        retval = 0  # "Seed not found" has already been printed to the console in btcrseed.main()

    # Wait for any remaining child processes to exit cleanly (to avoid error messages from gc)
    for process in multiprocessing.active_children():
        process.join(1.0)

    sys.exit(retval)
