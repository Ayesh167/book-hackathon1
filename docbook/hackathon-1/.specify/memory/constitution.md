<!--
Sync Impact Report:
- Version change: 0.0.0 → 1.0.0
- Modified principles:
  - PRINCIPLE_1_NAME → Accuracy through primary source execution
  - PRINCIPLE_2_NAME → Clarity for academic audiences
  - PRINCIPLE_3_NAME → Reproducibility
  - PRINCIPLE_4_NAME → Rigor
- Added sections:
  - Key Standards
  - Constraints
  - Success Criteria
- Removed sections: None
- Templates requiring updates:
  - ✅ .specify/templates/plan-template.md
  - ✅ .specify/templates/spec-template.md
  - ✅ .specify/templates/tasks-template.md
- Follow-up TODOs: None
-->
# Integrated RAG Chatbot Development for an AI-Native Textbook Constitution

## Core Principles

### I. Accuracy through primary source execution
All technical explanations must prioritize original research papers, specifications, and official documentation. All claims must be traceable, testable, and repeatable.

### II. Clarity for academic audiences
Writing must be technically precise yet readable for university-level computer science students. It must target a Flesch–Kincaid grade level of 10–12.

### III. Reproducibility
All claims must be traceable, testable, and repeatable. All setup steps, configuration files, and reproducible experiment procedures must be included.

### IV. Rigor
Prefer peer-reviewed sources over blogs or marketing material. All work must include critical analysis and limitations.

## Key Standards
- All factual claims must be traceable to a source.
- Citation format: APA Style.
- Minimum 50% of sources must be peer-reviewed articles.
- Plagiarism check: 0% tolerance before submission.
- Writing clarity must target Flesch–Kincaid grade 10–12.

## Constraints
- Total word count: 5,000–7,000 words.
- Minimum 15 sources.
- Output format: PDF-ready academic document with embedded APA citations.

## Success Criteria
- All technical and factual claims verified against sources.
- Zero plagiarism detected.
- Passes independent fact-checking review.

## Governance

This Constitution is the authoritative source for project standards. All development, documentation, and testing MUST adhere to these principles.

- **Technical Governance**: The system will use FastAPI for the backend and Qdrant Cloud Free Tier for the vector database. All development must align with the official documentation for these technologies.
- **Architecture Decisions**: All architectural decisions must be documented in ADRs, explaining the rationale, trade-offs, and alignment with the Core Principles.
- **Source Verification**: A `sources.md` file will be maintained, mapping every claim to its source.
- **Validation Pipeline**: Automated checks for plagiarism, citation format, and source linkage are required.
- **Quality Gates**: No work is considered "done" until it passes a peer review and an independent fact-checking review.

**Version**: 1.0.0 | **Ratified**: 2025-12-07 | **Last Amended**: 2025-12-07