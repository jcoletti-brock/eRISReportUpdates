# .NET gRPC Implementation Standards

This document defines the standards for implementing gRPC services in .NET (C#) for Brock Solutions projects.

---

## Service Structure

- **Proto files** are versioned and stored under `Api/Protos/<namespace>/<servicename>/v#`.
- gRPC service implementations reside in `Main/GrpcServices`.
- Business logic is implemented in `Main/Services` and referenced by gRPC services.

## Method Signatures

- Method names in implementation **must match** RPC method names in the proto file.
- All methods **must be async** and return `Task<ResponseType>`.
- Method parameters must include the request message and `ServerCallContext`.
- For repeated fields, **add items to the collection** rather than setting directly.

```csharp
public override async Task<GetQualityRecipeResponse> GetQualityRecipe(GetQualityRecipeRequest request, ServerCallContext context)
```

## Error Handling

### Input Handling

The GRPC service implement is not responsible for error handling the inputs.
eg. This type syntax is not required.

```csharp
 long? planId = string.IsNullOrEmpty(request.MeasurementPlanId) ? null : long.Parse(request.MeasurementPlanId);
 long? equipmentId = string.IsNullOrEmpty(request.EquipmentId) ? null : long.Parse(request.EquipmentId);
```

### Exceptions

- Use `RpcException` for gRPC error responses. Map domain/service errors to appropriate gRPC status codes.
- Include meaningful error messages and details in exceptions.
- Log errors using the injected logger; do not expose sensitive details to clients.
- Be specific in the exceptions handling such as ArgumentNullException and FormatException when parsing inputs.
- **Do NOT use general `catch (Exception)` blocks in gRPC service implementations.**
  - Only catch and handle specific exceptions (e.g., `ArgumentNullException`, `FormatException`, `KeyNotFoundException`, etc.) that are expected and can be mapped to a specific gRPC status code.
  - Let all other exceptions propagate naturally so they are logged and handled by the global exception handler/middleware.
  - This ensures that only known, expected error conditions are mapped to gRPC error responses, and unexpected errors are surfaced for investigation.
- Example:

```csharp
try
{
    // ...service / transform logic...
}
catch (ArgumentNullException ex)
{
    _logger.LogWarning(ex, "Input Arguments Invalid");
    throw new RpcException(new Status(StatusCode.InvalidArgument, "Input Arguments Invalid"));
}
catch (FormatException ex)
{
    _logger.LogWarning(ex, "Input Format Invalid");
    throw new RpcException(new Status(StatusCode.InvalidArgument, "Input Format Invalid"));
}
// Do NOT add: catch (Exception ex) { ... }
```

## Naming & Conventions

- Follow C# and .NET naming conventions.

## Model-to-Proto Mapping

- Map Entity Framework model objects to proto response objects in a dedicated mapping method or extension method.
- Do not expose entity models directly to the API layer.
- Use clear, explicit property assignments; avoid automappers unless justified for complex mappings.
- For collections, use LINQ's `Select` to project model lists to proto lists.
- Handle nulls and optional fields explicitly to avoid runtime errors.
- Example:

```csharp
private static QualityRecipeResponse MapToProto(QualityRecipe model)
{
    var response = new QualityRecipeResponse
    {
        Id = model.Id,
        // ...other property mappings...
    };
    response.RecipeItems.AddRange(model.RecipeItem.Select(MapToProto));
    return response;
}

private static QualityRecipe MapFromProto(QualityRecipeResponse proto)
{
    var model = new QualityRecipe
    {
        Id = proto.Id,
        // ...other property mappings...
    };
    model.RecipeItems = proto.RecipeItem.Select(MapFromProto).ToList();
    return model;
}
```
