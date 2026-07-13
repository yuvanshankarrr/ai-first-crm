from app.agents.crm_agent import crm_agent

result = crm_agent.invoke(
    {
        "notes": """
        Met Dr Rajesh Kumar.

        He appreciated Product X.

        Requested clinical trial comparison with Competitor Y.

        Asked for follow-up next week.
        """
    }
)

print(result["summary"])