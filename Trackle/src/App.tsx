import { useState, useEffect } from "react";
import { listen } from "@tauri-apps/api/event";
import StatCard from "./components/NetworkTable";
import { Network, Hardware } from "./types";


function App() {
  const [networkData, setNetworkData] = useState<Network | null>(null);
  const [hardwareData, setHardwareData] = useState<Hardware | null>(null);
  const [data, setData] = useState<any>({});
  useEffect(() => {
  let unlistenFn: any;

  const setup = async () => {
    unlistenFn = await listen("system-data", (event) => {
      const parsed = JSON.parse(event.payload as string);
      setNetworkData(parsed.network);
      setHardwareData(parsed.hardware);
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
      <h1 className="text-6xl font-bold text-blue-500">Trackle</h1>
      <StatCard title="CPU" value={hardwareData?.cpu_percentage + "%"} />
      <StatCard title="Ethernet" value={networkData?.speed?.Ethernet?.[2] + " Mbps"} />
      {networkData?.speed?.["Wi-Fi"] && (
        <StatCard title="Wi-Fi" value={networkData?.speed?.["Wi-Fi"]?.[2] + " Mbps"} />
      )}
      <pre>{JSON.stringify(data, null, 2)}</pre>
      
    </div>
  );
}

export default App;


