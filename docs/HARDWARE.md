# Hardware Documentation

## System Architecture Overview

The Multifunctional Highway Smart Street Pole is an integrated system consisting of the following hardware subsystems:

## 1. Dual-Source Power Generation System

### 1.1 Savonius-Type Vertical Axis Wind Turbine (VAWT)

#### Specifications:
- **Type**: Savonius (Drag-based)
- **Configuration**: 2-3 blade helical design
- **Power Output**: 48W under favorable conditions (4.4 m/s wind speed)
- **Efficiency**: 17-34.6% depending on design optimization
- **Optimal Placement Height**: 1.5m above road surface
- **Operational RPM Range**: 150-275 RPM
- **Generator Type**: Permanent Magnet Synchronous Generator (PMSG)

#### Key Features:
- Omnidirectional operation (no yaw mechanism required)
- Low cut-in speed and self-starting capability
- High starting torque
- Captures kinetic energy from vehicular wind turbulence

#### Performance Based on Traffic Density:
| Traffic Condition | RPM | Voltage Output | Avg Speed |
|-------------------|-----|----------------|------------|
| Light Traffic | 150 | 65V | - |
| Medium Traffic | 200 | 75.3V | 65 km/h |
| Heavy Traffic (Expressway) | 275 | 87V | 83 km/h |

### 1.2 Solar Panel Array

#### Specifications:
- **Technology**: High-efficiency monocrystalline panels
- **Total Capacity**: 300W (3 x 100W panels)
- **Panel Dimensions**: 39.0" x 21.3" x 1.2" per panel
- **Panel Weight**: ~13.2 lbs per panel (~40 lbs total)
- **Conversion Efficiency**: >21%
- **Mounting Configuration**: Top-of-pole mount or cylindrical solar wrap
- **Total Array Weight (with mounting)**: 100-150 lbs

#### Daily Energy Generation:
- **Formula**: Power (W) × Peak Sun Hours = Daily Energy (Wh)
- **Conservative Estimate**: 300W × 4 hours = 1,200 Wh/day (1.2 kWh)
- **Optimal Conditions**: 300W × 6 hours = 1,800 Wh/day (1.8 kWh)

## 2. Energy Storage and Management

### 2.1 Battery System

#### Specifications:
- **Chemistry**: LiFePO4 (Lithium Iron Phosphate)
- **System Voltage**: 12.8V
- **Recommended Capacity**: 6.7 kWh minimum
- **Autonomy**: 3 days minimum
- **Lifespan**: 7-10 years
- **Round-trip Efficiency**: 95%
- **Usable Depth of Discharge (DoD)**: 80-90%
- **Operating Temperature Range**: -20°C to 60°C
- **Charging Time**: 4-6 hours (full charge)

#### Advantages over Lead-Acid:
- 3-4x longer lifespan
- Higher efficiency (95% vs 50-80%)
- Greater usable capacity
- Faster charging
- Wider operating temperature range

### 2.2 Hybrid Charge Controller

#### Specifications:
- **Type**: Intelligent MPPT Hybrid Wind-Solar Controller
- **Input 1**: Solar Panel Array (300W)
- **Input 2**: Wind Turbine Generator (50W)
- **MPPT Efficiency**: >98%
- **Features**:
  - Dual independent MPPT tracking
  - Battery overcharge/deep discharge protection
  - Programmable load control (dusk-to-dawn, timer)
  - LCD display/RS232 communication
  - Boost charging function for low-speed wind

## 3. Air Purification Module

### 3.1 Filtration System

#### Components:
1. **Centrifugal Pre-filter** (Mechanically driven)
   - Function: Removes large particulate matter
   - Advantage: Extends HEPA filter life
   - Power Source: Direct mechanical linkage to VAWT

2. **HEPA Filter**
   - Standard: High-Efficiency Particulate Air
   - Efficiency: >99.97% capture of particles ≥0.3 microns
   - Targets: PM2.5, PM10, dust, pollen, black carbon

3. **Activated Carbon Filter**
   - Function: Adsorption of gaseous pollutants
   - Targets: NOx, VOCs, odors

#### Power Requirements:
- **Electrical Equivalent**: 30-50W (for fan motor)
- **Benchmark**: Similar to commercial air purifiers
- **Recommended Configuration**: Electric-powered (from battery bank)

### 3.2 Drivetrain (Optional - High-Risk Design)

**Note**: The dual-output mechanical linkage concept is high-risk. Recommended approach is separate electrical generation and electric-powered purifier.

## 4. AI-Powered Surveillance System

### 4.1 360-Degree Cameras

#### Specifications:
- **Quantity**: 2 cameras (one per traffic direction)
- **Type**: Multi-sensor Panoramic IP Camera
- **Resolution**: 32 Megapixels (total)
- **Field of View**: 180-360 degrees per camera
- **Power Consumption**: 20W per camera (40W total)
- **Environmental Rating**:
  - IP66/IP67 (dust/water resistant)
  - IK10 (vandal-resistant)
- **Operating Temperature**: -34°C to 74°C
- **Housing Material**: Powder-coated aluminum
- **Features**:
  - IR night vision
  - Wide Dynamic Range (WDR)
  - Built-in heater/fan

### 4.2 Edge AI Processor

#### Specifications:
- **Function**: Real-time video analytics
- **Power Consumption**: 2-5W
- **Processing Capabilities**:
  - YOLOv8-based accident detection
  - CNN-based drowsiness detection
  - License plate recognition (LPR)
  - Traffic flow statistics
  - Speed detection

#### AI Algorithms:
1. **Accident Detection**: YOLOv8 object detection model
2. **Drowsiness Detection**: CNN with facial landmark tracking
   - Eye Aspect Ratio (EAR)
   - Mouth Aspect Ratio (MAR)
   - Blink rate analysis

### 4.3 5G IoT Modem/Router

#### Specifications:
- **Technology**: 5G NR (New Radio)
- **Power Consumption**:
  - Idle: 1.5W
  - Active transmission: 15W
  - Average: 5W
- **Latency**: <1ms (URLLC mode)
- **Capabilities**:
  - Enhanced Mobile Broadband (eMBB)
  - Ultra-Reliable Low-Latency Communication (URLLC)
  - Massive Machine-Type Communications (mMTC)
- **Network Architecture**: Network slicing for emergency communications
- **Backup**: Satellite backhaul for remote areas

## 5. LED Street Lighting

### Specifications:
- **Power Rating**: 100W high-efficiency LED luminaire
- **Operational Hours**: 12 hours/night
- **Daily Energy Consumption**: 1,200 Wh
- **Luminous Efficacy**: >130 lm/W
- **Lifespan**: 50,000+ hours
- **Control**: Dusk-to-dawn sensor or programmable timer

## 6. Emergency Call Booth

### Specifications:
- **Housing**: 16-gauge steel, vandal-resistant
- **Power Consumption**:
  - Idle: 0.3W
  - Active call: 1.5W
- **Communication**: GSM/3G/4G cellular module
- **Features**:
  - Single-button activation
  - Always-lit LED faceplate
  - Flashing blue beacon (activated during call)
- **Independence**: Separate from main 5G network

## 7. Drone Integration Module (Future Capability)

### Specifications:
- **System**: Drone-in-a-Box (DiaB)
- **Payload**: First-aid supplies, AED, oxygen canister
- **Navigation**: Autonomous GPS + precision vision landing
- **Trigger**: AI accident detection signal
- **Status**: High regulatory complexity - future implementation

## 8. Structural Specifications

### Pole Requirements:
- **Material**: High-strength steel (ASTM-A-595 Grade A)
- **Base Diameter**: 7 inches
- **Wall Thickness**: No. 11 gauge
- **Design**: Uniform taper, hollow (for cable routing)
- **Foundation**: Deep reinforced concrete footing with anchor bolts
- **Access**: Weatherproof handhole for electronics/battery

### Load Considerations:
- **Static Load**: Dead weight of all components (~200-300 lbs)
- **Dynamic Load**: Vibration from turbine and traffic
- **Aerodynamic Load**: Wind force on solar panels and turbine (80 MPH design wind)
- **Engineering**: Requires FEA (Finite Element Analysis) and wind tunnel testing

## 9. Bill of Materials (BOM) Summary

### Core Components:
| Category | Component | Quantity | Est. Power |
|----------|-----------|----------|------------|
| Generation | 300W Solar Panels | 3 | 300W |
| Generation | Savonius VAWT + PMSG | 1 | 48W |
| Storage | LiFePO4 Battery 6.7kWh | 1 set | - |
| Control | Hybrid MPPT Controller | 1 | <5W |
| Lighting | 100W LED Luminaire | 1 | 100W |
| Surveillance | 32MP Panoramic IP Camera | 2 | 40W |
| Processing | Edge AI Processor | 1 | 5W |
| Comm | 5G IoT Router | 1 | 5W |
| Safety | Emergency Call Booth | 1 | 0.3W |
| Purification | HEPA+Carbon Air Purifier | 1 | 40W |
| Structure | Heavy-duty Steel Pole | 1 | - |
| Mounting | Solar Panel Mounting Rack | 1 | - |

### Total System Power Budget:
- **Daily Consumption**: ~2,887 Wh
- **Daily Generation (Average)**: ~1,500 Wh
- **Status**: Energy deficit - requires optimization

## 10. Installation Considerations

### Site Requirements:
- Highway median location
- Minimum clearance from traffic lanes
- Compliance with NHAI guidelines
- Foundation depth: Based on soil analysis
- Access for maintenance vehicles

### Safety Features:
- Crash-worthy design or protective barriers
- Reflective markings
- Warning signage during installation
- Lightning protection
- Grounding system

## 11. Maintenance Schedule

### Monthly:
- Visual inspection of all components
- Battery voltage check
- Camera cleaning (if accessible)

### Quarterly:
- HEPA filter inspection/replacement
- Activated carbon filter replacement
- Turbine bearing lubrication
- Connection tightness check

### Annual:
- Comprehensive system diagnostic
- Solar panel cleaning and efficiency test
- Structural integrity inspection
- Battery capacity test
- LED luminaire performance check

---

**Document Version**: 1.0  
**Last Updated**: November 2025  
**Author**: Smart Highway Infrastructure Team
