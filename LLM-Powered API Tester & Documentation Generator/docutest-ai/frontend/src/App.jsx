import React, { useState } from "react";
import axios from "axios";
import CodeEditor from "./Components/CodeEditor";

export default function App() {
  const [file, setFile] = useState(null);
  const [code, setCode] = useState("");

  const handleUpload = async () => {
    const formData = new FormData();
    formData.append("file", file);
    const res = await axios.post("http://localhost:8000/upload/", formData);
    setCode(res.data.test_code);
  };

  return (
    <div className="max-w-4xl mx-auto p-6">
      <h1 className="text-3xl font-bold mb-4">DocuTest AI</h1>
      <input type="file" onChange={(e) => setFile(e.target.files[0])} className="mb-4" />
      <button className="bg-blue-600 text-white px-4 py-2" onClick={handleUpload}>
        Upload API Spec
      </button>
      <div className="mt-6">
        <CodeEditor code={code} />
      </div>
    </div>
  );
}
