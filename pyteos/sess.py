#!/usr/bin/python3

"""
Session initiation and storage for session elements.

.. module:: sess
    :platform: Unix, Windows
    :synopsis: Session initiation and storage for session elements.

.. moduleauthor:: Tokenika

"""

import pyteos

def init():
    """
    Initialise a test session.

    - **global variables**::

        eosio: The primary EOSIO account predefined in the genesis file.

        alice, bob, carol: Prefabricated demo accounts.

        key_owner, key_active: Cryptographic keys.

        wallet: The wallet holding keys.
    """
    global eosio
    eosio = pyteos.AccountEosio(is_verbose=False)

    global wallet
    wallet = pyteos.Wallet(is_verbose=False)

    contract_eosio_bios = pyteos.SetContract(
        eosio, "eosio.bios", permission=eosio, is_verbose=False)

    global key_owner
    key_owner = pyteos.CreateKey("key_owner", is_verbose=False)
    global key_active
    key_active = pyteos.CreateKey("key_active", is_verbose=False)

    wallet.import_key(key_owner)
    wallet.import_key(key_active)

    global alice
    alice = pyteos.Account(
        eosio, "alice", key_owner, key_active, is_verbose=False)    
        
    global bob
    bob = pyteos.Account(
        eosio, "bob", key_owner, key_active, is_verbose=False)
            
    global carol
    carol = pyteos.Account(
        eosio, "carol", key_owner, key_active, is_verbose=False)

    print("#  Available test accounts: " + eosio.name + ", "  + alice.name + ", " + carol.name + ", " + bob.name)

