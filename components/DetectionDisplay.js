import { useEffect } from "react";

const DetectionDisplay = ({ detections }) => {
  useEffect(() => {
    if (!Array.isArray(detections) || detections.length === 0) return;

    const allDetections = detections.flat().filter(Boolean); // Prevent null issues
    const emergencyDetected = allDetections.some(
      (detection) => detection.class === "emergency_vehicle"
    );

    if (emergencyDetected) {
      const alertSound = new Audio("/alert.mp3");
      alertSound.play().catch((err) =>
        console.error("Error playing alert sound:", err)
      );
    }
  }, [detections]);

  return null; // 🚨 REMOVE ALL TEXT & UI, just keep emergency alert
};

export default DetectionDisplay;
