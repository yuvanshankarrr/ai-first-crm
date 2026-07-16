import { useEffect, useState } from "react";
import { getInteractions } from "../services/api";

function History() {

    const [loading, setLoading] = useState(true);
    const [error, setError] = useState("");

    const [interactions, setInteractions] = useState([]);

    useEffect(() => {

        async function loadHistory() {

            try {

                const data = await getInteractions();
                setInteractions(data);
                setLoading(false);
            }

            catch (error) {

                console.error(error);
                setError("Failed to load interaction history.");
                setLoading(false);

            }

        }

        loadHistory();

    }, []);

    if (loading) {
        return <h2>Loading...</h2>;
}

    if (error) {
       return <h2>{error}</h2>;
}

    return (

        <div>

            <h1>Interaction History</h1>

            {

                interactions.map((interaction) => (

                    <div className="history-card" key={interaction.id}>

    <h2>{interaction.hcp.name}</h2>

    <p>
        <strong>Specialization:</strong>{" "}
        {interaction.hcp.specialization}
    </p>

    <p>
        <strong>Hospital:</strong>{" "}
        {interaction.hcp.hospital}
    </p>

    <hr />

    <p>
        <strong>Visit Type:</strong>{" "}
        {interaction.visit_type}
    </p>

    <p>
        <strong>Visit Date:</strong>{" "}
        {interaction.visit_date}
    </p>

    <h4>Summary</h4>

    <p>{interaction.summary}</p>

</div>

                ))

            }

        </div>

    );

}

export default History;