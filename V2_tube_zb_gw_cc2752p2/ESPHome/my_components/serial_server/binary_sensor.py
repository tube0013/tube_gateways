import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import binary_sensor
from esphome.const import CONF_ID, CONF_DEVICE_CLASS, DEVICE_CLASS_CONNECTIVITY
from . import SerialServer, CONF_SERIAL_SERVER_ID

DEPENDENCIES = ['serial_server']

ns = cg.esphome_ns.namespace('binary_sensor')
class_ = ns.class_('BinarySensor', binary_sensor.BinarySensor, cg.Nameable)

CONFIG_SCHEMA = binary_sensor.BINARY_SENSOR_SCHEMA.extend({
    cv.GenerateID(): cv.declare_id(class_),
    cv.GenerateID(CONF_SERIAL_SERVER_ID): cv.use_id(SerialServer),
    cv.Optional(CONF_DEVICE_CLASS, default=DEVICE_CLASS_CONNECTIVITY): binary_sensor.device_class,
}).extend(cv.COMPONENT_SCHEMA)

def to_code(config):
    paren = yield cg.get_variable(config[CONF_SERIAL_SERVER_ID])
    var = cg.new_Pvariable(config[CONF_ID])
    
    yield binary_sensor.register_binary_sensor(var, config)
    
    cg.add(paren.register_connection_sensor(var))