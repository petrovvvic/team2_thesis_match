 GET /api/top-supervisors

  Top-Betreuer ranking (Screen 8), professors ranked by number of supervision requests received.

  ┌─────────────┬────────────────────────────────────────────────┐
  │             │                                                │
  ├─────────────┼────────────────────────────────────────────────┤
  │ Method      │ GET                                            │
  ├─────────────┼────────────────────────────────────────────────┤
  │ Path        │ /api/top-supervisors                           │
  ├─────────────┼────────────────────────────────────────────────┤
  │ Auth        │ None (public leaderboard)                      │
  ├─────────────┼────────────────────────────────────────────────┤
  │ Query param │ limit — optional, default 10, clamped to 1–100 │
  ├─────────────┼────────────────────────────────────────────────┤
  │ Response    │ application/json                               │
  └─────────────┴────────────────────────────────────────────────┘

  Examples
  - http://127.0.0.1:5050/api/top-supervisors
  - http://127.0.0.1:5050/api/top-supervisors?limit=5

  Response shape
  {
    "count": 2,
    "ranking": [
      {
        "rank": 1,
        "professor_id": 4,
        "name": "Prof. Dr. Max Profman",
        "research_areas": "ML, NLP",
        "request_count": 1
      },
      {
        "rank": 2,
        "professor_id": 2,
        "name": "Prof. Dr. Test Prof1 TestProf 1.0",
        "research_areas": "BWL",
        "request_count": 0
      }
    ] 
  } 

  Notes
  - Ordered by request_count desc, ties broken by last name (A→Z).
  - Includes professors with 0 requests (LEFT JOIN), so the full roster ranks even before any requests exist.
  - request_count only — ranking by rating isn't included (no ratings table in the schema yet; that's future work).