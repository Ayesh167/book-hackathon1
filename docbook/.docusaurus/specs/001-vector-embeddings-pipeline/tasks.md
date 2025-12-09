# Tasks: AI-Native Textbook – Gemini CLI Integration Setup

**Input**: Design documents from `specs/001-vector-embeddings-pipeline/`
**Prerequisites**: plan.md (required), spec.md (required for user stories)

## Format: `[ID] [P?] [Story?] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create `backend/` directory and basic Python project structure.
- [X] T002 Initialize Python project with `FastAPI` and other dependencies in `backend/requirements.txt`.
- [X] T003 [P] Configure linting and formatting tools for Python in `backend/pyproject.toml`.

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T004 Implement Docusaurus content source registration mechanism in `.specifyplus/config/content_source.py`.
- [X] T005 Develop structural manifest generation for all Docusaurus chapters in `.specifyplus/manifests/book_structure_generator.py`.
- [X] T006 Implement heading-based section indexing logic in `.specifyplus/config/section_indexer.py`.
- [X] T007 Integrate stable Content Identifiers (CID) generation for every section in `.specifyplus/config/cid_generator.py`.

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

## Phase 3: AI-Readiness Configuration

**Goal**: Prepare content for AI ingestion

### Implementation for AI-Readiness

- [X] T008 Implement semantic chunk boundary detection in `.specifyplus/config/chunking_strategy.py`.
- [X] T009 Develop paragraph-level content normalization for vector compatibility in `backend/src/services/content_normalizer.py`.
- [X] T010 Implement metadata tag attachment for retrieval context in `.specifyplus/config/metadata_tagger.py`.

## Phase 4: User-Experience Hooks

**Goal**: Register future hooks for user experience enhancements

### Implementation for UX Hooks

- [X] T011 Define placeholder for chapter-level personalization buttons in `.specifyplus/hooks/personalization_hook.py`.
- [X] T012 Define placeholder for Urdu translation toggles in `.specifyplus/hooks/translation_hook.py`.
- [X] T013 Define placeholder for user background-aware content variants in `.specifyplus/hooks/content_variant_hook.py`.

## Phase 5: Integration Stubs

**Goal**: Define placeholders for external service integrations

### Implementation for Integration Stubs

- [X] T014 Define placeholder for FastAPI service layer in `backend/src/main.py`.
- [X] T015 Define placeholder for Qdrant vector database client in `backend/src/services/qdrant_client.py`.
- [X] T016 Define placeholder for Neon Postgres user store client in `backend/src/services/postgres_client.py`.

## Phase 6: Runtime Intelligence Preparation

**Goal**: Enable extension points for Gemini CLI sub-agents and skill registry

### Implementation for Runtime Intelligence

- [X] T017 Enable extension points for Gemini CLI sub-agents in `.specifyplus/agents/extension_points.py`.
- [X] T018 Register reusable agent skills in `.specifyplus/agents/skill_registry.py`.
- [X] T019 Prepare system prompt registry in `.specifyplus/agents/system_prompt_registry.py`.

## Phase N+1: Constitution Compliance

**Purpose**: Ensure compliance with the project constitution.

- [X] T020 Verify all claims are traceable to sources in all generated content.
- [X] T021 Verify all citations are in APA format in all generated content.
- [X] T022 Verify at least 50% of sources are peer-reviewed in all generated content.
- [X] T023 Run plagiarism check on all generated content.
- [X] T024 Verify writing clarity meets Flesch-Kincaid grade 10-12 in all generated content.
- [X] T025 Verify word count is between 3000-5000 words for all new content.
- [X] T026 Verify there are at least 15 sources for all new content.
- [X] T027 Verify output is a PDF-ready academic document for all new content.

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all subsequent phases
- **AI-Readiness Configuration (Phase 3)**: Depends on Foundational phase completion
- **User-Experience Hooks (Phase 4)**: Depends on Foundational phase completion
- **Integration Stubs (Phase 5)**: Depends on Foundational phase completion
- **Runtime Intelligence Preparation (Phase 6)**: Depends on Foundational phase completion
- **Constitution Compliance (Phase N+1)**: Can be performed in parallel with or after other phases, but should be completed before final deployment.

### Within Each Phase

- Tasks within each phase should generally be executed sequentially unless marked with [P] for parallel execution.

### Parallel Opportunities

- T001, T002, T003 can run in parallel.
- Tasks within AI-Readiness, User-Experience Hooks, Integration Stubs, and Runtime Intelligence Preparation phases can be developed in parallel once the Foundational phase is complete.

## Implementation Strategy

### Incremental Delivery

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phases 3, 4, 5, 6 incrementally or in parallel.
4. Complete Phase N+1: Constitution Compliance.

## Notes

- Each task should be specific enough for an LLM to complete without additional context.
- Verify tasks are marked as complete upon successful execution.
