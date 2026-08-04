import Sidebar from "../components/layouts/Sidebar";
import Topbar from "../components/layouts/Topbar";

function MainLayout({ children }) {
  return (
    <div style={{ display: "flex", height: "100vh" }}>
      <Sidebar />

      <div style={{ flex: 1 }}>
        <Topbar />

        <main style={{ padding: "20px" }}>
          {children}
        </main>
      </div>
    </div>
  );
}

export default MainLayout;