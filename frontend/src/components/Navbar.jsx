import { Link } from "react-router-dom";
import "../styles/navbar.css";


function Navbar() {
    return (
        <nav className="navbar">
            <h2>AI First CRM</h2>

            <div>
                <Link to="/">Dashboard</Link>
                {" | "}
                <Link to="/history">History</Link>
            </div>
        </nav>
    );
}

export default Navbar;