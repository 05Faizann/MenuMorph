import { useCallback, useState } from "react";
import { useDropzone } from "react-dropzone";
import axios from "axios";

export default function App() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [websiteUrl, setWebsiteUrl] = useState("");

  const onDrop = useCallback((acceptedFiles) => {
    if (acceptedFiles.length > 0) {
      setSelectedFile(acceptedFiles[0]);
      setWebsiteUrl("");
    }
  }, []);

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop,
    accept: {
      "image/*": [".jpg", ".jpeg", ".png"],
      "application/pdf": [".pdf"],
    },
    multiple: false,
  });

  const uploadMenu = async () => {
    if (!selectedFile) return;

    setLoading(true);

    const formData = new FormData();
    formData.append("file", selectedFile);

    try {
      const response = await axios.post(
        "https://menumorph.onrender.com/upload",
        formData
      );
      console.log("Response:", response);
      console.log("Response data:", response.data);

      const fullUrl =
        "https://menumorph.onrender.com" +
        response.data.website_url;

      setWebsiteUrl(fullUrl);
    } catch (error) {
        console.error("Axios Error:", error);

        if (error.response) {
          console.log("Status:", error.response.status);
          console.log("Headers:", error.response.headers);
          console.log("Data:", error.response.data);
          alert(`Backend Error: ${error.response.status}`);
        } else if (error.request) {
          console.log("Request:", error.request);
          alert("No response received from backend.");
        } else {
          console.log("Message:", error.message);
          alert(error.message);
        }
      }

    setLoading(false);
  };

  return (
    <div className="min-h-screen bg-gray-100 flex items-center justify-center px-6">
      <div className="bg-white rounded-3xl shadow-xl p-10 w-full max-w-xl">

        <div className="text-center">
          <h1 className="text-5xl font-bold">
            🍽️ MenuMorph
          </h1>

          <p className="mt-4 text-gray-600 text-lg">
            Turn your restaurant menu into a beautiful AI-generated website.
          </p>
        </div>

        <div
          {...getRootProps()}
          className={`mt-10 border-2 border-dashed rounded-2xl p-12 text-center cursor-pointer transition
          ${
            isDragActive
              ? "border-violet-600 bg-violet-50"
              : "border-gray-300 hover:border-violet-500 hover:bg-gray-50"
          }`}
        >
          <input {...getInputProps()} />

          <div className="text-6xl">
            📄
          </div>

          <h2 className="text-xl font-semibold mt-4">
            {isDragActive
              ? "Drop your menu here"
              : "Drag & Drop your menu"}
          </h2>

          <p className="text-gray-500 mt-2">
            or click to browse
          </p>

          <p className="text-sm text-gray-400 mt-6">
            JPG • PNG • PDF
          </p>
        </div>

        {selectedFile && (
          <div className="mt-5 bg-gray-50 rounded-xl p-4">
            <p className="font-medium">
              📁 {selectedFile.name}
            </p>

            <p className="text-sm text-gray-500">
              {(selectedFile.size / 1024 / 1024).toFixed(2)} MB
            </p>
          </div>
        )}

        <button
          onClick={uploadMenu}
          disabled={!selectedFile || loading}
          className="w-full mt-6 bg-violet-600 hover:bg-violet-700 text-white py-4 rounded-xl font-semibold transition disabled:bg-gray-400"
        >
          {loading ? "Generating Website..." : "Generate Website"}
        </button>

        {loading && (
          <div className="mt-6 text-center">

            <div className="animate-spin rounded-full h-10 w-10 border-b-2 border-violet-600 mx-auto"></div>

            <p className="mt-4 text-gray-600">
              AI is building your website...
            </p>

          </div>
        )}

        {websiteUrl && (
          <div className="mt-8 rounded-2xl border border-green-300 bg-green-50 p-6">

            <h2 className="text-xl font-bold text-green-700">
              🎉 Website Ready!
            </h2>

            <p className="mt-3 text-gray-700 break-all">
              {websiteUrl}
            </p>

            <a
              href={websiteUrl}
              target="_blank"
              rel="noreferrer"
              className="block text-center mt-5 bg-green-600 hover:bg-green-700 text-white py-3 rounded-xl font-semibold transition"
            >
              Open Website
            </a>

          </div>
        )}

      </div>
    </div>
  );
}