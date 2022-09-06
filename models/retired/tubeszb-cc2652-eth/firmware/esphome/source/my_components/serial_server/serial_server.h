/* Copyright (C) 2021 github.com/thegroove
 *
 * Original made by Oxan van Leeuwen:
 * 
 * https://gist.github.com/oxan/4a1a36e12ebed13d31d7ed136b104959
 * 
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <https://www.gnu.org/licenses/>.
 */

#pragma once

#include "esphome/core/component.h"
#include "esphome/components/uart/uart.h"
#include "esphome/components/binary_sensor/binary_sensor.h"

#include <memory>
#include <string>
#include <vector>
#include <Stream.h>

#ifdef ARDUINO_ARCH_ESP8266
#include <ESPAsyncTCP.h>
#else
#include <AsyncTCP.h>
#endif

namespace esphome {
namespace serial_server {

class SerialServer : public uart::UARTDevice, public Component {
public:
    void setup() override;
    void loop() override;
    void dump_config() override;
    void on_shutdown() override;

    float get_setup_priority() const override { return esphome::setup_priority::AFTER_WIFI; }

    void set_port(uint16_t port) { this->port_ = port; }
    void set_multi_client(bool allow_multi_client) { this->allow_multi_client_ = allow_multi_client; }
    void register_connection_sensor(binary_sensor::BinarySensor *connection_sensor) {this->connection_sensor_ = connection_sensor; }

protected:
    void cleanup();
    void serial_read();
    void serial_write();
    void update_connection_sensor();

    struct Client {
        Client(AsyncClient *client, std::vector<uint8_t> &recv_buf);
        ~Client();

        AsyncClient *tcp_client{nullptr};
        std::string identifier{};
        bool disconnected{false};
    };

    AsyncServer server_{0};
    uint16_t port_;
    bool allow_multi_client_;

    std::vector<uint8_t> recv_buf_{};
    std::vector<std::unique_ptr<Client>> clients_{};
    binary_sensor::BinarySensor* connection_sensor_;
};

}  // namespace serial_server
}  // namespace esphome
