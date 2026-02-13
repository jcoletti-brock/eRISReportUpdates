# Testing

The backend C# projects use a combination of the following libraries to write tests. Test should follow the "[Arrange-Act-Assert](https://automationpanda.com/2020/07/07/arrange-act-assert-a-pattern-for-writing-good-tests/)" pattern wherever possible. Read more below about the different parts of this pattern. A video of someone writing a unit test can be seen [here](https://web.microsoftstream.com/video/136e7bd0-3eb6-43b3-b29a-98cbccf9b7ac){target=\_blank}. See the video for timestamps.

| Function             | Library                                       | Documentation                                    |
| -------------------- | --------------------------------------------- | ------------------------------------------------ |
| Testing Framework    | [NUnit](https://nunit.org/)                   | https://docs.nunit.org/articles/nunit/intro.html |
| Mocking              | [moq](https://github.com/moq/moq4)            | https://github.com/Moq/moq4/wiki/Quickstart      |
| Test Fixture Creator | [AutoFixture](https://autofixture.github.io/) | [AutoFixture](./autofixture)                     |

## Anatomy of a Basic Test (using real data)

```csharp linenums="1" title="TagDataServiceTests.cs"
[TestFixture] // Tells NUnit this class contains tests
public class TagDataServiceTests
{

    [OneTimeSetUp] // Tells NUnit to run this method once, before all the tests in this class are ran
    public void Init()
    {
        // AutoFixture setup
        _fixture = new Fixture()
            .Customize(new AutoMoqCustomization());

        // Setup a connection to the database
        var connectionString = "Server=127.0.0.1;Database=TestDatabase;User Id=sa;Password=bestPa!l65;";
        var contextOptions = new DbContextOptionsBuilder<NewMesContext>()
            .UseSqlServer(connectionString)
            .Options;
        // Create a context using that connection
        _context = new NewMesContext(contextOptions);
        // Create a instance of the service being tested, passing in the needed depenencies (in this case a logger and the context)
        _tagDataService = new TagDataServiceImpl(_fixture.Create<ILogger<TagDataServiceImpl>>(), _context);
    }

    [OneTimeTearDown] // Tells NUnit to run this method once, after all the tests in this class are ran
    public void Cleanup()
    {
        _context.Dispose(); // Cleanup the context
    }

    [Test] // Tells NUnit this method is a test
    public async Task WriteTag_TagExists_TagWrote()
    {
        #region Arrange

        var modelUid = _fixture.Create<long>(); // Get some random test values from Autofixture
        var typeName = _fixture.Create<string>();
        var valueLong = _fixture.Create<long>();
        _context.Tags.Add(GetTag(typeName, modelUid)); // Add some test data to the database
        _context.SaveChanges(); // Need to ensure the database is updated

        #endregion

        // Act
        _tagDataService.WriteTag(modelUid, typeName, valueLong); // Call the method being tested

        #region Asserts

        var tagValues = _context.TagValues
            .Where(tv => tv.TagU.TagTypeU.Name == typeName); // Check that the method being tested did something,
        // In this case, make sure the database has only one tag value with the random typeName from line 9
        Assert.That(tagValues, Has.Exactly(1).Items);
        // Also check that the tag value has the correct "ValueLong" value
        var value = tagValues.First();
        Assert.That(value, Has.Property(nameof(TagValue.ValueLong)).EqualTo(valueLong), "value");

        #endregion

    }

    // Convience method for creating a tag, could be replaced with AutoFixture
    private Tag GetTag(string typeName, long modelUid)
    {

        var tagType = new TagType
        {
            Name = typeName,
            RowInserted = DateTime.UtcNow,
            RowUpdated = DateTime.UtcNow
        };
        var dataType = _context.DataTypes.First();
        var tag = new Tag
        {
            Name = typeName,
            Path = typeName,
            ModelUid = modelUid,
            TagTypeU = tagType,
            DataTypeU = dataType,
            RowInserted = DateTime.UtcNow,
            RowUpdated = DateTime.UtcNow
        };
        return tag;
    }
}
```

!!! warning "Real data vs Mocking"

    The above example uses real data in the test database. This is only possible because the `_tagDataService.WriteTag` uses the database context directly. Other methods will call other services or performce GRPC calls, those methods need to be tested using Mocking instead. Some methods may need a combiniation of both. See [mocking](mocking.md) for an example of mocking service/grpc calls.

### Arrange

The arrange step should setup any objects and data required for the test case. Objects can be constructed using their normal constuctors and methods, or created using AutoFixture. The example above uses the former, for more information on the latter, [click here](autofixture.md). These objects can then be saved into the database using the `_context` object that is setup in the Init method. Remember to call `_context.SaveChanges();` to ensure the database is updated. Most filler data (ints, strings) should be randomly generated by AutoFixture, to ensure repeat runs of the test with the same database don't clash and cause failures.

### Act

The act step should exercise the main method or function being tested. Typically should be only 1 line.

### Asserts

Asserts should verify that the Act step did what it was supposed to do. For this we are using NUnits constraint-based Assert model, for more details see NUnit's [documentation](https://docs.nunit.org/articles/nunit/writing-tests/assertions/assertion-models/constraint.html). Assertions need to be wrote in a way that repeat runs of a test with the same database don't cause failures (look at filtered views of the database).

## Database Context

The database context of all services use the same `NewMesContext`
Do not make up new database contexts

```csharp
private NewMesContext _context = null!;
```

```csharp
_context = new NewMesContext(contextOptions);
```
