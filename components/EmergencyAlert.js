import React, { useEffect, useState } from "react";
import axios from "axios";

const EmergencyAlert = ({ detections }) => {
  const [distance, setDistance] = useState(null);
  const [estimatedTime, setEstimatedTime] = useState(null);
  const [vehicleCounts, setVehicleCounts] = useState({});

  useEffect(() => {
    if (!Array.isArray(detections)) return;

    const flattenedDetections = detections.flat();
    
    // Count different types of vehicles
    const counts = flattenedDetections.reduce((acc, vehicle) => {
      acc[vehicle.class] = (acc[vehicle.class] || 0) + 1;
      return acc;
    }, {});
    setVehicleCounts(counts);

    // Find emergency vehicle and get distance/time
    const emergencyVehicle = flattenedDetections.find(d => d.class === "Emergency");
    if (emergencyVehicle) {
      axios.get("http://localhost:8000/calculate-distance", {
        params: { bbox: emergencyVehicle.bbox.join(",") }
      }).then(response => {
        setDistance(response.data.distance);
        setEstimatedTime(response.data.estimated_time);
      }).catch(error => console.error("Error calculating distance:", error));
    }
  }, [detections]);

  return (
    <div className="mt-4 p-4 bg-gray-100 rounded text-center">
      <h2 className="text-xl font-semibold mb-2">Vehicle Detection Overview</h2>

      {/* Display vehicle counts */}
      <div className="mb-4">
        <h3 className="text-lg font-medium">Detected Vehicles:</h3>
        <ul className="list-disc list-inside">
          {Object.entries(vehicleCounts).map(([type, count]) => (
            <li key={type}>{type}: {count}</li>
          ))}
        </ul>
      </div>

      {/* Display emergency vehicle details if detected */}
      {distance !== null && estimatedTime !== null && (
        <div className="p-4 bg-yellow-100 rounded">
          <h2 className="text-xl font-semibold">Emergency Vehicle Details</h2>
          <p>Distance from CCTV: {distance} meters</p>
          <p>Estimated Time to Cross: {estimatedTime} seconds</p>
        </div>
      )}
    </div>
  );
};

export default EmergencyAlert;
