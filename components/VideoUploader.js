import React, { useState } from "react";
import axios from "axios";

const VideoUploader = () => {
  const [selectedFile, setSelectedFile] = useState(null);
  const [videoURL, setVideoURL] = useState(null); // Stores video preview URL
  const [loading, setLoading] = useState(false);

  // ✅ Handle file selection and preview
  const handleFileChange = (event) => {
    const file = event.target.files[0];
    if (file) {
      setSelectedFile(file);
      setVideoURL(URL.createObjectURL(file)); // Create local preview URL
      console.log("Selected file:", file.name);
    }
  };

  // ✅ Handle file upload & processing
  const handleUpload = async () => {
    if (!selectedFile) {
      alert("Please select a video file first!");
      return;
    }

    setLoading(true);
    const formData = new FormData();
    formData.append("file", selectedFile);

    try {
      await axios.post("http://localhost:8000/process-video/", formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });

      console.log("Video uploaded successfully.");
    } catch (error) {
      console.error("Error uploading video:", error);
      alert("Error processing video.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex flex-col items-center space-y-4">
      <input type="file" accept="video/*" onChange={handleFileChange} className="p-2 border" />
      
      {videoURL && (
        <video
          src={videoURL}
          controls
          className="mt-4 w-full max-w-md rounded-lg shadow-lg"
        />
      )}

      <button
        onClick={handleUpload}
        className="px-4 py-2 bg-blue-500 text-white rounded disabled:opacity-50"
        disabled={loading || !selectedFile}
      >
        {loading ? "Processing..." : "Upload & Process"}
      </button>
    </div>
  );
};

export default VideoUploader;
