from pymodbus.server.async_io import StartTcpServer
from pymodbus.datastore import ModbusSequentialDataBlock, ModbusSlaveContext, ModbusServerContext
import logging

logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.INFO)

def get_context():
    store = ModbusSlaveContext(
        hr=ModbusSequentialDataBlock(0, list(range(10)))
    )
    context = ModbusServerContext(slaves=store, single=True)
    return context

def run_server():
    context = get_context()
    print('Modbus TCP 从站启动，监听 127.0.0.1:5020')
    StartTcpServer(context=context, address=("127.0.0.1", 5020))

if __name__ == "__main__":
    run_server() 