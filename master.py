from pymodbus.client.sync import ModbusTcpClient
import logging

logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.INFO)

def run_client():
    client = ModbusTcpClient('127.0.0.1', port=5020)
    client.connect()
    print('连接到 Modbus TCP 从站 127.0.0.1:5020')

    # 读取保持寄存器（地址0-9）
    rr = client.read_holding_registers(0, 10, unit=1)
    if rr.isError():
        print('读取失败:', rr)
    else:
        print('读取到的寄存器值:', rr.registers)

    client.close()

if __name__ == "__main__":
    run_client() 