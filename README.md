# Modbus 主从模拟器

本项目用于帮助理解 Modbus 协议的基本通信流程。包含一个简单的 Modbus TCP 主站（Master）和从站（Slave）示例。

## 依赖
- Python 3.7+
- pymodbus

## 安装依赖
```bash
pip install -r requirements.txt
```

## 运行方式
1. 先启动从站：
   ```bash
   python slave.py
   ```
2. 再启动主站：
   ```bash
   python master.py
   ```

主站会向从站读取寄存器数据，并打印通信内容。 