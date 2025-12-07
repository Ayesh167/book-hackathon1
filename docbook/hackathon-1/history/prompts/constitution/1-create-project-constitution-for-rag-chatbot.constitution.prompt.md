---
id: 1
title: Create Project Constitution for RAG Chatbot
stage: constitution
date: 2025-12-07
surface: agent
model: gemini
feature: none
branch: unknown
user: unknown
command: /sp.constitution
labels: [constitution, rag, chatbot]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .specify/memory/constitution.md
  - .specify/templates/plan-template.md
  - .specify/templates/tasks-template.md
tests:
  - none
---

## Prompt

/sp.constitution Create a Speckit Constitution for the project: 
“Integrated RAG Chatbot Development for an AI-Native Textbook”.

PROJECT SCOPE:
Design, implement, and document a Retrieval-Augmented Generation (RAG) chatbot embedded within a published technical textbook. 
The chatbot must:
- Answer user questions about the textbook content
- Support answering based only on user-selected text
- Use OpenAI Agents/ChatKit SDKs
- Use FastAPI as the backend framework
- Use Qdrant Cloud Free Tier as the vector database
- Be production-ready and academically documented

CORE PRINCIPLES:
1. Accuracy through primary source execution
   - All technical explanations must prioritize original research papers, specifications, and official documentation.

2. Clarity for academic audiences (computer science background)
   - Writing must be technically precise yet readable for university-level CS students.

3. Reproducibility
   - All claims must be traceable, testable, and repeatable.
   - Include setup steps, configuration files, and reproducible experiment procedures.

4. Rigor
   - Prefer peer-reviewed sources over blogs or marketing material.
   - Include critical analysis and limitations.

KEY STANDARDS:
- All factual claims must be traceable to sources.
- Citation format: APA Style
- Minimum 50% of sources must be peer-reviewed articles
- Plagiarism check: 0% tolerance before submission
- Writing clarity must target Flesch–Kincaid grade 10–12

CONSTRAINTS:
- Total word count: 5,000–7,000 words
- Minimum 15 sources
- Output format: PDF-ready academic document with embedded APA citations

SUCCESS CRITERIA:
- All technical and factual claims verified against sources
- Zero plagiarism detected
- Passes independent fact-checking review

REQUIRED OUTPUT:
Generate a formal “Speckit Constitution” that will govern how this RAG Chatbot system is implemented, documented, tested, and validated.
The constitution must include:
- Technical governance rules
- Architecture decision standards
- Source verification workflow
- Citation and validation pipeline
- Quality gates for academic publication

## Response snapshot

I have created the Speckit Constitution for the "Integrated RAG Chatbot Development for an AI-Native Textbook" project. I have also updated the plan and tasks templates to align with the new constitution.

## Outcome

- ✅ Impact: The project now has a constitution that defines the core principles and standards for the project.
- 🧪 Tests: none
- 📁 Files: 3 files modified
- 🔁 Next prompts: /sp.specify
- 🧠 Reflection: The constitution is a key document for aligning the team and ensuring quality.

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): none
- Next experiment (smallest change to try): none
