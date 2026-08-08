import { useState } from "react"
import api from "../services/api";
import { useNavigate } from "react-router-dom";

function Login()  {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const navigate = useNavigate();
    const handleLogin = async (e) => {
    e.preventDefault();

    const formData = new URLSearchParams();

    formData.append("username", email);
    formData.append("password", password);

    const response = await api.post("/login", formData, {
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        }
    });

    console.log(response.data);
};
    return(
        <div>
            <h1>Login</h1>
            <form onSubmit={handleLogin}>
                email:<input type="email" name="email" placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)} />
                password:<input type="password" name="password" value={password} onChange={(e) => setPassword(e.target.value)}/>
                <button type="submit">Login</button>
            </form>
        </div>
    );
}
export default Login;