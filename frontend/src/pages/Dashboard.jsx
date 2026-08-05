import MainLayout from "../layouts/MainLayout";
import DashboardCard from "../components/DashboardCard";
import { FaTasks } from "react-icons/fa";

function Dashboard() {
  return (
    <MainLayout>
      <div 
      style={{
        display : "flex",
        gap: "20px"
      }}
      >
        <DashboardCard
          title="Total Tasks"
          value={15}
          icon={<FaTasks />}
        />
                <DashboardCard
          title="Total Notes"
          value={24}
          icon={<FaTasks />}
        />
                <DashboardCard
          title="Total Expenses"
          value={2500}
          icon={<FaTasks />}
        />
      </div>
    </MainLayout>
  );
}

export default Dashboard;