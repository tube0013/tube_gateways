# ESPHome serial server component
ESPHome component that provides a TCP-to-UART service, to directly access serial devices connected to an esp device over a network connection.

```yaml

logger:
  baud_rate: 0 # disable serial logging if you're using the standard TX/RX pins for your serial peripheral

# requires uart to be set up:
uart:
  tx_pin: GPIO1
  rx_pin: GPIO3
  baud_rate: 115200 

serial_server:
  port: 8888 # optional, default is 8888
  multi_client: false # optional, default is false. Set to true to allow multiple simultaneous connections

# optional binary sensor to monitor serial connection:
binary_sensor:
  - platform: serial_server
    name: My serial server
```
