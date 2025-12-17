┌────────────────────────────────────────────────────────────────┐
│                    AGENT EXECUTION FLOW                         │
├────────────────────────────────────────────────────────────────┤
│                                                                 │
│  INPUT: ResearchState                                           │
│  ┌─────────────────────────────────────────────────────┐       │
│  │ query: "LLM efficiency techniques"                  │       │
│  │ papers: []                                          │       │
│  │ insights: []                                        │       │
│  │ report: ""                                          │       │
│  └─────────────────────────────────────────────────────┘       │
│                         │                                       │
│                         ▼                                       │
│  ┌─────────────────────────────────────────────────────┐       │
│  │          RESEARCHER AGENT                            │       │
│  ├─────────────────────────────────────────────────────┤       │
│  │ Role: Find relevant sources                         │       │
│  │ Tools: search_arxiv, search_wikipedia               │       │
│  │ Process:                                             │       │
│  │  1. Call search_arxiv("LLM efficiency")            │       │
│  │  2. Get 5 academic papers                           │       │
│  │  3. Call search_wikipedia("LLM")                    │       │
│  │  4. Add papers to state.papers[]                    │       │
│  └─────────────────────────────────────────────────────┘       │
│                         │                                       │
│                         ▼                                       │
│  State: papers = [Paper1, Paper2, Paper3, Paper4, Paper5]      │
│                         │                                       │
│                         ▼                                       │
│  ┌─────────────────────────────────────────────────────┐       │
│  │          ANALYZER AGENT                              │       │
│  ├─────────────────────────────────────────────────────┤       │
│  │ Role: Synthesize findings                           │       │
│  │ Tools: None (pure reasoning)                         │       │
│  │ Process:                                             │       │
│  │  1. Read all papers from state                      │       │
│  │  2. Identify patterns and themes                    │       │
│  │  3. Find contradictions/gaps                        │       │
│  │  4. Add insights to state.insights[]                │       │
│  └─────────────────────────────────────────────────────┘       │
│                         │                                       │
│                         ▼                                       │
│  State: insights = ["Insight1", "Insight2", "Insight3"]        │
│                         │                                       │
│                         ▼                                       │
│  ┌─────────────────────────────────────────────────────┐       │
│  │          WRITER AGENT                                │       │
│  ├─────────────────────────────────────────────────────┤       │
│  │ Role: Create structured report                      │       │
│  │ Tools: None (pure generation)                        │       │
│  │ Process:                                             │       │
│  │  1. Read insights + papers                          │       │
│  │  2. Structure 500-word summary                      │       │
│  │  3. Add citations [1], [2], etc.                    │       │
│  │  4. Set state.report                                │       │
│  └─────────────────────────────────────────────────────┘       │
│                         │                                       │
│                         ▼                                       │
│  OUTPUT: Complete ResearchState                                 │
│  ┌─────────────────────────────────────────────────────┐       │
│  │ report: "500-word summary with citations"           │       │
│  └─────────────────────────────────────────────────────┘       │
│                                                                 │
│  Total Execution: ~8-12s | ~10,500 tokens | ~$0.018 (GPT-4o-mini)│
└────────────────────────────────────────────────────────────────┘

