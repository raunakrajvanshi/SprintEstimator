from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_prompt(description, criteria, team_size, dependencies, risks):
    prompt = f"""
    You're an agile sprint estimator with deep knowledge of software development tasks and complexities. Based on historical data, estimate the effort in Story Points and Hours.

    User Story: {description}
    Acceptance Criteria: {criteria}
    Team Size: {team_size}
    Dependencies: {dependencies}
    Risks: {risks}

    Provide:
    - Suggested Story Points (numeric)
    - Suggested Effort in Hours (numeric)
    - Briefly highlight potential dependencies, risks, or bottlenecks.

    Example Response:
    Story Points: 5
    Hours: 8
    Dependencies: Dependency details...
    Risks: Risk details...
    Bottlenecks: Bottleneck details...
    """
    return prompt

def get_estimation(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=200,
        temperature=0.3
    )
    return response.choices[0].message.content.strip()
