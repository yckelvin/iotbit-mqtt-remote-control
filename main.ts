ESP8266_IoT.MqttEvent("myhome/bedroom/remote-control", ESP8266_IoT.QosList.Qos2, function (message) {
    if (message == "1") {
        OLED.writeStringNewLine("Turn on the light")
    } else if (message == "2") {
        OLED.writeStringNewLine("Turn off the light")
    } else if (message == "3") {
        OLED.writeStringNewLine("Turn on the fan")
    } else if (message == "4") {
        OLED.writeStringNewLine("Turn off the fan")
    }
})
input.onButtonPressed(Button.A, function () {
    ESP8266_IoT.publishMqttMessage(convertToText(randint(1, 4)), "myhome/bedroom/remote-control", ESP8266_IoT.QosList.Qos2)
})
basic.showNumber(0)
ESP8266_IoT.initWIFI(SerialPin.P8, SerialPin.P12, BaudRate.BaudRate115200)
ESP8266_IoT.connectWifi("ssid", "password")
let clientID = randint(0, 99999999)
basic.showNumber(1)
ESP8266_IoT.setMQTT(
ESP8266_IoT.SchemeList.TCP,
convertToText(clientID),
"test",
"test",
""
)
ESP8266_IoT.connectMQTT("192.168.0.32", 1884, false)
basic.showNumber(2)
OLED.init(128, 64)
basic.showNumber(3)
basic.pause(2000)
if (ESP8266_IoT.isMqttBrokerConnected()) {
    basic.showIcon(IconNames.Yes)
}
