from pymodbus.client import ModbusSerialClient

def run_client():
    client = ModbusSerialClient(
        port='COM10',
        baudrate=9600,
        stopbits=1,
        bytesize=8,
        parity='N',
        timeout=1
    )
    if not client.connect():
        print('串口连接失败，请检查端口号和设备连接')
        return
    print('连接到 Modbus RTU 从站 COM10，波特率9600')

    rr = client.read_holding_registers(address=0, count=1, slave=1)
    print('请求已发送，等待响应...')
    if rr.isError():
        print('读取失败:', rr)
    else:
        print('读取到的寄存器值:', rr.registers)

    client.close()

if __name__ == "__main__":
    run_client() 