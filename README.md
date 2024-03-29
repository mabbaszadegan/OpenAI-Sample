# OpenAI-Sample Repository

This repository contains sample code and experiments related to OpenAI.

## Table of Contents
- [Introduction](#introduction)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction


OpenAI-Sample is a project that explores the capabilities of the OpenAI platform through sample code and experiments. It provides a hands-on experience with OpenAI's powerful tools and technologies.

### Key Features
- **Database Interaction:** Execute queries on a database and retrieve results seamlessly within the project.
- **Code Samples:** Browse through a variety of code snippets demonstrating how to interact with OpenAI's API.
- **Experiments:** Explore experimental implementations showcasing the potential applications of OpenAI in different domains.
- **Free Trial:** Experience the capabilities of OpenAI by obtaining a free API key and testing the project for up to three months.


## Getting Started

Provide instructions on how to get the project up and running on a local machine. Include any dependencies or prerequisites.
This repository requires obtaining an API key from OpenAI before use. For testing purposes, you can utilize a free account for up to three months.

1. Obtain an API key from OpenAI by signing up for a free account (https://openai.com).
2. Clone this repository to your local machine:

```bash
git clone https://github.com/mabbaszadegan/OpenAI-Sample.git
cd OpenAI-Sample
py -m venv ./venv
.\venv\Scripts\activate
```

## Usage
### Create .env file
You must create a .env file for configure application

```bash
# Example .env file
api_secret = "[your-api-key (https://platform.openai.com/api-keys)]"
sql_schema = "
CREATE TABLE Orders (
      OrderID int,
      CustomerID int,
      OrderDate datetime,
      OrderTime varchar(8),
      PRIMARY KEY (OrderID)
    );
    
    CREATE TABLE OrderDetails (
      OrderDetailID int,
      OrderID int,
      ProductID int,
      Quantity int,
      PRIMARY KEY (OrderDetailID)
    );
    
    CREATE TABLE Products (
      ProductID int,
      ProductName varchar(50),
      Category varchar(50),
      UnitPrice decimal(10, 2),
      Stock int,
      PRIMARY KEY (ProductID)
    );
    
    CREATE TABLE Customers (
      CustomerID int,
      FirstName varchar(50),
      LastName varchar(50),
      Email varchar(100),
      Phone varchar(20),
      PRIMARY KEY (CustomerID)
    );
" 
```

```bash
# Example usage commands or code snippets
flask --app main run   
```
## Contributing

We appreciate your interest in contributing to OpenAI-Sample! Your contributions help improve the project and make it more valuable for the community.

### How to Contribute

1. **Fork the Repository:**
   Fork the OpenAI-Sample repository to your own GitHub account.

2. **Clone the Repository:**
   Clone the repository from your fork to your local machine:

   ```bash
   git clone https://github.com/your-username/OpenAI-Sample.git
   cd OpenAI-Sample
   ```
## License
Feel free to customize this template based on your project's specifics. Add more sections or details as needed.
