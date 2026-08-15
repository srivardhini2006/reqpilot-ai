from app.services.llm_service import LLMService

def main():
    llm = LLMService()

    response = llm.generate_text(
        "Introduce yourself as a Business Analyst in two sentences."
    )

    print(response)


if __name__ == "__main__":
    main()