import React, { useState } from "react";
import VideoUploader from "./components/VideoUploader";
import DetectionDisplay from "./components/DetectionDisplay";
import EmergencyAlert from "./components/EmergencyAlert";

const App = () => {
  const [detections, setDetections] = useState([]);  // ✅ Keep this here inside the App component

  return (
    <div className="p-4 flex flex-col items-center">
      <h1 className="text-2xl font-bold mb-4">Traffic Management System</h1>
      <VideoUploader setDetections={setDetections} />  {/* Pass setDetections as a prop */}
      <DetectionDisplay detections={detections} />  {/* Pass detections */}
      <EmergencyAlert detections={detections} />  {/* Pass detections */}
    </div>
  );
};

export default App;
