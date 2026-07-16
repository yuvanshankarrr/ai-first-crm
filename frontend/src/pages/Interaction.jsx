import { useParams } from "react-router-dom";
import { useEffect, useState } from "react";
import {
    getHCP,
    createInteraction,
    editInteraction,
} from "../services/api";

function Interaction() {

    const { id } = useParams();

    const [loading, setLoading] = useState(true);
    const [error, setError] = useState("");

    const [hcp, setHcp] = useState(null);

    const [visitType, setVisitType] = useState("In Person");

    const [notes, setNotes] = useState("");

    const [instruction, setInstruction] = useState("");

    const [editedNotes, setEditedNotes] = useState("");

    const [result, setResult] = useState(null);

    useEffect(() => {

        async function loadHCP() {

            try {

                const data = await getHCP(id);

                setHcp(data);

                setLoading(false);

            }

            catch (error) {

                console.error(error);

                setError("Failed to load healthcare professional details.");

                setLoading(false);

            }

        }

        loadHCP();

    }, [id]);



    async function handleEdit() {

        try {

            const data = await editInteraction({

                notes,

                instruction,

            });

            setEditedNotes(data.updated_notes);

            // Automatically replace Notes with edited version
            setNotes(data.updated_notes);

        }

        catch (error) {

            console.error(error);

        }

    }



    async function handleAnalyze() {

        try {

            const interaction = {

                hcp_id: Number(id),

                visit_date: "2026-07-14",

                visit_type: visitType,

                // Analyze edited notes if available
                notes: editedNotes || notes,

                follow_up_date: "2026-07-21",

            };

            const data = await createInteraction(interaction);

            setResult(data);

        }

        catch (error) {

            console.error(error);

        }

    }



    if (loading) {

        return <h2>Loading...</h2>;

    }

    if (error) {

        return <h2>{error}</h2>;

    }



    return (

        <div>

            <h1>Interaction</h1>

            {

                hcp && (

                    <div>

                        <h2>{hcp.name}</h2>

                        <p>{hcp.specialization}</p>

                        <p>{hcp.hospital}</p>

                        <hr />

                    </div>

                )

            }

            <h3>Visit Type</h3>

            <select

                value={visitType}

                onChange={(e) => setVisitType(e.target.value)}

            >

                <option>In Person</option>

                <option>Virtual</option>

                <option>Phone Call</option>

            </select>

            <br /><br />

            <h3>Notes</h3>

            <textarea

                rows={8}

                cols={60}

                value={notes}

                onChange={(e) => setNotes(e.target.value)}

            />

            <br /><br />

            <h3>Edit Instruction</h3>

            <input

                type="text"

                value={instruction}

                onChange={(e) => setInstruction(e.target.value)}

                placeholder="Example: Rewrite professionally"

            />

            <br /><br />

            <button onClick={handleEdit}>

                Edit Notes

            </button>

            <br /><br />

            {

                editedNotes && (

                    <div>

                        <h3>Edited Notes</h3>

                        <textarea

                            rows={8}

                            cols={60}

                            value={editedNotes}

                            readOnly

                        />

                    </div>

                )

            }

            <br /><br />

            <button onClick={handleAnalyze}>

                Analyze with AI

            </button>

            {

                result && (

                    <div>

                        <hr />

                        <h2>AI Analysis</h2>

                        <h3>Summary</h3>

                        <p>{result.summary}</p>

                        <h3>Next Action</h3>

                        <p>{result.next_action}</p>

                        <h3>Follow Up</h3>

                        <p>{result.follow_up}</p>

                    </div>

                )

            }

        </div>

    );

}

export default Interaction;