def clarify_requirements(domain: str) -> str:
    print("Please answer the following to refine your CRM needs:\n")

    name = input("Business Name: ")
    scale = input("Scale (e.g. startup, enterprise): ")
    focus = input(f"What is the main goal for this {domain} CRM? ")

    return f"Business: {name}\nScale: {scale}\nGoal: {focus}"
