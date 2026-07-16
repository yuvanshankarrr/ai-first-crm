import { Link } from "react-router-dom";

function HCPCard({ hcp }) {
    return (
        <div className="hcp-card">
            <h2>{hcp.name}</h2>

            <p>
                <strong>Specialization:</strong> {hcp.specialization}
            </p>

            <p>
                <strong>Hospital:</strong> {hcp.hospital}
            </p>

            <p>
                <strong>City:</strong> {hcp.city}
            </p>

            <Link to={`/interaction/${hcp.id}`}>
                <button>Open CRM</button>
            </Link>
        </div>
    );
}

export default HCPCard;