# Haul Co

Dispatch and ticket management for a hauling and billing management. Drivers submit photos of the tickets they collect on a trip (scale tickets, fuel receipts, and so on), each ticket is linked to a job, and the back office reviews them and bills the customer. An Object Character Recognition Model is used to determine certain aspects of each ticket and if any discrepancies are found, human review is initiated. 

> **Status:** early development (terminal v1.0b). 

## Features

**Implemented**

- **Email and password authentication** (register, login, logout) with Flask-Login
- **Driver dashboard** with recent ticket submissions, tickets pending, active jobs, and ability to submit new tickets for review
- **Administration dashboard** with the ability to create & assign new jobs
    - Admins can view staff members and other admins
    - More functionality to be added:
        - Ticket review (artifacts/issues detected by OCR)
        - Archived tickets
        - Jobs (current & old)
        - Vehicle management
- **Ticket upload modal** (ticket type, special instructions, job selection, image upload)
- **Ticket review status tracking**
    - *Only on frontend* - review functionality needs to be implemented on the admin panel
- **Data models** for users, tickets, jobs, and vehicles

**Planned**

*Subject to change.* This will continually be updated over time as features get pushed to production, but also with new features that will need to be added. 

- Email verification with expiring links
- Email notifications for:
    - Ticket filing issues
    - Ticket status updates
    - Billing notices
    - Job completion
    - Payouts
    - Automatic, itemized invoices
    - Separate revenue (customer billing) and cost (driver or owner-operator pay) calculations per ticket
    - _etc..._
- OCR for tickets
- Mapping information read from tickets to database
- Flagging and review of tickets for site admins
- Basic user settings
    - Email
    - Password
    - Name (first + last)
    - Vehicle management by owner/operators (maybe?)
    - Vehicle management by admins (maybe?)
- Cost calculations (this will take time to create)
    - Fuel surcharges
    - Maintenance
    - Pay Periods
    - Accounts Recievable / Payable
- Emailing invoices to companies requesting transport services
- Tweaking/fixing object relations in the database
- Permenant database configuration within a hosting service
    - Most likely will be switching to Postgres for prod to avoid headaches
- When I have time I hope to add API capabilities for expansion of the platform - like mobile support - with the same framework

With this system I hope to have some sort of dashboard to manage and configure each job with tickets mapped to them so that everyone that needs to be payed can be payed and everyone that owes Haul Co money pays Haul Co. More of a money management dashboard per say.

## Tech Stack

| Layer | Tool |
| --- | --- |
| Backend | Flask |
| ORM | Flask-SQLAlchemy |
| Migrations | Flask-Migrate (Alembic) |
| Database | SQLite (development) |
| UI | Tabler, Chart.js (loaded from jsDelivr) |

## Roadmap & Current Progress

`TBD`

## Artificial Intelligence

_Majority of the code within this repository is written by myself with the guidance and assistance from **some** artifical intelligence. I do not condone passing artificial intelligence off as one's own work._

Written by artificial intelligence:
- ORM foreign relationships
- OCR ticket review

I've read the SQL-Alchemy documentation quite a few times and I actually appreciate how nicely documented it is. I often have trouble remembering certain relationships and how they're defined, therefore some of the foriegn key relationships within the database have been curated with the help of Claude.

I essentially tasked Claude with creating the OCR entirely. I originally was going to create it myself, but I don't have too much experience in machine learning. Additionally, most of the machine learning libraries for python are poorly documented and often written in another language other than Enlgish. I'd figured I'd had enough tasked for myself already in terms of the website itself so I've taken what Claude has produced and tailored it to work seamlessly with what I've created so far.

#### *This repository will remain open until I decide otherwise.*