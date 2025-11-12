Project Description: Multifunctional Smart Street Lamp with Integrated Renewable Energy Harvesting and Emergency Response System
1. Introduction
Modern urbanization and infrastructure development demand innovative solutions for sustainable energy, public safety, and environmental improvement. Roads and highways are critical arteries of transportation where safety, energy efficiency, and environmental quality are vital. This project proposes a multifunctional smart street lamp system designed to integrate renewable energy harvesting, air purification, real-time monitoring, emergency detection, and response functionalities in a single infrastructure unit placed along highways.

2. Objective
The primary objective is to develop and deploy a multifunctional street lamp that:

Generates clean, continuous energy using photovoltaic solar panels, a Savonius vertical-axis wind turbine (VAWT), and vehicle-induced dynamo energy harvesting.

Purifies highway air using a wind turbine-driven air purifier mounted on the pole.

Provides intelligent lighting with energy storage for night-time operations.

Monitors traffic and highway conditions via 360° Wi-Fi enabled 5G cameras for accident detection and speed monitoring.

Sends real-time alerts automatically to nearby police stations, hospitals, and ambulance services to accelerate emergency response.

Dispatches drones equipped with oxygen and medicines to accident sites for faster rescue.

Incorporates an emergency calling booth powered by harvested energy.

Alerts distracted or sleepy drivers at night using smart speed detection cameras.

3. System Architecture and Components
3.1 Structural Design and Dimensions
Pole Height: 8.5 meters above ground level to optimize lighting and camera coverage.

Foundation Depth: 1.5 meters for stability near highways.

Savonius Wind Turbine: Mounted at the center of the pole for omnidirectional wind capture.

Solar Panels: Fixed at the top for maximal solar irradiance exposure.

Dynamo Mechanism: Integrated at the pole base connected to road vibrations and vehicle movement to harness kinetic energy.

Air Purifier: Attached via a shaft to the turbine blades on top to utilize turbine rotation for air filtration.

Cameras: Two 360° Wi-Fi 5G cameras on the top pole for comprehensive monitoring.

3.2 Energy Harvesting and Storage
Sources: Photovoltaic solar panel (~200W nominal), Savonius wind turbine (~50W average output), vehicle-induced dynamo (~30W).

Battery Bank: 48V, 400Ah deep-cycle battery storing approximately 19.2 kWh to enable night-time operation and emergency power.

Power Management: Smart charge controller managing input sources and load balancing for street lamps, cameras, air purifier, emergency booth, and communication equipment.

3.3 Monitoring and Safety Systems
Speed Detection Cameras: Using advanced image processing for driver behavior and speed recognition.

Accident and Emergency Detection: AI-based real-time image/video analytics detecting crashes or unusual incidents.

Alert Mechanism: Automatic push notifications to police, hospitals, ambulances, and an emergency drone control system.

Drone Dispatch: Upon accident detection, an oxygen and medicine drone is deployed to the precise location for rapid medical aid.

3.4 Environmental and Social Impact
Air Quality Improvement: The air purifier reduces pollutants in highway air corridors, improving local air quality by filtering dust, smoke, and vehicle emissions.

Energy Sustainability: Renewable energy integration reduces carbon footprint and dependence on grid electricity.

Public Safety Enhancement: Reduced accident response time decreases mortality and morbidity associated with highway accidents.

Connectivity: Enhanced public safety communication with live feeds to local authorities and emergency responders.

4. Expected Outcomes and Benefits
Continuous power supply from renewable sources enabling autonomous street lighting.

Improved air quality along highways through continuous air filtration powered by turbine rotation.

Real-time traffic surveillance and driver safety monitoring.

Faster emergency response times (target <3 minutes) leveraging automated alerts and drone delivery.

A cost-effective solution promoting green energy, smart city infrastructure, and intelligent transport systems.

5. Innovation and Novelty
This project introduces the first-ever integration of:

Hybrid Renewable Energy Harvesting: Combining solar, vehicle-motion dynamo, and Savonius wind turbine on one street pole.

Wind-Powered Air Purification: Utilizing mechanical shaft power directly from the turbine to drive an air purifier.

AI-Enabled Emergency and Driver Alert System: Using smart cameras and automatic alert dispatch.

Drone-Assisted Emergency Aid: Real-time drone deployment for medical response.

6. Conclusion
The proposed multifunctional smart street lamp system demonstrates an innovative approach to highway infrastructure, combining energy sustainability, intelligent safety monitoring, and environmental health. Its integrated design can significantly reduce accident fatalities, improve air quality, and promote renewable energy usage in public infrastructure.

#!/usr/bin/env python3
"""
Accident Detection System using YOLOv8
Part of Multifunctional Highway Smart Street Pole System

This module uses YOLOv8 for real-time traffic accident detection from 360° camera feeds.
When an accident is detected, it triggers the emergency alert system.

Author: Smart Chinnodu
Institution: Dadi Institute of Engineering and Technology
"""

import cv2
import numpy as np
try:
    from ultralytics import YOLO
except ImportError:
    print("[WARNING] YOLOv8 not installed. Install with: pip install ultralytics")
import datetime
import json
from pathlib import Path
import argparse

class AccidentDetector:
    """
    Real-time accident detection using YOLOv8 model.
    
    Attributes:
        model: YOLOv8 model for object detection
        confidence_threshold: Minimum confidence for accident detection
        alert_callback: Function to call when accident is detected
    """
    
    def __init__(self, model_path='yolov8n.pt', confidence=0.5):
        """
        Initialize the accident detector.
        
        Args:
            model_path (str): Path to YOLOv8 model weights
            confidence (float): Confidence threshold for detection
        """
        print(f"[INFO] Loading YOLOv8 model from {model_path}...")
        self.model = YOLO(model_path)
        self.confidence_threshold = confidence
        self.accident_log = []
        
        # Define accident-related classes
        self.accident_indicators = {
            'overturned_vehicle': ['car', 'truck', 'bus'],
            'debris': ['person', 'bicycle', 'motorcycle'],
            'unusual_angles': True
        }
        print("[INFO] Accident detector initialized successfully")
        
    def detect_accident(self, frame):
        """
        Analyze frame for accident indicators.
        
        Args:
            frame: Input video frame (numpy array)
            
        Returns:
            tuple: (is_accident, results, annotated_frame, accident_score)
        """
        # Run YOLOv8 inference
        results = self.model(frame, conf=self.confidence_threshold, verbose=False)
        
        # Initialize accident detection flags
        is_accident = False
        accident_score = 0.0
        
        # Analyze detections
        for result in results:
            boxes = result.boxes
            
            if len(boxes) == 0:
                continue
                
            # Check for multiple vehicles in abnormal positions
            vehicle_count = 0
            abnormal_positions = 0
            person_count = 0
            
            for box in boxes:
                cls = int(box.cls[0])
                conf = float(box.conf[0])
                
                class_name = self.model.names[cls]
                
                # Count vehicles
                if class_name in ['car', 'truck', 'bus', 'motorcycle']:
                    vehicle_count += 1
                    
                    # Check for abnormal bounding box aspect ratios
                    x1, y1, x2, y2 = box.xyxy[0].tolist()
                    width = x2 - x1
                    height = y2 - y1
                    aspect_ratio = width / height if height > 0 else 0
                    
                    # Overturned vehicles have unusual aspect ratios
                    if aspect_ratio < 0.5 or aspect_ratio > 3.0:
                        abnormal_positions += 1
                        accident_score += 0.3
                
                # Detect debris or people on highway (danger indicator)
                if class_name == 'person':
                    person_count += 1
                    accident_score += 0.4
            
            # Multiple vehicles close together (collision indicator)
            if vehicle_count >= 2:
                accident_score += 0.3
            
            # Abnormal vehicle orientations
            if abnormal_positions > 0:
                accident_score += 0.4
            
            # People on highway
            if person_count >= 1:
                accident_score += 0.2
            
            # Threshold for accident detection (adjust based on testing)
            if accident_score >= 0.7:
                is_accident = True
        
        # Annotate frame with detection boxes
        annotated_frame = results[0].plot() if len(results) > 0 else frame.copy()
        
        return is_accident, results, annotated_frame, accident_score

    def process_video(self, video_source, output_path=None, display=True):
        """
        Process video stream for accident detection.
        
        Args:
            video_source: Video file path or camera index (0, 1, etc.)
            output_path: Optional path to save output video
            display: Whether to display video feed
        """
        # Open video source
        cap = cv2.VideoCapture(video_source)
        
        if not cap.isOpened():
            print(f"[ERROR] Could not open video source: {video_source}")
            return
        
        # Get video properties
        fps = int(cap.get(cv2.CAP_PROP_FPS)) or 30
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        
        print(f"[INFO] Video Properties: {width}x{height} @ {fps}FPS")
        
        # Setup video writer if output path provided
        writer = None
        if output_path:
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            writer = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
            print(f"[INFO] Output will be saved to: {output_path}")
        
        frame_count = 0
        accident_detected_frames = 0
        
        try:
            while True:
                ret, frame = cap.read()
                if not ret:
                    print("[INFO] End of video stream")
                    break
                
                frame_count += 1
                
                # Detect accidents every frame (or skip frames for performance)
                is_accident, detections, annotated_frame, score = self.detect_accident(frame)
                
                # Add status overlay
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                status_text = "⚠ ACCIDENT DETECTED!" if is_accident else "✓ Monitoring..."
                status_color = (0, 0, 255) if is_accident else (0, 255, 0)  # BGR format
                
                # Draw semi-transparent overlay for status
                overlay = annotated_frame.copy()
                cv2.rectangle(overlay, (0, 0), (width, 100), (0, 0, 0), -1)
                cv2.addWeighted(overlay, 0.3, annotated_frame, 0.7, 0, annotated_frame)
                
                # Add text information
                cv2.putText(annotated_frame, status_text, (10, 35),
                           cv2.FONT_HERSHEY_SIMPLEX, 1.2, status_color, 3)
                cv2.putText(annotated_frame, f"Confidence: {score:.2f}", (10, 70),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
                cv2.putText(annotated_frame, f"Frame: {frame_count}", (width-200, 30),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
                cv2.putText(annotated_frame, timestamp, (10, height - 15),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
                
                # Log accident
                if is_accident:
                    accident_detected_frames += 1
                    self.log_accident(frame_count, timestamp, score, detections)
                    print(f"[ALERT] Accident detected at frame {frame_count} | Score: {score:.2f}")
                    # Here you would trigger the emergency alert system
                    # self.trigger_emergency_alert(frame, timestamp, score)
                
                # Write frame to output video
                if writer:
                    writer.write(annotated_frame)
                
                # Display frame
                if display:
                    cv2.imshow('Highway Accident Detection System - Smart Street Pole', annotated_frame)
                    key = cv2.waitKey(1) & 0xFF
                    if key == ord('q'):
                        print("[INFO] User requested quit")
                        break
                    elif key == ord('s'):
                        # Save screenshot
                        screenshot_path = f"accident_frame_{frame_count}.jpg"
                        cv2.imwrite(screenshot_path, annotated_frame)
                        print(f"[INFO] Screenshot saved: {screenshot_path}")
                
        except KeyboardInterrupt:
            print("\n[INFO] Interrupted by user")
        finally:
            # Cleanup
            cap.release()
            if writer:
                writer.release()
            if display:
                cv2.destroyAllWindows()
            
            # Print summary statistics
            print("\n" + "="*50)
            print("DETECTION SUMMARY")
            print("="*50)
            print(f"Total frames processed: {frame_count}")
            print(f"Accidents detected: {accident_detected_frames}")
            if frame_count > 0:
                print(f"Detection rate: {accident_detected_frames/frame_count*100:.2f}%")
            print("="*50)
    
    def log_accident(self, frame_number, timestamp, score, detections):
        """
        Log accident details for alert system.
        
        Args:
            frame_number: Frame where accident was detected
            timestamp: Time of detection
            score: Accident confidence score
            detections: YOLO detection results
        """
        accident_data = {
            'frame': frame_number,
            'timestamp': timestamp,
            'confidence': float(score),
            'alert_status': 'CRITICAL' if score > 0.85 else 'WARNING',
            'location': 'Highway Section A (Placeholder GPS)',  # Add actual GPS data
            'pole_id': 'POLE-001'  # Smart pole identifier
        }
        
        self.accident_log.append(accident_data)
        
        # Save log to file
        log_path = Path('accident_logs')
        log_path.mkdir(exist_ok=True)
        
        log_file = log_path / f"accident_log_{datetime.datetime.now().strftime('%Y%m%d')}.json"
        with open(log_file, 'w') as f:
            json.dump(self.accident_log, f, indent=2)

def main():
    """
    Main function for command-line usage.
    """
    parser = argparse.ArgumentParser(
        description='Highway Accident Detection System - Smart Street Pole Project',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  # Process video file
  python detect_accident.py --video highway_traffic.mp4
  
  # Use webcam (camera index 0)
  python detect_accident.py --video 0
  
  # Save output with custom confidence
  python detect_accident.py --video traffic.mp4 --output detected.mp4 --confidence 0.6
  
  # Run on edge device without display
  python detect_accident.py --video 0 --no-display
        ''')
    
    parser.add_argument('--video', type=str, default='0',
                       help='Video file path or camera index (default: 0 for webcam)')
    parser.add_argument('--output', type=str, default=None,
                       help='Output video path (optional)')
    parser.add_argument('--model', type=str, default='yolov8n.pt',
                       help='YOLOv8 model path (default: yolov8n.pt - nano model)')
    parser.add_argument('--confidence', type=float, default=0.5,
                       help='Detection confidence threshold (default: 0.5, range: 0.0-1.0)')
    parser.add_argument('--no-display', action='store_true',
                       help='Run without display window (useful for edge devices like Raspberry Pi)')
    
    args = parser.parse_args()
    
    # Convert camera index if numeric
    video_source = int(args.video) if args.video.isdigit() else args.video
    
    # Initialize detector
    print("\n" + "="*70)
    print("  MULTIFUNCTIONAL HIGHWAY SMART STREET POLE SYSTEM")
    print("  Accident Detection Module - YOLOv8 Powered")
    print("  Dadi Institute of Engineering and Technology")
    print("="*70 + "\n")
    
    detector = AccidentDetector(model_path=args.model, confidence=args.confidence)
    
    # Process video
    print("\n[INFO] Starting accident detection system...")
    print("[INFO] Press 'q' to quit | Press 's' to save screenshot\n")
    
    detector.process_video(
        video_source=video_source,
        output_path=args.output,
        display=not args.no_display
    )
    
    print("\n[INFO] Accident detection system stopped")

if __name__ == "__main__":
    main()
