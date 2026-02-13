# Hints when working with wire mock

## Valid JSON Search

When creating or modifying wiremock mappings use the following syntax for JSON value lookups

```
{
    "request": {
    "method": "POST",
    "url": "/brock_solutions.quality_recipe.v1.QualityRecipeService/GetQualityRecipe",
    "bodyPatterns": [
        {
            "equalToJson": "{ \"quality_recipe_id\": 1 }"
        }
    ]
    },
    "response": {
        "status": 200,
        "bodyFileName": "QualityRecipe_1.json"
    }
}
```
