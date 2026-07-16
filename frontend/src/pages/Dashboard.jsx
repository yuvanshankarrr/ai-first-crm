import { useEffect, useState } from "react";
import { getHCPs } from "../services/api";
import HCPCard from "../components/HCPCard";

function Dashboard() {

    const [loading, setLoading] = useState(true);

    const [hcps, setHcps] = useState([]);

    useEffect(() => {

        async function loadHCPs() {

            try {

                const data = await getHCPs();
                console.log(data);

                setHcps(data);
                setLoading(false);

            }

            catch (error) {

                console.error(error);

            }

        }

        loadHCPs();

    }, []);

    if (loading) {
        return <h2>Loading...</h2>;
}

    return (

        <div>

            <h1>AI First CRM</h1>

            <h2>Healthcare Professionals</h2>

            {

                hcps.map((hcp) => (

                    <HCPCard
                        key={hcp.id}
                        hcp={hcp}
                    />


                ))

            }

        </div>

    );

}

export default Dashboard;