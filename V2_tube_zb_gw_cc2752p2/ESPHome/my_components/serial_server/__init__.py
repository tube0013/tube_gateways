import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import uart
from esphome.const import CONF_ID, CONF_PORT, CONF_BAUD_RATE

DEPENDENCIES = ['uart']
AUTO_LOAD = ['binary_sensor']

CONF_MULTI_CLIENT = "multi_client"
CONF_MDNS_SERVICE_NAME = "mdns_service_name"
CONF_SERIAL_SERVER_ID = "serial_server_id"

ns = cg.esphome_ns.namespace('serial_server')
SerialServer = ns.class_('SerialServer', cg.Component, uart.UARTDevice)

uart_ns = cg.esphome_ns.namespace("uart")


CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(SerialServer),
    cv.Optional(CONF_PORT, default=8888): cv.port,
    cv.Optional(CONF_MULTI_CLIENT, default=False): cv.boolean,
    cv.GenerateID(CONF_SERIAL_SERVER_ID): cv.use_id(SerialServer),
}).extend(cv.COMPONENT_SCHEMA).extend(uart.UART_DEVICE_SCHEMA)

def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    yield cg.register_component(var, config)

    cg.add(var.set_port(config[CONF_PORT]))
    cg.add(var.set_multi_client(config[CONF_MULTI_CLIENT]))
   
    yield uart.register_uart_device(var, config)
    
   