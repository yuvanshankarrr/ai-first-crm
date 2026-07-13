from app.tools.edit_interaction import edit_interaction


notes = """
Met Dr Rajesh Kumar.

Doctor appreciated Product X.

Requested clinical trial comparison.
"""

instruction = """
Add that the doctor also requested pricing details.
"""

updated = edit_interaction(
    notes,
    instruction,
)

print(updated)