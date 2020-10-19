from datetime import time
import Adafruit_DHT
import json
from GuangMinMysql import Light
import YZFtempMysql
from YZFtempMysql import Temp
import time
import photoresistor
import GuangMinMysql


def WSDReader(gpio):
    """
    输入gpio参数，返回温湿度值
    """

    sensor = Adafruit_DHT.DHT11

    humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)

    if humidity is not None and temperature is not None:
        result = 'Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(
            temperature, humidity)
        return {'result': result,
                'temperature': temperature,
                'humidity': humidity}
    else:
        print('Failed to get reading. Try again!')
        return 0


if __name__ == '__main__':
    for i in range(0, 1000):
        try:
            # 光敏部分
            photoresistor.makerobo_setup()  # 地址设置
            lightResult = photoresistor.makerobo_loop()  # 调用
            lightinto = Light()
            lightinto.lighting = float(lightResult)

            # 温湿度部分
            result = WSDReader(4)
            temp = Temp()
            temp.temperature = float(result['temperature'])
            temp.Humidity = float(result['humidity'])

            # 插入部分
            GuangMinMysql.Lighting().insert(light1=lightinto)
            YZFtempMysql.TEMPerature().insert(temp1=temp)
            print(lightinto)
            print(float(result['temperature']))
            print(float(result['humidity']))
            print(json.dumps(result))
            print(result['result'])
            time.sleep(2)
        except KeyboardInterrupt:
            pass
