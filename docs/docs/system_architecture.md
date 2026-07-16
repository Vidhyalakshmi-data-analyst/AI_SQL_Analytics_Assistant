# System Architecture

## Overview

The AI SQL Analytics Assistant follows a layered architecture that separates the user interface, AI processing, business logic, and database.

```text
                    +----------------------+
                    |      User            |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    |  Streamlit Frontend  |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    | Python Application   |
                    |  (Controller Layer)  |
                    +----------+-----------+
                               |
              +----------------+----------------+
              |                                 |
              v                                 v
+---------------------------+      +---------------------------+
| Gemini LLM (NLP → SQL)    |      | Business Logic Layer      |
+-------------+-------------+      +-------------+-------------+
              |                                 |
              +---------------+-----------------+
                              |
                              v
                 +----------------------------+
                 | SQL Validation & Security  |
                 +-------------+--------------+
                               |
                               v
                     +-----------------------+
                     | PostgreSQL Database   |
                     +-----------------------+
```

---

## Data Flow

1. User enters a question in Streamlit.
2. Python receives the request.
3. Gemini converts natural language into SQL.
4. SQL is validated before execution.
5. PostgreSQL executes the query.
6. Results are returned to Python.
7. Python formats the output.
8. Streamlit displays tables and charts.

---

## Advantages of this Architecture

- Separation of concerns
- Secure SQL execution
- Easy maintenance
- Scalable design
- AI isolated from database access
- Supports future enhancements
