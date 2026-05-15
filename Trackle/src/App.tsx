import { useState, useEffect } from "react";
import { listen } from "@tauri-apps/api/event";



function App() {
  const [data, setData] = useState({});
  useEffect(() => {
  let unlistenFn: any;

  const setup = async () => {
    unlistenFn = await listen("system-data", (event) => {
      const parsed = JSON.parse(event.payload as string);
      setData(parsed);
    });
  };

  setup();

  return () => {
    if (unlistenFn) unlistenFn();
  };
}, []);


  return (
    <div>
      <h1>Trackle</h1>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
}

export default App;


