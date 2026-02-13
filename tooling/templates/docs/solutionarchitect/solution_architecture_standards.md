# Solution Architecture Standards and Best Practices

## Objective

Produce system designs and software implementations that are concise, usable, and complete.
Designs must be based on Project Requirements Documents (PRD) or functional definitions.
Adhere to the design paradigms that already exist within the codebase.

## Design Deliverables

Output documentation should be placed in `docs/detailed-design`.

### Backend Services

When reviewing system requirements, identify new Backend Services.
For each service, provide:

- **Service Definition**: Specific responsibilities and data domain.
- **Database Entities**: Complete list of entities based on requirements (conceptual, not necessarily specific fields).

### API Endpoints

Construct a list of API endpoints.
For each endpoint:

- **Concrete Definition**: What it is expected to perform.
- **Message Details**: Input/output requirements (potentially Protobuf messages).
- **Simplicity**: Keep endpoints atomic and payloads simple for the calling system.

### Key Visualizations

When requirements involve UI, identify Key Visualizations.
For each visualization:

- **Detailed Description**: Purpose is to enable UI mockup creation.
- **Concise Purpose and Capability**.
- **Service Dependencies**.

### Technical Analysis

- **Technology Stack**: Review existing stack; add new elements only when strictly necessary.
- **Technical Challenges**: Present a well-composed list of challenges the new requirements present.
- **Dataflow Diagrams**: Provide Mermaid diagrams for API calls for key use cases, maintaining existing patterns.
- **Assumptions**: Include a section for assumptions made during design.
- **Prioritize Native Solutions**: Leverage built-in capabilities of existing frameworks; minimize new dependencies.

## Documentation Best Practices

- **Clarity and Brevity**: Write in simple, concise language to minimize ambiguity.
- **Consistency**: Use consistent formatting, terminology, and structure.
- **Visual Aids**: Use Mermaid for diagrams and tables for complex concepts.
- **Content Accuracy**: Ensure information is correct, up-to-date, and referenced.
- **Readability**: Use lists, tables, and other techniques.
- **Content Re-organization**: Reorganize sections so concepts read as complete thoughts.

## Existing Technical Details

### Solution Architecture

The frontend application follows a structured component architecture based on React with Redux for state management.
The application organizes UI elements into three categories:

1. **Pages** - Top-level route components that compose the application layout
2. **Features** - Reusable domain-specific components (e.g., headers, menus)
3. **Widgets** - Generic UI elements that can be used across multiple features

The backend follows a domain-driven microservices architecture where each service:

1. **Owns a specific business domain**: Each service encapsulates a distinct business capability with clearly defined boundaries
2. **Maintains autonomous data storage**: Services own their data models and persistence mechanisms
3. **Exposes standardized interfaces**: All services implement consistent API patterns for interoperability

#### Database Strategy

- Each service utilizes Entity Framework Core with dedicated DbContext classes in the `Data` directory
- Services connect to SQL Server databases with service-specific schemas or tables
- Data models are defined in the `Models` directory and mapped to database entities
- Entity Framework migrations are managed through SQL scripts in the `sql` directory

### Libraries and Frameworks

#### Frontend Technologies

- React.js with hooks for UI development
- Redux Toolkit for state management
- Material UI for consistent component design
- Vite for fast development and builds
- gRPC-Web for API communication
- SignalR for real-time updates
- MSW for API mocking during development

#### Backend Technologies

- .NET for microservice implementation
- gRPC for efficient service communication
- Entity Framework Core for data access
- SQL Server for relational data storage
- RabbitMQ for message queuing
- Camel for integration workflows
- Traefik for API gateway and routing
- Envoy for protocol translation
- SignalR for real-time backend-to-frontend communication

#### Infrastructure Technologies

- Docker for containerization
- Docker Compose for local development
- Kubernetes for production orchestration
- Azure DevOps for CI/CD pipelines
- MkDocs for documentation

#### Frontend Integration

Services interact with the frontend through:

1. **API Gateway layer**: Consolidates service endpoints for frontend consumption
   - Uses gRPC Gateway to translate gRPC to REST APIs
   - Traefik routes requests to appropriate services
   - Envoy provides additional protocol translation as needed
2. **WebSocket notifications**: For real-time updates and events
   - SignalR hubs for bi-directional communication
   - Notification messages for real-time updates
3. **Authorization middleware**: Enforces consistent security across all service boundaries

### Service Communication

Services communicate through:

1. gRPC for service-to-service communication
2. REST APIs via gRPC Gateway for external clients
3. Event-driven patterns using Sagas for complex workflows

#### Event-Driven Communication

- Services publish domain events to notify of state changes
- Event subscribers coordinate cross-service business processes
- Saga pattern orchestrates distributed transactions across service boundaries
- SignalR is used for real-time communication between services and frontend
