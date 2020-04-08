import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX='dcececdc'.decode('hex') 
P2P_PORT=9069
ADDRESS_VERSION=63
RPC_PORT=9370
# RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue('virclesaddress' in (yield bitcoind.rpc_help()) and not (yield bitcoind.rpc_getinfo())['testnet']))
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            (yield helper.check_genesis_block(bitcoind, '0000066e6810ff0642cc34fe5fc3c66c3f39c9a0c713c079df427524994fc06a')) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        ))
SUBSIDY_FUNC = lambda height: 66.6*100000000 >> (height + 1)//525600
POW_FUNC=lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data))
# POW_FUNC = data.hash256
BLOCK_PERIOD=60
SYMBOL='VCL'
CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Vircles') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Vircles/') if platform.system() == 'Darwin' else os.path.expanduser('~/.vircles'), 'vircles.conf')
BLOCK_EXPLORER_URL_PREFIX='http://sys.coinzone.info/chain/SysCoin/block/'
ADDRESS_EXPLORER_URL_PREFIX='http://sys.coinzone.info/chain/SysCoin/address/'
TX_EXPLORER_URL_PREFIX='http://sys.coinzone.info/chain/SysCoin/tx/'
SANE_TARGET_RANGE=(2**256//1000000000 - 1, 2**256//1000 - 1)
DUMB_SCRYPT_DIFF=2**16
DUST_THRESHOLD=0.03e8