import { useNavigate } from "react-router-dom";
import { useLocation } from "react-router-dom";

import {
  FaHome,
  FaTasks,
  FaStickyNote,
  FaCalendarAlt,
  FaWallet,
  FaUser,
  FaCog,
} from "react-icons/fa";

function Sidebar() {

  const navigate = useNavigate();
  const location = useLocation();
  return (
    <div
      style={{
        width: "250px",
        background: "#111827",
        color: "white",
        height: "100vh",
        padding: "20px",
        boxSizing: "border-box",
      }}
    >
      <h2 style={{ marginBottom: "30px" }}>🚀 LifeOS</h2>

      <MenuItem icon={<FaHome />} text="Dashboard" route="/dashboard" navigate={navigate} />
      <MenuItem icon={<FaTasks />} text="Tasks" route="/tasks"  navigate={navigate}/>
      <MenuItem icon={<FaStickyNote />} text="Notes" route="/notes" navigate={navigate} />
      <MenuItem icon={<FaCalendarAlt />} text="Calendar" route="/calendar" navigate={navigate}/>
      <MenuItem icon={<FaWallet />} text="Expenses" route = "/expenses" navigate={navigate}/>
      <MenuItem icon={<FaUser />} text="Profile" route = "/profile" navigate={navigate}/>
      <MenuItem icon={<FaCog />} text="Settings" route = "/settings" />
    </div>
  );
}

function MenuItem({ icon, text, route, navigate }) {
  return (
    <div onClick={() => navigate(route)}
      style={{
        display: "flex",
        gap: "12px",
        alignItems: "center",
        padding: "12px",
        marginBottom: "8px",
        borderRadius: "10px",
        cursor: "pointer",
      }}
    >
      {icon}
      {text}
    </div>
  );
}

export default Sidebar;