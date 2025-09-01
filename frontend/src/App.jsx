import { useEffect, useState } from "react";

function App() {
  const [message, setMessage] = useState("");

  useEffect(() => {
    fetch("http://127.0.0.1:8000")
      .then((res) => res.json())
      .then((data) => setMessage(data.message));
  }, []);

  return <div className="p-6 text-xl font-bold">{message || "Loading..."}</div>;
}

export default App;
