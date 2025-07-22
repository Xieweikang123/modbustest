import logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)

from pymodbus.server import StartSerialServer
from pymodbus.datastore import ModbusSequentialDataBlock, ModbusSlaveContext, ModbusServerContext
import serial
import time

class LoggingDataBlock(ModbusSequentialDataBlock):
    def getValues(self, address, count=1):
        print(f"收到主站读请求：地址={address}, 数量={count}")
        return super().getValues(address, count)
    def setValues(self, address, values):
        print(f"收到主站写请求：地址={address}, 值={values}")
        super().setValues(address, values)

def get_context():
    store = ModbusSlaveContext(
        hr=LoggingDataBlock(0, list(range(10)))
    )
    context = ModbusServerContext(slaves=store, single=True)
    return context

def send_test_message():
    try:
        ser = serial.Serial('COM10', 9600, bytesize=8, parity='N', stopbits=1, timeout=1)
        test_data = b'hello from slave\n'  # 你可以改成任意内容或十六进制
        ser.write(test_data)
        print(f"已向 COM10 发送测试消息: {test_data}")
        ser.close()
    except Exception as e:
        print(f"发送测试消息失败: {e}")

def run_server():
    context = get_context()
    print('Modbus RTU 从站启动，监听 COM11，波特率9600')
    StartSerialServer(
        context=context,
        port='COM11',
        baudrate=9600,
        stopbits=1,
        bytesize=8,
        parity='N',
        timeout=1
    )

if __name__ == "__main__":
    send_test_message()
    run_server() 