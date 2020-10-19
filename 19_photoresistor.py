#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# －－－－湖南创乐博智能科技有限公司－－－－
#  文件名：19_photoresistor.py
#  版本：V2.0
#  author: zhulin
#  说明：光敏电阻传感器实验
#####################################################
import PCF8591 as ADC
import RPi.GPIO as GPIO
import time

makerobo_DO = 17       # 光敏传感器管脚
GPIO.setmode(GPIO.BCM) # 管脚映射，采用BCM编码

# 初始化工作
def makerobo_setup():
	ADC.setup(0x48)      # 设置PCF8591模块地址
	GPIO.setup(makerobo_DO, GPIO.IN) # 光敏传感器，设置为输入模式

# 循环函数
def makerobo_loop():
	makerobo_status = 1 # 状态值
	# 无限循环
	while True:
		print ('Photoresistor Value: ', ADC.read(0)) # 读取AIN0的值，获取光敏模拟量值		
		time.sleep(0.2)                              # 延时200ms

# 程序入口
if __name__ == '__main__':
	try:
		makerobo_setup() # 地址设置
		makerobo_loop()  # 调用无限循环
	except KeyboardInterrupt: 
		pass	
