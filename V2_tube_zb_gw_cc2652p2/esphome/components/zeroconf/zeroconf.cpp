
#include "esphome/core/log.h"
#include "zeroconf.h"

namespace esphome {
namespace zeroconf {

static const char *TAG = "zeroconf";

void Zeroconf::setup() {
    MDNS.addService(this->service_.name, this->service_.protocol, this->service_.port);

    for(Txt txt : this->txts_){
        MDNS.addServiceTxt(this->service_.name, this->service_.protocol, txt.key, txt.value);
    }
}

void Zeroconf::dump_config(){
    ESP_LOGCONFIG(TAG, "_%s._%s :",  this->service_.name, this->service_.protocol);
    ESP_LOGCONFIG(TAG, "\tport = [%d]", this->service_.port);
    ESP_LOGCONFIG(TAG, "\ttxt = [%s]", txts_to_string().c_str());
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