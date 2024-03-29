# python-web-examples
Examples for web development with Python.

Reference: https://www.cosmicpython.com/book/preface.html

# Architecture
<img src="img/architecture.png" width="600">

## Controller Layer
* Handling the user request and response.
* Passing the request to the service layer.
* Should not contain any business logic.
* Should not interact with the repository and domain model layer.
## Service Layer
* Contains the business logic.
* Interacts with the repository layer.
## Repository Layer
* Interacts with the database.
## DTO (Data Transfer Object)
* Object that is used to encapsulate data, and send it from one subsystem of an application to another.
## DAO (Data Access Object)
* Object that provides an abstract interface to some type of database or other persistence mechanism.

# Basic
* domain
  * service
  * repository
  * domain model
* exceptions
* constants
* testing
  * unit
  * integration
* worker
* web response
  * external
  * internal debug
* api documentation
* data migration
* environment configuration
* testing, running environment
* CI/CD pipeline, scripts
* package management
* linter, formatter, typo check configuration

# Domain Structure
* Domain
  * Service
    * The workflow of the business logic.
    * Validate the workflow.
  * Domain model
    * The rules of the business logic.
    * Define the entity and the value object.
    * Validate the entity and the value object.
  * Repository
    * CRUD operation of the database.
