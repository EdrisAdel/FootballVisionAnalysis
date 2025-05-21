import { useState, useRef } from 'react'
import './App.css'

function App() {
  const fileInputRef = useRef(null);

  const handleFile = (e) => {
    const file = e.target.files[0];
    if (file && file.type !== "video/mp4" && !file.name.endsWith('.mp4')) {
      alert("Please upload an MP4 file.");
      fileInputRef.current.value = "";
    }
  };

  return (
    <>
      <div className="file-container">
        <input type="file" id="file" name="uploadedFile" accept=".mp4,video/mp4" onChange={handleFile} ref={fileInputRef} />
        <input type="submit" value="Upload Selected File" />
      </div>
    </>
  )
}

export default App
