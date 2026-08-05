function DashboardCard({title, icon, value}) {
    return (
  <div
    style={{
      width: "300px",
      background: "#2c4477",
      color: "white",
      padding: "20px",
      borderRadius: "16px",
      fontSize: "32px",
      fontWeight: "bold",
      marginTop: "15px",
      boxShadow: "0px 4px 10px rgba(0,0,0,0.3)"
    }}
  >
    <div
    style={{
        display: "flex",
        alignItems: "center",
        gap: "10px"
    }}
    >  
        {icon}
        {title} 
    </div>
    {value}
  </div>
);
}
export default DashboardCard;