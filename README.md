# Bank Account Manager

Welcome to the Bank Account Manager project! This application enables users to create a bank account and perform basic banking operations such as deposits, withdrawals, and transfers in a user-friendly way. Built using SQLAlchemy 2.0 ORM for database management and customtkinter for a sleek, modern GUI, this project offers a robust solution for managing personal finances.

## Features

- **Account Creation:** Users can sign up for a new bank account.
- **Deposits:** Deposit money into your account with ease.
- **Withdrawals:** Withdraw money from your account.
- **Transfers:** Transfer money between accounts securely.
- **Flexible Database Support:** Choose between PostgreSQL or MySQL for database management depending on your preference.
- **User-Friendly GUI:** Built with customtkinter, the interface is intuitive and easy to navigate.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- [Docker](https://docs.docker.com/get-docker/)
- [Micromamba](https://mamba.readthedocs.io/en/latest/installation.html)
- [Taskfile](https://taskfile.dev/installation/)

## Getting Started

To get your Bank Account Manager running, follow these steps:

### 1. Clone the repository

Clone this repository to your local machine using:

```bash
git clone https://github.com/Sule26/bank-account-manager.git
cd bank-account-manager
```

### 2. Set the enviroment

Use micromamba to set the enviroment running the task:

```bash
task env:set
```

### 3. Choose your database and start the corresponding docker container

Choose the database option (MySQL or PostgreSQL) and run the corresponding task

```bash
# Start MySQL
task mysql:up
# Start PostgreSQL
task postgres:up
```

### 4. Generate fake data on database (optional)

Use faker lib to generate fake data on database in order to make some tests

```bash
task generate:schemas
```

### 5. Run the application

Finally, you can run the application

```bash
task app
```
