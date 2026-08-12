# AI SQL Analytics Assistant

## Project Overview

AI SQL Analytics Assistant is an enterprise-style portfolio project that enables users to ask business questions in natural language. The application converts English questions into SQL queries using Google's Gemini 2.5 Flash model, executes them securely on a PostgreSQL database, and presents interactive visualizations along with AI-generated business insights.

The project follows a production-style architecture with modular components for AI, database management, visualization, and analytics.
---

## Objectives

- Convert Natural Language into SQL
- Execute SQL securely
- Display Interactive Charts
- Generate AI Business Insights
- Build a production-style analytics application

---

## Features

- Natural Language to SQL conversion
- Secure SQL execution
- PostgreSQL relational database
- AI-powered business analytics
- Interactive dashboards
- Data visualization with Plotly
- Modular enterprise architecture
- Production-style project structure

---------

## Database

The application currently includes the following relational tables:

- Customers
- Categories
- Products
- Orders
- Order Items
- Payments
- Returns

The database has been populated with realistic synthetic business data generated using Python and Faker.

------------

## Planned Tech Stack

| Layer | Technology |
|--------|------------|
| Frontend | Streamlit |
| Backend | Python |
| Database | PostgreSQL |
| AI Model | Gemini 2.5 Flash |
| LLM Framework | LangChain |
| ORM | SQLAlchemy |
| Charts | Plotly |
| Version Control | Git & GitHub |

---

## Current Project Structure

```text
AI_SQL_Analytics_Assistant/
│
├── ai/
│   ├── database_context.py
│   ├── gemini_client.py
│   ├── prompt_builder.py
│   ├── query_engine.py
│   ├── sql_generator.py
│   └── sql_validator.py
│
├── database/
│   ├── connection/
│   │   └── db_connection.py
│   ├── schema/
│   ├── seed/
│   └── database_executor.py
│
├── docs/
│
├── tests/
│   ├── test_db_connection.py
│   ├── test_database_executor.py
│   ├── test_gemini_connection.py
│   ├── test_query_engine.py
│   └── test_sql_validator.py
│
├── .env.example
├── README.md
├── requirements.txt
└── main.py
```
---

## Roadmap

- ✅ Sprint 0 – Project Initialization
- ✅ Sprint 1 – Planning & Architecture
- ✅ Sprint 2 – Database Setup & Schema
- ✅ Sprint 3 – Database Seeding
- ✅ Sprint 4 – AI Backend
  - Gemini Integration
  - Database Context
  - Prompt Builder
  - SQL Generator
  - SQL Validator
  - Database Executor
  - Query Engine
  - End-to-End Integration Tests
- ✅ Sprint 5 – Streamlit Dashboard
- ✅ Sprint 6 – Interactive Charts & Visualizations
- 🚀 Sprint 7 – AI Business Insights & Report Generation
- ⏳ Sprint 8 – Deployment & Production Readiness
---

## Current Features

- ✅ Natural Language to SQL using Gemini AI
- ✅ Secure SQL Validation
- ✅ PostgreSQL Integration
- ✅ AI Query Engine
- ✅ End-to-End AI Pipeline
- ✅ Pandas DataFrame Output
- ✅ Modular Enterprise Architecture
- ✅ Unit & Integration Tests

-----

## Project Status

### ✅ Sprint 0 – Project Initialization
- Project folder structure created
- Git repository initialized
- Virtual environment configured
- Initial documentation created

### ✅ Sprint 1 – Planning & Architecture
- Business requirements documented
- Database schema designed
- ER diagram completed
- System architecture documented

### ✅ Sprint 1.5 – Version Control
- Git repository connected to GitHub
- Main branch configured
- Initial project published

### ✅ Sprint 2 – Database Setup
- PostgreSQL 17 installed
- pgAdmin configured
- Database created
- Database schema implemented
- Constraints added
- Indexes created

### ✅ Sprint 3 – Database Seeding
- Customers seeded
- Categories seeded
- Products seeded
- Orders seeded
- Order Items seeded
- Payments seeded
- Returns seeded
- All seed scripts verified

### ✅ Sprint 4 – AI Backend
- Gemini API integrated
- Database context module created
- Prompt builder implemented
- SQL Generator implemented
- SQL Validator implemented
- Database Executor implemented
- Query Engine implemented
- End-to-End AI pipeline completed
- Unit tests completed
- Integration tests completed
- End-to-End backend pipeline verified

## Completed Backend Workflow

The backend is fully functional and follows a modular architecture.

```
Natural Language Question
            │
            ▼
      Query Engine
            │
            ▼
     Prompt Builder
            │
            ▼
      Gemini 3.5 Flash
            │
            ▼
      SQL Generator
            │
            ▼
      SQL Validator
            │
            ▼
    Database Executor
            │
            ▼
      PostgreSQL
            │
            ▼
    Pandas DataFrame
```

This backend has been completely implemented and tested before building the Streamlit frontend.


### ✅ Sprint 5 – Streamlit Dashboard
- Streamlit application created
- Professional dashboard layout implemented
- Sidebar implemented
- Business question input implemented
- Query execution integrated with backend
- Generated SQL displayed
- SQL results displayed in interactive tables
- CSV download implemented
- Error and warning handling implemented
- Component-based UI architecture implemented

### ✅ Sprint 6 – Interactive Visualizations
- Chart generator module implemented
- Automatic chart type selection implemented
- Bar charts implemented
- Line charts implemented
- Pie charts implemented
- Numeric and categorical column detection implemented
- Date/time column detection implemented
- Distribution analysis implemented for pie-chart selection
- Chart generation integrated with Streamlit
- Chart generator unit tests completed

### 🚧 Sprint 7 – AI Business Insights
- AI-generated business insights
- Key trend identification
- Anomaly/highlight detection
- Natural-language summary of query results

### ⏳ Sprint 8 – Deployment
- Application deployment
- Environment/secrets configuration
- Production testing
