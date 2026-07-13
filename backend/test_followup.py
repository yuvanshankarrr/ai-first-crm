from app.tools.extract_followup import extract_followup

notes = """
Met Dr Rajesh Kumar.

Doctor appreciated Product X.

Requested clinical trial comparison.

Asked for follow-up next week.
"""

print(extract_followup(notes))



# from app.tools.extract_followup import extract_followup

# print("Starting...")

# notes = """
# Met Dr Rajesh Kumar.

# Doctor appreciated Product X.

# Requested clinical trial comparison.

# Asked for follow-up next week.
# """

# result = extract_followup(notes)

# print("Result object:")
# print(repr(result))

# print("Done")