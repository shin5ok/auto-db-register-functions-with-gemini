
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
         構造的に丁寧に情報を読み取って JSON で出力して
         最後まで読み取るように
         キー名は日本語にして
        """],
        generation_config=c.GEN_CONFIG,
        safety_settings=safety_settings,
        stream=False,
    )

    import json

    return json.loads(responses.text)

if __name__ == "__main__":
    import sys
    file = sys.argv[1]
    generate(file)