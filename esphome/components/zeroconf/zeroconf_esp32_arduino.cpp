#ifdef USE_ESP32_FRAMEWORK_ARDUINO

#include "zeroconf.h"
#include "esphome/core/log.h"
#include <ESPmDNS.h>

namespace esphome {
namespace zeroconf {

static const char *TAG = "zeroconf";

void Zeroconf::setup() {
    MDNS.addService(this->service_.name, this->service_.protocol, this->service_.port);

    for(Txt txt : this->txts_){
        MDNS.addServiceTxt(this->service_.name, this->service_.protocol, txt.key, txt.value);
    }
}

std::string Zeroconf::txts_to_string(){

    if(this->txts_.size() ==0){
        return "";
    }

    std::string txtstr;

    for(Txt txt : this->txts_){
        txtstr.append("\"").append(txt.key).append("=").append(txt.value).append("\"").append(" ");
    }

    txtstr.pop_back();

    return txtstr;
}

}  // namespace zeroconf
}  // namespace esphome

#endif  // USE_ESP32_FRAMEWORK_ARDUINO