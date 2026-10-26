# NetPulse — Network Monitoring Appliance

NetPulse is a learning and portfolio project combining an ESP32-based network monitor with a Python backend and dashboard.

## Planned features
- ESP32 firmware: Wi-Fi connection, signal strength (RSSI), reachability, and basic response-time measurements.
- OLED display: live connection status and measurements.
- Python backend: receive ESP32 measurements.
- SQLite: store history.
- Dashboard: visualise recent and historical network performance.
- PC-based internet speed tests, kept separate from ESP32 measurements.

> Status: initial project scaffold. Hardware features will be implemented and tested as components arrive.

## Architecture
See [`docs/architecture.md`](docs/architecture.md).

## Initial hardware
- ESP32 development board based on ESP32-WROOM-32, with USB-to-serial interface
- 0.96-inch SSD1306 128×64 I²C OLED
- Breadboard, jumper wires, and USB data cable

Exact board and module markings will be verified when the hardware arrives.

## Backend starter
```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python app.py
```
Then open http://127.0.0.1:5000/health.

## Safety and privacy
- Never commit Wi-Fi passwords, API keys, tokens, or private configuration.
- Avoid publishing private network details, device identifiers, or assessment data.
- Only test networks and devices you own or are authorised to monitor.
- ESP32 GPIO uses 3.3 V logic. Never apply 5 V to GPIO pins.

## Roadmap
- [ ] Create and publish the Git repository
- [ ] Confirm Python backend runs
- [ ] Verify ESP32 board and USB serial connection
- [ ] Connect ESP32 to Wi-Fi
- [ ] Display RSSI and connectivity on OLED
- [ ] Send ESP32 readings to Python
- [ ] Store measurements in SQLite
- [ ] Add PC-based speed tests
- [ ] Build dashboard charts
- [ ] Add wiring photos, test evidence, and final documentation

## License
MIT. See [`LICENSE`](LICENSE).
