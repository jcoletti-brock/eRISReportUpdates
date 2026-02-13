# Brock Solutions Service Architecture Code Generation Guidelines

## Service Structure

Consider the following structure when working with Service code in this workspace:

- `Api/Protos` contains proto files for gRPC services.
- Proto files are stored as versions under the following structure:
  - `Api/Protos/<namespace>/<servicename>/v#`
- `Main/Services` contains the main service code.
- `Main/Data` contains the database context and data access code.
- `Main/GrcpServices` contains gRPC api implementations.
- `Main/Models` contains entity models.
- `Main/Services` contains the service implementations reference by the api.
- `Main/Consumers` contains the consumers for message queues.
- `Main/sql` contains the liquibase files for database creation and migration.

## Entity Framework Models

Consider the following when working with Entity Framework models in this workspace:

- Entity models are auto-generated and should not be modified directly
- Models are partial classes - extend them with `.UDT.cs` files instead of modifying the original
- Use the `[NotMapped]` attribute for any properties not directly mapped to database columns
- Follow Entity Framework conventions for database relationships

## gRPC Implementation

- Method names in implementation should match RPC method names in proto
- All methods should be async and return Task<ResponseType>
- Parameters should include the request message and ServerCallContext
- For repeated fields, add items to the collection rather than setting directly

## Services Logic

- `Main/Services` contains the service implementations reference by the api.
- This is where the business logic for the serverice should be implemented.
