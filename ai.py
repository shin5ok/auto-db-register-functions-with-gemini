
import vertexai
from vertexai.generative_models import GenerativeModel, Part, SafetySetting

import config as c

safety_settings = []

vertexai.init(project=c.PROJECT, location=c.REGION)
model = GenerativeModel(
    "gemini-1.5-flash-002",
)


def generate(file_path: str):
    # print(f"Processing...{file_path}")

    with open(file_path, "rb") as f:
                pdf_data = f.read()

    document1 = Part.from_data(
            mime_type="application/pdf",
            data=pdf_data,
    )

    responses = model.generate_content(
        [document1, 
        """
         できるだけ情報を読み取って JSON で出力して
         キー名は英語にして
        """],
        generation_config=c.GEN_CONFIG,
        safety_settings=safety_settings,
        stream=True,
    )

    for response in responses:
        print(response.text, end="")

if __name__ == "__main__":
    import sys
    file = sys.argv[1]
    generate(file)
