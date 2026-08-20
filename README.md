# AI SQL Analytics Assistant

## Project Overview

AI SQL Analytics Assistant is an enterprise-style portfolio project that enables users to ask business questions in natural language. The application converts English questions into SQL queries using Google's Gemini 3.5 Flash model, executes them securely on a PostgreSQL database, and presents interactive visualizations along with AI-generated business insights.

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

- Natural Language to SQL conversion using Gemini AI
- Secure SQL validation and controlled query execution
- PostgreSQL relational database integration
- AI-powered business analytics
- Automated KPI generation from query results
- Interactive data visualization using Plotly
- Automatic chart selection based on query results
- AI-generated business insights
- Automated analytical findings from verified query results
- Time-series trend analysis
- Category and numerical comparison analysis
- Interactive Business Dashboard
- Dynamic dashboard filtering by date, category, state and order status
- Filter-aware KPI calculations
- Sales trend and category performance analysis
- Geographic sales analysis by state
- Order status distribution analysis
- Top product and top customer analysis
- Filtered dashboard data export to Excel
- Persistent dashboard filter state across Streamlit interactions
- Modular service-oriented architecture
- Separation of AI, database, dashboard and UI layers
- Production-style project structure
- Unit and integration testing
- Streamlit-based interactive application


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
| AI Model | Gemini 3.5 Flash |
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
│   ├── insight_client.py
│   ├── insight_engine.py
│   ├── insight_generator.py
│   ├── insight_prompt.py
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
├── dashboard/
│   ├── chart_service.py
│   ├── dashboard_controller.py
│   ├── export_service.py
│   ├── filters.py
│   ├── filter_options.py
│   ├── kpi_service.py
│   └── service.py
│
├── ui/
│   ├── components.py
│   ├── dashboard.py
│   ├── dashboard_filters.py
│   ├── layout.py
│   └── sidebar.py
│
├── tests/
│   ├── test_db_connection.py
│   ├── test_database_executor.py
│   ├── test_gemini_connection.py
│   ├── test_insight_client.py
│   ├── test_insight_engine.py
│   ├── test_insight_generator.py
│   ├── test_insight_prompt.py
│   ├── test_query_engine.py
│   ├── test_sql_validator.py
│   │
│   ├── test_dashboard_filters.py
│   ├── test_dashboard_filter_options.py
│   ├── test_dashboard_service.py
│   ├── test_dashboard_controller.py
│   ├── test_dashboard_kpi_service.py
│   ├── test_dashboard_chart_service.py
│   └── test_dashboard_export_service.py
│
├── docs/
│
├── .env.example
├── .gitignore
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
- ✅ Sprint 7 – AI Business Insights & Report Generation
- ✅ Sprint 7.5 – Interactive Business Dashboard
- ⏳ Sprint 8 – Deployment & Production Readiness
---

## Current Features

- ✅ Natural Language to SQL using Gemini AI
- ✅ Secure SQL Validation
- ✅ PostgreSQL Integration
- ✅ AI Query Engine
- ✅ End-to-End AI Pipeline
- ✅ Pandas DataFrame Output
- ✅ Automatic Chart Selection
- ✅ Bar, Line and Pie Chart Generation
- ✅ Query-Level KPI Generation
- ✅ Verified Analytical Findings
- ✅ Time-Series Analysis
- ✅ AI-Generated Business Insights
- ✅ Streamlit Insight Integration
- ✅ Graceful Handling of Insufficient Analytical Data

### Interactive Business Dashboard

- ✅ Interactive Dashboard Filters
- ✅ Date Range Filtering
- ✅ Category Filtering
- ✅ State Filtering
- ✅ Order Status Filtering
- ✅ Filter-Aware Dashboard Data Loading
- ✅ Persistent Dashboard Filter State
- ✅ Dashboard KPI Cards
- ✅ Total Sales, Orders, Customers and Units Sold KPIs
- ✅ Average Order Value Calculation
- ✅ Sales Trend Visualization
- ✅ Sales by Category Visualization
- ✅ Sales by State Visualization
- ✅ Order Status Distribution
- ✅ Top Products by Sales
- ✅ Top Customers by Sales
- ✅ Filtered Dashboard Excel Export

### Engineering & Quality

- ✅ Modular Enterprise Architecture
- ✅ Separation of AI, Dashboard, UI and Database Layers
- ✅ Dedicated Dashboard Services
- ✅ Reusable Chart Service
- ✅ Dedicated KPI Service
- ✅ Dedicated Export Service
- ✅ Unit & Integration Tests
- ✅ Filter-State Persistence Across Streamlit Reruns

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
- Chart visualization verified with real query results

### ✅ Sprint 7 – AI Business Insights
The AI Business Insights layer has been implemented as a separate modular pipeline that analyzes verified query results before sending them to Gemini.

## Analytical Findings
- Basic statistical analysis implemented
- Numeric result analysis implemented
- Total and average calculations implemented
- Highest and lowest value detection implemented
- Category comparison analysis implemented
- Distribution analysis implemented
- Time-series analysis implemented
- Percentage change calculations implemented
- Insufficient-data handling implemented
- AI Insight Layer
- Dedicated insight prompt builder implemented
- Verified analytical findings passed to the AI instead of raw query results
- Dedicated Gemini insight client implemented
- Insight engine implemented to orchestrate the complete AI insight workflow
- AI-generated business insights integrated into Streamlit
- Category comparisons handled using appropriate comparison language
- Time-based increases and decreases handled separately from category comparisons
- AI instructed not to invent unsupported numbers, causes, trends, or business explanations
- Data limitations explicitly communicated when analytical findings are insufficient

## Insight Workflow

```
Query Result DataFrame
          │
          ▼
   Insight Generator
          │
          ▼
Verified Analytical Findings
          │
          ▼
    Insight Prompt
          │
          ▼
   Gemini Insight Client
          │
          ▼
    Insight Engine
          │
          ▼
 AI Business Insight
          │
          ▼
   Streamlit Dashboard
```

## Completed AI Insight Architecture

The project now separates SQL generation from business insight generation.

```
                         User Question
                              │
                              ▼
                       ┌─────────────┐
                       │ Query Engine│
                       └──────┬──────┘
                              │
                              ▼
                       SQL Generation
                              │
                              ▼
                       SQL Validation
                              │
                              ▼
                       PostgreSQL DB
                              │
                              ▼
                       Pandas DataFrame
                              │
                 ┌────────────┴────────────┐
                 │                         │
                 ▼                         ▼
          Chart Generator          Insight Generator
                 │                         │
                 ▼                         ▼
        Interactive Chart        Verified Findings
                                           │
                                           ▼
                                   Insight Prompt
                                           │
                                           ▼
                                  Gemini Insight Client
                                           │
                                           ▼
                                     Insight Engine
                                           │
                                           ▼
                                  Business Insight
                                           │
                                           ▼
                                    Streamlit UI

```

This separation allows analytical calculations to remain deterministic and verifiable while Gemini is used primarily for natural-language interpretation and business communication.

---

---

### ✅Sprint 7.5 – Interactive Business Dashboard

An interactive Business Dashboard layer was implemented as a separate modular pipeline to provide filtered business analysis and reusable dashboard visualizations from verified PostgreSQL data.

## Dashboard Architecture

The Business Dashboard was implemented using a modular architecture with separate responsibilities for:

- Dashboard filter state management
- Filter option retrieval
- Filtered dashboard data loading
- Dashboard KPI calculation
- Dashboard-specific chart generation
- Dashboard export functionality
- Streamlit dashboard presentation

## Dashboard Filters

- Interactive date range filtering implemented
- Category filtering implemented
- State filtering implemented
- Order status filtering implemented
- Filter selections represented using a dedicated `FilterContext`
- Filter options dynamically retrieved from PostgreSQL
- Filtered dashboard data loaded based on the selected filter context
- Dashboard filter state preserved across Streamlit reruns
- Reset filter functionality implemented
- Empty-result handling implemented

## Dashboard KPIs

Dedicated dashboard KPI calculations implemented independently from the query-level KPI engine.

The dashboard KPI layer provides:

- Total Sales
- Total Orders
- Total Customers
- Units Sold
- Average Order Value

KPIs are calculated deterministically from the filtered dashboard dataset.

## Dashboard Visualizations

Dedicated Plotly chart services implemented for:

- Sales Trend
- Sales by Category
- Sales by State
- Order Status Distribution
- Top Products by Sales
- Top Customers by Sales

Charts are generated from the filtered dashboard dataset and remain independent from the Streamlit presentation layer.

## Dashboard Data Architecture

The Business Dashboard uses a dedicated dashboard dataset containing:

- Order information
- Customer information
- Product information
- Category and sub-category information
- Brand information
- Geographic information
- Order status
- Quantity
- Unit price
- Line total
- Order date

## Dashboard Export

Dashboard export functionality implemented using Excel.

The export functionality supports:

- Export of filtered dashboard data
- Excel workbook generation
- Streamlit Excel download
- Filter-aware dashboard export
- Persistent dashboard filters during file download

## Streamlit Integration

The Business Dashboard was integrated into the existing Streamlit application without disturbing the previously implemented AI SQL workflow.

The application flow now includes:

1. Business question input
2. AI-generated SQL
3. Query execution
4. Query result display
5. Query-level KPIs
6. Query-level visualizations
7. AI-generated business insight
8. Interactive Business Dashboard
9. Dashboard filters
10. Dashboard KPIs
11. Dashboard visualizations
12. Filtered dashboard export

## Dashboard Testing

Unit tests implemented for:

- Dashboard filter context
- Filter option retrieval
- Dashboard data loading
- Dashboard controller
- Dashboard KPI calculations
- Dashboard chart services
- Dashboard Excel export

All implemented dashboard components were tested independently before Streamlit integration.

### ⏳ Sprint 8 – Deployment & Production Readiness
- Application deployment
- Environment/secrets configuration
- Production testing
- Production error handling
- Performance optimization
- Final documentation
