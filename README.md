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

```
AI_SQL_Analytics_Assistant/
│
├── ai/
├── database/
│   ├── connection/
│   ├── schema/
│   └── seed/
├── docs/
├── tests/
├── .env.example
├── README.md
├── requirements.txt
└── main.py
```
------------

## Roadmap

- ✅ Sprint 0 – Project Initialization
- ✅ Sprint 1 – Planning & Architecture
- ✅ Sprint 2 – Database Design
- ✅ Sprint 3 – Database Seeding
- 🚀 Sprint 4 – AI SQL Generation
- ⏳ Sprint 5 – Streamlit Dashboard
- ⏳ Sprint 6 – Interactive Charts
- ⏳ Sprint 7 – AI Business Insights
- ⏳ Sprint 8 – Deployment

-----------

## Project Status

### ✅ Sprint 0 – Project Initialization
- Project folder structure created
- Git repository initialized
- Virtual environment configured
- Initial documentation created

### ✅ Sprint 1 – Planning & Architecture
- Business requirements documented
- System architecture designed
- Database schema planned
- ER diagram completed

### ✅ Sprint 1.5 – Version Control
- Git repository configured
- Initial commit completed
- Branch renamed to `main`

### ✅ Sprint 2 – Database Design & Setup
- PostgreSQL 17 installed
- pgAdmin configured
- Database created
- Database schema implemented
- All tables created with constraints

### ✅ Sprint 3 – Database Seeding
- Database connection module created
- Environment variables configured
- Customer data generated
- Category data generated
- Product catalog generated
- Orders generated
- Order items generated
- Payments generated
- Returns generated
- Realistic relational dataset created

### 🚀 Sprint 4 – AI Engine (Current)
- Gemini integration (In Progress)
- Prompt engineering
- SQL generation
- SQL execution
- Query validation


