package main

import (
	"fmt"
	"log"
	"time"

	"github.com/goburrow/serial"
	"github.com/tbrandon/mbserver"
)

func main() {
	server := mbserver.NewServer()

	// 初始化寄存器数据（保持寄存器，地址0-5）
	server.HoldingRegisters[0] = 11
	server.HoldingRegisters[1] = 22
	server.HoldingRegisters[2] = 33
	server.HoldingRegisters[3] = 44
	server.HoldingRegisters[4] = 55
	server.HoldingRegisters[5] = 66

	// 自定义功能码3（读保持寄存器）handler
	server.RegisterFunctionHandler(3, func(s *mbserver.Server, frame mbserver.Framer) ([]byte, *mbserver.Exception) {
		req := frame.GetData()
		fmt.Printf("收到主站读请求：%v\n", req)
		if len(req) >= 4 {
			startAddr := int(req[1]) | int(req[0])<<8
			quantity := int(req[3]) | int(req[2])<<8
			fmt.Printf("收到主站读请求：地址=%d, 数量=%d\n", startAddr, quantity)
		}
		// Let the default handler process the request
		return nil, nil
	})

	for code := 1; code <= 127; code++ {
		server.RegisterFunctionHandler(byte(code), func(s *mbserver.Server, frame mbserver.Framer) ([]byte, *mbserver.Exception) {
			fmt.Printf("收到主站功能码: %d\n", frame.GetFunction())
			return nil, nil // 让 mbserver 用默认逻辑处理
		})
	}

	config := &serial.Config{
		Address:  "\\\\.\\COM11",
		BaudRate: 9600,
		DataBits: 8,
		Parity:   "N",
		StopBits: 1,
	}

	fmt.Println("Modbus RTU 从站启动，监听 COM11，波特率9600")
	err := server.ListenRTU(config)
	if err != nil {
		log.Fatal(err)
	}
	defer server.Close()

	for {
		time.Sleep(time.Second)
	}
}
