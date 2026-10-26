# NetPulse — ESP32 Network Monitor

NetPulse is a personal electronics and software project to build a network monitoring appliance using an ESP32, an OLED display, and a Python backend.

The goal is to monitor Wi-Fi signal strength and connectivity, collect network performance measurements, and visualise historical results through a dashboard.

## Project Status

**Current stage:** Initial project setup

The repository structure and starter code are in place. Hardware integration and feature development are still pending.

## Planned Features

- **Wi-Fi monitoring:** Measure the ESP32's Wi-Fi signal strength (RSSI) and connection status.
- **Connectivity and latency:** Check reachability and record basic response times.
- **OLED display:** Show live network status and measurements.
- **Python backend:** Receive and process ESP32 measurements.
- **Historical data:** Store measurements in SQLite.
- **Performance dashboard:** Visualise historical network conditions.
- **Internet speed tests:** Run download and upload tests from the connected PC.

Features will be implemented and tested incrementally as development progresses.

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
