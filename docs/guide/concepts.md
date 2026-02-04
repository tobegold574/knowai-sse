# Core Concepts

## Values

Values are the core concept of KnowAI SSE, used to guide the direction of search instruction generation. The system supports the following value dimensions:

### radical (Radicalism)

Focus on frontier labs, GitHub trends, unpublished papers.

Use cases:
- Tracking latest technological breakthroughs
- Discovering unpublished research
- Following experimental projects

### ethics (Ethical Concern)

Focus on AI ethics, digital divide, technological fairness, social impact.

Use cases:
- Technology ethics research
- Social impact assessment
- Fairness analysis

### practical (Pragmatism)

Focus on engineering practices, application cases, implementation effects, business value.

Use cases:
- Engineering practice exploration
- Application case analysis
- Business value assessment

### academic (Academic Rigor)

Focus on theoretical foundations, academic rigor, peer review, citation analysis.

Use cases:
- Theoretical research
- Academic literature review
- Citation relationship analysis

### open_source (Open Source Spirit)

Focus on open source projects, community ecosystem, developer tools, collaboration patterns.

Use cases:
- Open source project discovery
- Community dynamic tracking
- Developer tool exploration

## Search Channels

### arxiv

Academic literature search, supports LaTeX syntax and arXiv search operators.

### web

Web search, supports Google Search Operators (e.g., `filetype:pdf`, `site:edu`).

### rss

RSS subscription source search, suitable for tracking updates from specific websites or blogs.

## Data Flow

```
PlanetContext (Theme + Values)
    ↓
PromptManager (Build prompts)
    ↓
LLMClient (Call LLM)
    ↓
Expander (Parse response)
    ↓
SSEOutput (Search instructions)
```
