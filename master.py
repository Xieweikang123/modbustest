from pymodbus.client import ModbusTcpClient
import logging

logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.INFO)

def run_client():
    client = ModbusTcpClient('127.0.0.1', port=5020)
    client.connect()
    print('连接到 Modbus TCP 从站 127.0.0.1:5020')

    # 尝试 unit=0
    rr = client.read_holding_registers(0, 9, unit=0)
    if rr.isError():
        print('读取失败:', rr)
    else:
        print('读取到的寄存器值:', rr.registers)

    client.close()

if __name__ == "__main__":
    run_client() 