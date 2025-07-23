using System;
using System.IO.Ports;
using System.Threading;
using NModbus;
using NModbus.Serial;

class Program
{
    static void Main(string[] args)
    {
        // 配置串口
        var port = new SerialPort("COM11");
        port.BaudRate = 9600;
        port.DataBits = 8;
        port.Parity = Parity.None;
        port.StopBits = StopBits.One;
        port.Open();

        // 创建Modbus工厂
        var factory = new ModbusFactory();
        var slaveNetwork = factory.CreateRtuSlaveNetwork(port);

        // 初始化10个保持寄存器
        ushort[] holdingRegisters = new ushort[10];
        var dataStore = new DefaultSlaveDataStore(
            holdingRegisters: holdingRegisters,
            inputRegisters: null,
            coils: null,
            discreteInputs: null
        );
        var slave = factory.CreateSlave(1, dataStore);
        slaveNetwork.AddSlave(slave);

        Console.WriteLine("Modbus RTU Slave 启动，监听 COM11，波特率9600");
        var slaveThread = new Thread(() =>
        {
            try
            {
                slaveNetwork.ListenAsync(CancellationToken.None).Wait();
            }
            catch (Exception ex)
            {
                Console.WriteLine($"异常: {ex.Message}");
            }
        });
        slaveThread.Start();

        Console.WriteLine("按任意键退出...");
        Console.ReadKey();
        port.Close();
    }
}
