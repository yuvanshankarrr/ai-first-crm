from app.tools.recommend_next_action import recommend_next_action

notes = """
Met Dr Rajesh Kumar.

Doctor appreciated Product X.

Requested clinical trial comparison.

Asked for follow-up next week.
"""

print(recommend_next_action(notes))