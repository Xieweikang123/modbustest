from pymodbus.server.sync import StartTcpServer
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock, ModbusSlaveContext, ModbusServerContext
import logging

logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.INFO)

def run_server():
    # 初始化数据块，假设有10个寄存器，初始值为0-9
    store = ModbusSlaveContext(
        hr=ModbusSequentialDataBlock(0, list(range(10)))
    )
    context = ModbusServerContext(slaves=store, single=True)

    identity = ModbusDeviceIdentification()
    identity.VendorName = 'pymodbus'
    identity.ProductCode = 'PM'
    identity.VendorUrl = 'http://github.com/riptideio/pymodbus/'
    identity.ProductName = 'pymodbus Server'
    identity.ModelName = 'pymodbus Server'
    identity.MajorMinorRevision = '1.0'

    print('Modbus TCP 从站启动，监听 127.0.0.1:5020')
    StartTcpServer(context, identity=identity, address=("127.0.0.1", 5020))

if __name__ == "__main__":
    run_server() 