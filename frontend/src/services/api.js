const BASE_URL = "http://127.0.0.1:8000";

export async function getHCPs() {
    const response = await fetch(`${BASE_URL}/hcps/`);

    if (!response.ok) {
        throw new Error("Failed to fetch HCPs");
    }

    return await response.json();
}

export async function getHCP(id) {

    const response = await fetch(`${BASE_URL}/hcps/${id}`);

    if (!response.ok) {
        throw new Error("Failed to fetch HCP");
    }

    return await response.json();
}

export async function createInteraction(interaction) {

    const response = await fetch(`${BASE_URL}/interactions/`, {

        method: "POST",

        headers: {
            "Content-Type": "application/json",
        },

        body: JSON.stringify(interaction),

    });

    if (!response.ok) {

        throw new Error("Failed to create interaction");

    }

    return await response.json();

}


export async function getInteractions() {

    const response = await fetch(`${BASE_URL}/interactions/`);

    if (!response.ok) {
        throw new Error("Failed to fetch interactions");
    }

    return await response.json();
}

export async function editInteraction(data) {

    const response = await fetch(`${BASE_URL}/interactions/edit`, {

        method: "POST",

        headers: {
            "Content-Type": "application/json",
        },

        body: JSON.stringify(data),

    });

    if (!response.ok) {
        throw new Error("Failed to edit notes");
    }

    return await response.json();
}