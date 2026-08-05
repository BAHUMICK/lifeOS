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

      <MenuItem icon={<FaHome />} text="Dashboard" />
      <MenuItem icon={<FaTasks />} text="Tasks" />
      <MenuItem icon={<FaStickyNote />} text="Notes" />
      <MenuItem icon={<FaCalendarAlt />} text="Calendar" />
      <MenuItem icon={<FaWallet />} text="Expenses" />
      <MenuItem icon={<FaUser />} text="Profile" />
      <MenuItem icon={<FaCog />} text="Settings" />
    </div>
  );
}

function MenuItem({ icon, text }) {
  return (
    <div
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