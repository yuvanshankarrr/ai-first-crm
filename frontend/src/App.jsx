import { BrowserRouter, Routes, Route } from "react-router-dom";

import Navbar from "./components/Navbar";

import Dashboard from "./pages/Dashboard";
import Interaction from "./pages/Interaction";
import History from "./pages/History";

function App() {
  return (
    <BrowserRouter>

      <Navbar />

      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/interaction/:id" element={<Interaction />} />
        <Route path="/history" element={<History />} />
      </Routes>

    </BrowserRouter>
  );
}

export default App;