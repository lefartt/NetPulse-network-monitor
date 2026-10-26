# NetPulse Architecture

## Planned data flow
1. ESP32 joins the configured 2.4 GHz Wi-Fi network.
2. Firmware measures Wi-Fi RSSI and performs a basic reachability/latency check.
3. ESP32 sends measurements to the Python service over the local network.
4. Python validates and stores incoming measurements in SQLite.
5. The PC runs internet speed tests and records those results separately.
6. The dashboard displays current status and historical measurements.

## Design boundaries
- The ESP32 provides lightweight, continuous measurements.
- The PC handles heavier speed tests, data storage, and visualisation.
- Router-specific APIs and per-device traffic inspection are not assumed.
- Basic ESP32 readings should continue when the PC backend is offline.

## Security notes
- Do not hard-code Wi-Fi credentials in tracked source files.
- Bind the development backend to localhost until LAN access is intentionally configured.
- Validate incoming data before storing it.
