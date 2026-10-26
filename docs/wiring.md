# Wiring Notes

Hardware has not been tested yet. Confirm pin labels and board documentation before powering the circuit.

## Planned SSD1306 I²C OLED connections

| OLED pin | ESP32 connection |
|---|---|
| GND | GND |
| VCC | 3V3, if supported by the specific OLED module |
| SDA | GPIO 21 (common default on classic ESP32 boards) |
| SCL | GPIO 22 (common default on classic ESP32 boards) |

Confirm the exact board and OLED module when they arrive. ESP32 GPIO is 3.3 V logic; never drive GPIO with 5 V.
